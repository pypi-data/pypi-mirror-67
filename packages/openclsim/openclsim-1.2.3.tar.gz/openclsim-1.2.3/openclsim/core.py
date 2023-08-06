# -*- coding: utf-8 -*-

"""Main module."""

# package(s) related to time, space and id
import json
import logging
import uuid
import itertools

# you need these dependencies (you can get these from anaconda)
# package(s) related to the simulation
import simpy
import networkx as nx

# spatial libraries
import pyproj
import shapely.geometry

# additional packages
import math
import datetime, time
import copy
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class SimpyObject:
    """General object which can be extended by any class requiring a simpy environment

    env: a simpy Environment
    """

    def __init__(self, env, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.env = env


class DebugArgs:
    """Object that logs if leftover args are passed onto it.
    """

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            message = "leftover arguments passed to {}, args: {},  kwargs: {}"
            logger.warn(message.format(self, args, kwargs))
        super().__init__()


class Identifiable:
    """Something that has a name and id

    name: a name
    id: a unique id generated with uuid"""

    def __init__(self, name, ID=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.name = name
        # generate some id, in this case based on m
        self.id = ID if ID else str(uuid.uuid1())


class Locatable:
    """Something with a geometry (geojson format)

    geometry: can be a point as well as a polygon"""

    def __init__(self, geometry, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.geometry = geometry
        self.wgs84 = pyproj.Geod(ellps="WGS84")

    def is_at(self, locatable, tolerance=100):
        current_location = shapely.geometry.asShape(self.geometry)
        other_location = shapely.geometry.asShape(locatable.geometry)
        _, _, distance = self.wgs84.inv(
            current_location.x, current_location.y, other_location.x, other_location.y
        )

        return distance < tolerance


class ReservationContainer(simpy.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.expected_level = self.level
        self._content_available = None
        self._space_available = None

    def reserve_put(self, amount):
        if self.expected_level + amount > self.capacity:
            raise RuntimeError("Attempting to reserve unavailable space")

        self.expected_level += amount

        if (
            self._content_available is not None
            and not self._content_available.triggered
            and amount > 0
        ):
            self._content_available.succeed()

    def reserve_get(self, amount):
        if self.expected_level < amount:
            raise RuntimeError("Attempting to reserve unavailable content")

        self.expected_level -= amount

        if (
            self._space_available is not None
            and not self._space_available.triggered
            and amount > 0
        ):
            self._space_available.succeed()

    @property
    def reserve_put_available(self):
        if self.expected_level < self.capacity:
            return self._env.event().succeed()

        if self._space_available is not None and not self._space_available.triggered:
            return self._space_available

        self._space_available = self._env.event()
        return self._space_available

    @property
    def reserve_get_available(self):
        if self.expected_level > 0:
            return self._env.event().succeed()

        if (
            self._content_available is not None
            and not self._content_available.triggered
        ):
            return self._content_available

        self._content_available = self._env.event()
        return self._content_available


class EventsContainer(simpy.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._get_available_events = {}
        self._put_available_events = {}

    def get_available(self, amount):
        if self.level >= amount:
            return self._env.event().succeed()
        if amount in self._get_available_events:
            return self._get_available_events[amount]
        new_event = self._env.event()
        self._get_available_events[amount] = new_event
        return new_event

    def put_available(self, amount):
        if self.capacity - self.level >= amount:
            return self._env.event().succeed()
        if amount in self._put_available_events:
            return self._put_available_events[amount]
        new_event = self._env.event()
        self._put_available_events[amount] = new_event
        return new_event

    def get_empty_event(self, start_event=False):
        if not start_event:
            return self.empty_event
        elif start_event.processed:
            return self.empty_event
        else:
            return self._env.event()

    def get_full_event(self, start_event=False):
        if not start_event:
            return self.full_event
        elif start_event.processed:
            return self.full_event
        else:
            return self._env.event()

    @property
    def empty_event(self):
        return self.put_available(self.capacity)

    @property
    def full_event(self):
        return self.get_available(self.capacity)

    def put(self, amount):
        put_event = super().put(amount)
        put_event.callbacks.append(self.put_callback)
        return put_event

    def put_callback(self, event):
        for amount in sorted(self._get_available_events):
            if isinstance(self, ReservationContainer):
                if self.expected_level >= amount:
                    self._get_available_events[amount].succeed()
                    del self._get_available_events[amount]
            elif self.level >= amount:
                self._get_available_events[amount].succeed()
                del self._get_available_events[amount]
            else:
                return

    def get(self, amount):
        get_event = super().get(amount)
        get_event.callbacks.append(self.get_callback)
        return get_event

    def get_callback(self, event):
        for amount in sorted(self._put_available_events):
            if isinstance(self, ReservationContainer):
                if self.capacity - self.expected_level >= amount:
                    self._put_available_events[amount].succeed()
                    del self._put_available_events[amount]
            elif self.capacity - self.level >= amount:
                self._put_available_events[amount].succeed()
                del self._put_available_events[amount]
            else:
                return


class HasContainer(SimpyObject):
    """Container class

    capacity: amount the container can hold
    level: amount the container holds initially
    container: a simpy object that can hold stuff"""

    def __init__(self, capacity, level=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        container_class = type(
            "CombinedContainer", (EventsContainer, ReservationContainer), {}
        )
        self.container = container_class(self.env, capacity, init=level)


class EnergyUse(SimpyObject):
    """EnergyUse class

    energy_use_sailing:   function that specifies the fuel use during sailing activity   - input should be time
    energy_use_loading:   function that specifies the fuel use during loading activity   - input should be time
    energy_use_unloading: function that specifies the fuel use during unloading activity - input should be time

    Example function could be as follows.
    The energy use of the loading event is equal to: duration * power_use.

    def energy_use_loading(power_use):
        return lambda x: x * power_use
    """

    def __init__(
        self,
        energy_use_sailing=None,
        energy_use_loading=None,
        energy_use_unloading=None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.energy_use_sailing = energy_use_sailing
        self.energy_use_loading = energy_use_loading
        self.energy_use_unloading = energy_use_unloading


class HasCosts:
    """
    Add cost properties to objects
    """

    def __init__(
        self,
        dayrate=None,
        weekrate=None,
        mobilisation=None,
        demobilisation=None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        """Initialization"""

        assert dayrate != weekrate
        self.dayrate = dayrate if dayrate else weekrate / 7

        self.mobilisation = mobilisation if mobilisation else 0
        self.demobilisation = demobilisation if demobilisation else 0

    @property
    def cost(self):

        cost = (
            (self.log["Timestamp"][-1] - self.log["Timestamp"][0]).total_seconds()
            / 3600
            / 24
            * self.dayrate
            if self.log["Timestamp"]
            else 0
        )

        return cost + self.mobilisation + self.demobilisation


class HasPlume(SimpyObject):
    """Using values from Becker [2014], https://www.sciencedirect.com/science/article/pii/S0301479714005143.

    The values are slightly modified, there is no differences in dragead / bucket drip / cutterhead within this class
    sigma_d = source term fraction due to dredging
    sigma_o = source term fraction due to overflow
    sigma_p = source term fraction due to placement
    f_sett  = fraction of fines that settle within the hopper
    f_trap  = fraction of fines that are trapped within the hopper
    """

    def __init__(
        self,
        sigma_d=0.015,
        sigma_o=0.1,
        sigma_p=0.05,
        f_sett=0.5,
        f_trap=0.01,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        """Initialization"""

        self.sigma_d = sigma_d
        self.sigma_o = sigma_o
        self.sigma_p = sigma_p
        self.f_sett = f_sett
        self.f_trap = f_trap

        self.m_r = 0


class HasSpillCondition(SimpyObject):
    """Condition to stop dredging if certain spill limits are exceeded

    limit = limit of kilograms spilled material
    start = start of the condition
    end   = end of the condition
    """

    def __init__(self, conditions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        limits = []
        starts = []
        ends = []

        if type(conditions) == list:
            for condition in conditions:
                limits.append(simpy.Container(self.env, capacity=condition.spill_limit))
                starts.append(time.mktime(condition.start.timetuple()))
                ends.append(time.mktime(condition.end.timetuple()))

        else:
            limits.append(simpy.Container(self.env, capacity=conditions.spill_limit))
            starts.append(time.mktime(conditions.start.timetuple()))
            ends.append(time.mktime(conditions.end.timetuple()))

        self.SpillConditions = pd.DataFrame.from_dict(
            {"Spill limit": limits, "Criterion start": starts, "Criterion end": ends}
        )

    def check_conditions(self, spill):
        tolerance = math.inf
        waiting = 0

        for i in self.SpillConditions.index:

            if (
                self.SpillConditions["Criterion start"][i] <= self.env.now
                and self.env.now <= self.SpillConditions["Criterion end"][i]
            ):
                tolerance = (
                    self.SpillConditions["Spill limit"][i].capacity
                    - self.SpillConditions["Spill limit"][i].level
                )

                if tolerance < spill:
                    waiting = self.SpillConditions["Criterion end"][i]

                while i + 1 != len(self.SpillConditions.index) and tolerance < spill:
                    if (
                        self.SpillConditions["Criterion end"][i]
                        == self.SpillConditions["Criterion start"][i + 1]
                    ):
                        tolerance = (
                            self.SpillConditions["Spill limit"][i + 1].capacity
                            - self.SpillConditions["Spill limit"][i + 1].level
                        )
                        waiting = self.SpillConditions["Criterion end"][i + 1]

                    i += 1

        return waiting


class SpillCondition:
    """Condition to stop dredging if certain spill limits are exceeded

    limit = limit of kilograms spilled material
    start = start of the condition
    end   = end of the condition
    """

    def __init__(self, spill_limit, start, end, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.spill_limit = spill_limit
        self.start = start
        self.end = end


class HasSpill(SimpyObject):
    """Using relations from Becker [2014], https://www.sciencedirect.com/science/article/pii/S0301479714005143."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

    def spillDredging(
        self,
        processor,
        mover,
        density,
        fines,
        volume,
        dredging_duration,
        overflow_duration=0,
    ):
        """Calculate the spill due to the dredging activity

        density = the density of the dredged material
        fines   = the percentage of fines in the dredged material
        volume  = the dredged volume
        dredging_duration = duration of the dredging event
        overflow_duration = duration of the dredging event whilst overflowing

        m_t = total mass of dredged fines per cycle
        m_d = total mass of spilled fines during one dredging event
        m_h = total mass of dredged fines that enter the hopper

        m_o  = total mass of fine material that leaves the hopper during overflow
        m_op = total mass of fines that are released during overflow that end in dredging plume
        m_r  = total mass of fines that remain within the hopper"""

        m_t = density * fines * volume
        m_d = processor.sigma_d * m_t
        m_h = m_t - m_d

        m_o = (
            (overflow_duration / dredging_duration)
            * (1 - mover.f_sett)
            * (1 - mover.f_trap)
            * m_h
        )
        m_op = mover.sigma_o * m_o
        mover.m_r = m_h - m_o

        processor.log_entry(
            "fines released",
            self.env.now,
            m_d + m_op,
            self.geometry,
            processor.ActivityID,
        )

        return m_d + m_op

    def spillPlacement(self, processor, mover):
        """Calculate the spill due to the placement activity"""
        if isinstance(self, Log):
            processor.log_entry(
                "fines released",
                self.env.now,
                mover.m_r * processor.sigma_p,
                self.geometry,
                processor.ActivityID,
            )

        return mover.m_r * processor.sigma_p


class SoilLayer:
    """ Create a soillayer

    layer = layer number, 0 to n, with 0 the layer at the surface
    material = name of the dredged material
    density = density of the dredged material
    fines = fraction of total that is fine material
    """

    def __init__(self, layer, volume, material, density, fines, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.layer = layer
        self.volume = volume
        self.material = material
        self.density = density
        self.fines = fines


class HasSoil:
    """ Add soil properties to an object

    soil = list of SoilLayer objects
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

        self.soil = {}

    def add_layer(self, soillayer):
        """Add a layer based on a SoilLayer object."""
        for key in self.soil:
            if key == "Layer {:04d}".format(soillayer.layer):
                print(
                    "Soil layer named **Layer {:04d}** already exists".format(
                        soillayer.layer
                    )
                )

        # Add soillayer to self
        self.soil["Layer {:04d}".format(soillayer.layer)] = {
            "Layer": soillayer.layer,
            "Volume": soillayer.volume,
            "Material": soillayer.material,
            "Density": soillayer.density,
            "Fines": soillayer.fines,
        }

        # Make sure that self.soil is always a sorted dict based on layernumber
        soil = copy.deepcopy(self.soil)
        self.soil = {}

        for key in sorted(soil):
            self.soil[key] = soil[key]

    def add_layers(self, soillayers):
        """Add a list layers based on a SoilLayer object."""
        for layer in soillayers:
            self.add_layer(layer)

    def total_volume(self):
        """Determine the total volume of soil."""
        total_volume = 0

        for layer in self.soil:
            total_volume += self.soil[layer]["Volume"]

        return total_volume

    def weighted_average(self, layers, volumes):
        """Create a new SoilLayer object based on the weighted average parameters of extracted layers.

        len(layers) should be len(volumes)"""
        densities = []
        fines = []
        name = "Mixture of: "

        for i, layer in enumerate(layers):
            if 0 < volumes[i]:
                densities.append(self.soil[layer]["Density"])
                fines.append(self.soil[layer]["Fines"])
                name += self.soil[layer]["Material"] + ", "
            else:
                densities.append(0)
                fines.append(0)

        return SoilLayer(
            0,
            sum(volumes),
            name.rstrip(", "),
            np.average(np.asarray(densities), weights=np.asarray(volumes)),
            np.average(np.asarray(fines), weights=np.asarray(volumes)),
        )

    def get_soil(self, volume):
        """Remove soil from self."""

        # If soil is a mover, the mover should be initialized with an empty soil dict after emptying
        if isinstance(self, Movable) and 0 == self.container.level:
            removed_soil = list(self.soil.items())[0]

            self.soil = {}

            return SoilLayer(
                0,
                removed_soil[1]["Volume"],
                removed_soil[1]["Material"],
                removed_soil[1]["Density"],
                removed_soil[1]["Fines"],
            )

        # In all other cases the soil dict should remain, with updated values
        else:
            removed_volume = 0
            layers = []
            volumes = []

            for layer in sorted(self.soil):
                if (volume - removed_volume) <= self.soil[layer]["Volume"]:
                    layers.append(layer)
                    volumes.append(volume - removed_volume)

                    self.soil[layer]["Volume"] -= volume - removed_volume

                    break

                else:
                    removed_volume += self.soil[layer]["Volume"]
                    layers.append(layer)
                    volumes.append(self.soil[layer]["Volume"])

                    self.soil[layer]["Volume"] = 0

            return self.weighted_average(layers, volumes)

    def put_soil(self, soillayer):
        """Add soil to self.

        Add a layer based on a SoilLayer object."""
        # If already soil available
        if self.soil:
            # Can be moveable --> mix
            if isinstance(self, Movable):
                pass

            # Can be site --> add layer or add volume
            else:
                top_layer = list(sorted(self.soil.keys()))[0]

                # If toplayer material is similar to added material --> add volume
                if (
                    self.soil[top_layer]["Material"] == soillayer.material
                    and self.soil[top_layer]["Density"] == soillayer.density
                    and self.soil[top_layer]["Fines"] == soillayer.fines
                ):

                    self.soil[top_layer]["Volume"] += soillayer.volume

                # If not --> add layer
                else:
                    layers = copy.deepcopy(self.soil)
                    self.soil = {}
                    self.add_layer(soillayer)

                    for key in sorted(layers):
                        layers[key]["Layer"] += 1
                        self.add_layer(
                            SoilLayer(
                                layers[key]["Layer"],
                                layers[key]["Volume"],
                                layers[key]["Material"],
                                layers[key]["Density"],
                                layers[key]["Fines"],
                            )
                        )

        # If no soil yet available, add layer
        else:
            self.add_layer(soillayer)

    def get_properties(self, amount):
        """Get the soil properties for a certain amount"""
        volumes = []
        layers = []
        volume = 0

        for layer in sorted(self.soil):
            if (amount - volume) <= self.soil[layer]["Volume"]:
                volumes.append(amount - volume)
                layers.append(layer)
                break
            else:
                volumes.append(self.soil[layer]["Volume"])
                layers.append(layer)
                volume += self.soil[layer]["Volume"]

        properties = self.weighted_average(layers, volumes)

        return properties.density, properties.fines


class HasWeather:
    """HasWeather class

    Used to add weather conditions to a project site
    name: name of .csv file in folder

    year: name of the year column
    month: name of the month column
    day: name of the day column

    timestep: size of timestep to interpolate between datapoints (minutes)
    bed: level of the seabed / riverbed with respect to CD (meters)
    """

    def __init__(
        self,
        dataframe,
        timestep=10,
        bed=None,
        waveheight_column="Hm0 [m]",
        waveperiod_column="Tp [s]",
        waterlevel_column="Tide [m]",
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.timestep = datetime.timedelta(minutes=timestep)

        data = {}
        for key in dataframe:
            series = (
                pd.Series(dataframe[key], index=dataframe.index)
                .fillna(0)
                .resample(self.timestep)
                .interpolate("linear")
            )

            data[key] = series.values

        data["Index"] = series.index
        self.metocean_data = pd.DataFrame.from_dict(data)
        self.metocean_data.index = self.metocean_data["Index"]
        self.metocean_data.drop(["Index"], axis=1, inplace=True)

        # Column names
        self.waveheight = waveheight_column
        self.waveperiod = waveperiod_column
        self.waterlevel = waterlevel_column
        self.waterdepth = "Water depth"

        if bed:
            self.metocean_data[self.waterdepth] = (
                self.metocean_data[waterlevel_column] - bed
            )


class HasWorkabilityCriteria:
    """HasWorkabilityCriteria class

    Used to add workability criteria
    """

    def __init__(self, criteria, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.criteria = criteria
        self.work_restrictions = {}

    def calc_work_restrictions(self, location):
        self.work_restrictions[location.name] = {}

        # Loop through series to find windows
        for criterion in self.criteria:
            index = location.metocean_data[criterion.condition].index
            values = location.metocean_data[criterion.condition].values
            in_range = False
            ranges = []

            for i, value in enumerate(values):
                if value <= criterion.maximum:
                    if i == 0:
                        begin = index[i]
                    elif not in_range:
                        begin = index[i]

                    in_range = True
                elif in_range:
                    in_range = False
                    end = index[i]

                    if (end - begin) >= criterion.window_length:
                        ranges.append(
                            (
                                begin.to_datetime64(),
                                (end - criterion.window_length).to_datetime64(),
                            )
                        )

            self.work_restrictions[location.name][criterion.event_name] = np.array(
                ranges
            )

    def check_weather_restriction(self, location, event):
        waiting = []

        if location.name not in self.work_restrictions.keys():
            self.calc_work_restrictions(location)
        elif event not in self.work_restrictions[location.name].keys():
            self.calc_work_restrictions(location)

        for criterion in sorted(self.work_restrictions[location.name].keys()):
            ranges = self.work_restrictions[location.name][criterion]

            t = datetime.datetime.fromtimestamp(self.env.now)
            t = pd.Timestamp(t).to_datetime64()
            i = ranges[:, 0].searchsorted(t)

            if i > 0 and (ranges[i - 1][0] <= t <= ranges[i - 1][1]):
                waiting.append(pd.Timedelta(0).total_seconds())
            elif i + 1 < len(ranges):
                waiting.append(pd.Timedelta(ranges[i, 0] - t).total_seconds())
            else:
                print("\nSimulation cannot continue.")
                print("Simulation time exceeded the available metocean data.")

                self.env.exit()

        if waiting:
            self.log_entry(
                "waiting for weather start",
                self.env.now,
                waiting,
                self.geometry,
                self.ActivityID,
            )
            yield self.env.timeout(np.max(waiting))
            self.log_entry(
                "waiting for weather stop",
                self.env.now,
                waiting,
                self.geometry,
                self.ActivityID,
            )


class WorkabilityCriterion:
    """WorkabilityCriterion class

    Used to add limits to vessels (and therefore acitivities)
    event_name: name of the event for which this criterion applies
    condition: column name of the metocean data (Hs, Tp, etc.)
    minimum: minimum value
    maximum: maximum value
    window_length: minimal length of the window (minutes)"""

    def __init__(
        self,
        event_name,
        condition,
        minimum=math.inf * -1,
        maximum=math.inf,
        window_length=datetime.timedelta(minutes=60),
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.event_name = event_name
        self.condition = condition
        self.minimum = minimum
        self.maximum = maximum
        self.window_length = window_length


class HasDepthRestriction:
    """HasDepthRestriction class

    Used to add depth limits to vessels
    draught: should be a lambda function with input variable container.volume
    waves: list with wave_heights
    ukc: list with ukc, corresponding to wave_heights

    filling: filling degree [%]
    min_filling: minimal filling degree [%]
    max_filling: max filling degree [%]
    """

    def __init__(
        self,
        compute_draught,
        ukc,
        waves=None,
        filling=None,
        min_filling=None,
        max_filling=None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        """Initialization"""

        # Information required to determine whether vessel can access an area
        self.compute_draught = compute_draught
        self.ukc = ukc
        self.waves = waves

        # Information require to self-select filling degree
        if min_filling is not None and max_filling is not None:
            assert min_filling <= max_filling

        self.filling = int(filling) if filling is not None else None
        self.min_filling = int(min_filling) if min_filling is not None else int(0)
        self.max_filling = int(max_filling) if max_filling is not None else int(100)

        self.depth_data = {}

    def calc_depth_restrictions(self, location, processor):
        # Minimal waterdepth should be draught + ukc
        # Waterdepth is tide - depth site
        # For empty to full [20%, 25%, 30%, ... 90%, 95%, 100%]

        self.depth_data[location.name] = {}

        if not self.filling:
            filling_degrees = np.linspace(
                self.min_filling,
                self.max_filling,
                (self.max_filling - self.min_filling) + 1,
                dtype=int,
            )
        else:
            filling_degrees = [self.filling]

        for i in filling_degrees:
            filling_degree = i / 100

            # Determine characteristics based on filling
            draught = self.compute_draught(filling_degree)
            duration = datetime.timedelta(
                seconds=processor.unloading(
                    self,
                    location,
                    self.container.level - filling_degree * self.container.capacity,
                )
            )

            # Make dataframe based on characteristics
            df = location.metocean_data.copy()
            df["Required depth"] = df[location.waveheight].apply(
                lambda s: self.calc_required_depth(draught, s)
            )
            series = pd.Series(df["Required depth"] <= df[location.waterdepth])

            # Loop through series to find windows
            index = series.index
            values = series.values
            in_range = False
            ranges = []

            for i, value in enumerate(values):
                if value == True:
                    if i == 0:
                        begin = index[i]
                    elif not in_range:
                        begin = index[i]

                    in_range = True
                elif in_range:
                    in_range = False
                    end = index[i]

                    if (end - begin) >= duration:
                        ranges.append(
                            (begin.to_datetime64(), (end - duration).to_datetime64())
                        )

            self.depth_data[location.name][filling_degree] = {
                "Volume": filling_degree * self.container.capacity,
                "Draught": draught,
                "Ranges": np.array(ranges),
            }

    def viable_time_windows(self, fill_degree, duration, location):
        duration = datetime.timedelta(seconds=duration)
        draught = self.compute_draught(fill_degree)

        # Make dataframe based on characteristics
        df = location.metocean_data.copy()
        df["Required depth"] = df[location.waveheight].apply(
            lambda s: self.calc_required_depth(draught, s)
        )
        series = pd.Series(df["Required depth"] <= df[location.waterdepth])
        # Loop through series to find windows
        index = series.index
        values = series.values
        in_range = False
        ranges = []
        for i, value in enumerate(values):
            if value == True:
                if i == 0:
                    begin = index[i]
                elif not in_range:
                    begin = index[i]

                in_range = True
            elif in_range:
                in_range = False
                end = index[i]

                if (end - begin) >= duration:
                    ranges.append(
                        (begin.to_datetime64(), (end - duration).to_datetime64())
                    )

        self.depth_data[location.name][fill_degree] = {
            "Volume": fill_degree * self.container.capacity,
            "Draught": draught,
            "Ranges": np.array(ranges),
        }

    def check_depth_restriction(self, location, fill_degree, duration):
        if location.name not in self.depth_data.keys():
            fill_degree = int(fill_degree * 100) / 100
            self.depth_data[location.name] = {}
            self.viable_time_windows(fill_degree, duration, location)

            ranges = self.depth_data[location.name][int(fill_degree * 100) / 100][
                "Ranges"
            ]

        elif fill_degree not in self.depth_data[location.name].keys():
            fill_degree = int(fill_degree * 100) / 100
            self.viable_time_windows(fill_degree, duration, location)

            ranges = self.depth_data[location.name][int(fill_degree * 100) / 100][
                "Ranges"
            ]

        else:
            ranges = self.depth_data[location.name][int(fill_degree * 100) / 100][
                "Ranges"
            ]

        if len(ranges) == 0:
            self.log_entry(
                "No actual allowable draught available - starting anyway",
                self.env.now,
                -1,
                self.geometry,
                self.ActivityID,
            )
            waiting = 0

        else:
            t = datetime.datetime.fromtimestamp(self.env.now)
            t = pd.Timestamp(t).to_datetime64()
            i = ranges[:, 0].searchsorted(t)

            if i > 0 and (ranges[i - 1][0] <= t <= ranges[i - 1][1]):
                waiting = pd.Timedelta(0).total_seconds()
            elif i + 1 < len(ranges):
                waiting = pd.Timedelta(ranges[i, 0] - t).total_seconds()
            else:
                print("Exceeding time")
                waiting = 0

        if waiting != 0:
            self.log_entry(
                "waiting for tide start",
                self.env.now,
                waiting,
                self.geometry,
                self.ActivityID,
            )
            yield self.env.timeout(waiting)
            self.log_entry(
                "waiting for tide stop",
                self.env.now,
                waiting,
                self.geometry,
                self.ActivityID,
            )

    def calc_required_depth(self, draught, wave_height):
        required_depth = np.nan

        if self.waves:
            for i, wave in enumerate(self.waves):
                if wave_height <= wave:
                    required_depth = self.ukc[i] + draught

            return required_depth

        else:
            return self.ukc + draught

    def check_optimal_filling(self, loader, unloader, origin, destination):
        # Calculate depth restrictions
        if not self.depth_data:
            if isinstance(origin, HasWeather):
                self.calc_depth_restrictions(origin, loader)
            if isinstance(destination, HasWeather):
                self.calc_depth_restrictions(destination, unloader)

        elif (
            origin.name not in self.depth_data.keys()
            or destination.name not in self.depth_data.keys()
        ):
            if isinstance(origin, HasWeather):
                self.calc_depth_restrictions(origin, loader)
            if isinstance(destination, HasWeather):
                self.calc_depth_restrictions(destination, unloader)

        # If a filling degee has been specified
        if self.filling is not None:
            return self.filling * self.container.capacity / 100

        elif destination.name not in self.depth_data.keys():
            return self.container.capacity

        # If not, try to optimize the load with regard to the tidal window
        else:
            loads = []
            waits = []
            amounts = []

            fill_degrees = self.depth_data[destination.name].keys()

            for filling in fill_degrees:
                ranges = self.depth_data[destination.name][filling]["Ranges"]

                if len(ranges) != 0:
                    # Determine length of cycle
                    loading = loader.loading(
                        origin,
                        destination,
                        filling * self.container.capacity - self.container.level,
                    )

                    orig = shapely.geometry.asShape(origin.geometry)
                    dest = shapely.geometry.asShape(destination.geometry)
                    _, _, distance = self.wgs84.inv(orig.x, orig.y, dest.x, dest.y)
                    sailing_full = distance / self.compute_v(0)
                    sailing_full = distance / self.compute_v(filling)

                    duration = sailing_full + loading + sailing_full

                    # Determine waiting time
                    t = datetime.datetime.fromtimestamp(self.env.now + duration)
                    t = pd.Timestamp(t).to_datetime64()
                    i = ranges[:, 0].searchsorted(t)

                    if i > 0 and (ranges[i - 1][0] <= t <= ranges[i - 1][1]):
                        waiting = pd.Timedelta(0).total_seconds()
                    elif i != len(ranges):
                        waiting = pd.Timedelta(ranges[i, 0] - t).total_seconds()
                    else:
                        print("\nSimulation cannot continue.")
                        print("Simulation time exceeded the available metocean data.")

                        self.env.exit()

                    # In case waiting is always required
                    loads.append(filling * self.container.capacity)
                    waits.append(waiting)

                    if waiting < destination.timestep.total_seconds():
                        amounts.append(filling * self.container.capacity)

            # Check if there is a better filling degree
            if amounts:
                return max(amounts)
            elif loads:
                cargo = 0

                for i, _ in enumerate(loads):
                    if waits[i] == min(waits):
                        cargo = loads[i]

                return cargo

    @property
    def current_draught(self):
        return self.compute_draught(self.container.level / self.container.capacity)


class Movable(SimpyObject, Locatable):
    """Movable class

    Used for object that can move with a fixed speed
    geometry: point used to track its current location
    v: speed"""

    def __init__(self, v=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.v = v

    def move(self, destination, engine_order=1.0):
        """determine distance between origin and destination. 
        Yield the time it takes to travel based on flow properties and load factor of the flow."""

        # Log the start event
        self.log_sailing(event="start")

        # Determine the sailing_duration
        sailing_duration = self.sailing_duration(
            self.geometry, destination, engine_order
        )

        # Check out the time based on duration of sailing event
        yield self.env.timeout(sailing_duration)

        # Set mover geometry to destination geometry
        self.geometry = shapely.geometry.asShape(destination.geometry)

        # Debug logs
        logger.debug("  duration: " + "%4.2f" % (sailing_duration / 3600) + " hrs")

        # Log the stop event
        self.log_sailing(event="stop")

    @property
    def current_speed(self):
        return self.v

    def log_sailing(self, event):
        """ Log the start or stop of the sailing event """

        if isinstance(self, HasContainer):
            status = "filled" if self.container.level > 0 else "empty"
            self.log_entry(
                "sailing {} {}".format(status, event),
                self.env.now,
                self.container.level,
                self.geometry,
                self.ActivityID,
            )
        else:
            self.log_entry(
                "sailing {}".format(event),
                self.env.now,
                -1,
                self.geometry,
                self.ActivityID,
            )

    def sailing_duration(self, origin, destination, engine_order, verbose=True):
        """ Determine the sailing duration """
        orig = shapely.geometry.asShape(self.geometry)
        dest = shapely.geometry.asShape(destination.geometry)
        _, _, distance = self.wgs84.inv(orig.x, orig.y, dest.x, dest.y)

        # Log the energy use
        self.energy_use(distance, self.current_speed * engine_order)

        return distance / (self.current_speed * engine_order)

    def energy_use(self, distance, speed):
        """ Determine the energy use """
        if isinstance(self, EnergyUse):
            # message depends on filling degree: if container is empty --> sailing empt
            if not isinstance(self, HasContainer) or self.container.level == 0:
                message = "Energy use sailing empty"
                filling = 0.0
            else:
                message = "Energy use sailing filled"
                filling = self.container.level / self.container.capacity

            energy = self.energy_use_sailing(distance, speed, filling)
            self.log_entry(
                message, self.env.now, energy, self.geometry, self.ActivityID
            )


class ContainerDependentMovable(Movable, HasContainer):
    """ContainerDependentMovable class

    Used for objects that move with a speed dependent on the container level
    compute_v: a function, given the fraction the container is filled (in [0,1]), returns the current speed"""

    def __init__(self, compute_v, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.compute_v = compute_v

    @property
    def current_speed(self):
        return self.compute_v(self.container.level / self.container.capacity)

    def determine_amount(self, origins, destinations, loader, unloader, filling=1):
        """ Determine the maximum amount that can be carried """

        # Determine the basic amount that should be transported
        all_amounts = {}
        all_amounts.update(
            {
                "origin." + origin.id: origin.container.expected_level
                for origin in origins
            }
        )
        all_amounts.update(
            {
                "destination."
                + destination.id: destination.container.capacity
                - destination.container.expected_level
                for destination in destinations
            }
        )

        origin_requested = 0
        destination_requested = 0

        for key in all_amounts.keys():
            if "origin." in key:
                origin_requested += all_amounts[key]
            else:
                destination_requested += all_amounts[key]

        amount = min(
            self.container.capacity * filling - self.container.level,
            origin_requested,
            destination_requested,
        )

        # If the mover has a function to optimize its load, check if the amount should be changed
        if not hasattr(self, "check_optimal_filling"):
            return amount, all_amounts

        else:
            amounts = [amount]
            amounts.extend(
                [
                    self.check_optimal_filling(loader, unloader, origin, destination)
                    for origin, destination in itertools.product(origins, destinations)
                ]
            )

            return min(amounts), all_amounts

    def determine_schedule(self, amount, all_amounts, origins, destinations):
        """ 
        Define a strategy for passing through the origins and destinations
        Implemented is FIFO: First origins will start and first destinations will start.
        """
        self.vrachtbrief = {"Type": [], "ID": [], "Priority": [], "Amount": []}

        def update_vrachtbrief(typestring, id, priority, amount):
            """ Update the vrachtbrief """

            self.vrachtbrief["Type"].append(typestring)
            self.vrachtbrief["ID"].append(id)
            self.vrachtbrief["Priority"].append(priority)
            self.vrachtbrief["Amount"].append(amount)

        to_retrieve = 0
        to_place = 0

        # reserve the amount in origin an destination
        for origin in origins:
            if all_amounts["origin." + origin.id] == 0:
                continue
            elif all_amounts["origin." + origin.id] <= amount - to_retrieve:
                to_retrieve += all_amounts["origin." + origin.id]
                origin.container.reserve_get(all_amounts["origin." + origin.id])
                update_vrachtbrief(
                    "Origin", origin, 1, all_amounts["origin." + origin.id]
                )

            else:
                origin.container.reserve_get(amount - to_retrieve)
                update_vrachtbrief("Origin", origin, 1, amount - to_retrieve)
                break

        for destination in destinations:
            if all_amounts["destination." + destination.id] == 0:
                continue
            elif all_amounts["destination." + destination.id] <= amount - to_place:
                to_place += all_amounts["destination." + destination.id]
                destination.container.reserve_put(
                    all_amounts["destination." + destination.id]
                )
                update_vrachtbrief(
                    "Destination",
                    destination,
                    1,
                    all_amounts["destination." + destination.id],
                )

            else:
                destination.container.reserve_put(amount - to_place)
                update_vrachtbrief("Destination", destination, 1, amount - to_place)
                break

        return pd.DataFrame.from_dict(self.vrachtbrief).sort_values("Priority")


class Routeable(Movable):
    """
    Moving folling a certain path
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

    def determine_route(self, origin, destination):
        """ Determine the fastest sailing route based on distance """

        # If travelling on route is required, assert environment has a graph
        assert hasattr(self.env, "FG")

        # Origin is geom - convert to node on graph
        geom = nx.get_node_attributes(self.env.FG, "geometry")

        for node in geom.keys():
            if np.isclose(origin.x, geom[node].x, rtol=1e-8) and np.isclose(
                origin.y, geom[node].y, rtol=1e-8
            ):
                origin = node
                break

        if origin != node:
            raise AssertionError("The origin cannot be found in the graph")

        # Determine fastest route
        if hasattr(destination, "name"):
            if destination.name in list(self.env.FG.nodes):
                return nx.dijkstra_path(self.env.FG, origin, destination.name)

        for node in geom.keys():
            if (
                destination.geometry.x == geom[node].x
                and destination.geometry.y == geom[node].y
            ):
                destination = node
                return nx.dijkstra_path(self.env.FG, origin, destination)

        # If no route is returned
        raise AssertionError("The destination cannot be found in the graph")

    def determine_speed(self, node_from, node_to):
        """ Determine the sailing speed based on edge properties """
        edge_attrs = self.env.FG.get_edge_data(node_from, node_to)

        if not edge_attrs:
            return self.current_speed

        elif "maxSpeed" in edge_attrs.keys():
            return min(self.current_speed, edge_attrs["maxSpeed"])

        else:
            return self.current_speed

    def sailing_duration(self, origin, destination, engine_order, verbose=True):
        """ Determine the sailing duration based on the properties of the sailing route """

        # A dict with all nodes and the geometry property
        geom = nx.get_node_attributes(self.env.FG, "geometry")

        # Determine the shortest route from origin to destination
        route = self.determine_route(origin, destination)

        # Determine the duration and energy use of following the route
        duration = 0
        energy = 0

        for i, _ in enumerate(route):
            if i + 1 != len(route):
                orig = shapely.geometry.asShape(geom[route[i]])
                dest = shapely.geometry.asShape(geom[route[i + 1]])

                distance = self.wgs84.inv(orig.x, orig.y, dest.x, dest.y)[2]
                speed = self.determine_speed(route[i], route[i + 1])

                duration += distance / speed
                energy += self.energy_use(distance, speed)

                self.log_entry(
                    "Sailing", self.env.now + duration, 0, dest, self.ActivityID
                )

        # Log energy use
        self.log_energy_use(energy)

        return duration

    def energy_use(self, distance, speed):
        if isinstance(self, EnergyUse):
            return self.energy_use_sailing(distance, speed)
        else:
            return 0

    def log_energy_use(self, energy):
        if 0 < energy:
            self.log_entry(
                "Energy use sailing",
                self.env.now,
                energy,
                self.geometry,
                self.ActivityID,
            )


class ContainerDependentRouteable(ContainerDependentMovable, Routeable):
    """ContainerDependentRouteable class

    Used for objects that move with a speed dependent on the container level
    compute_v: a function, given the fraction the container is filled (in [0,1]), returns the current speed"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

    @property
    def current_speed(self):
        return self.compute_v(self.container.level / self.container.capacity)

    def energy_use(self, distance, speed):
        if isinstance(self, EnergyUse):
            filling = self.container.level / self.container.capacity
            return self.energy_use_sailing(distance, speed, filling)
        else:
            return 0

    def log_energy_use(self, energy):
        if 0 < energy:
            status = "filled" if self.container.level > 0 else "empty"

            self.log_entry(
                "Energy use sailing {}".format(status),
                self.env.now,
                energy,
                self.geometry,
                self.ActivityID,
            )


class HasResource(SimpyObject):
    """HasProcessingLimit class

    Adds a limited Simpy resource which should be requested before the object is used for processing."""

    def __init__(self, nr_resources=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.resource = simpy.Resource(self.env, capacity=nr_resources)


class Log(SimpyObject):
    """Log class

    log: log message [format: 'start activity' or 'stop activity']
    t: timestamp
    value: a value can be logged as well
    geometry: value from locatable (lat, lon)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.log = {
            "Message": [],
            "Timestamp": [],
            "Value": [],
            "Geometry": [],
            "ActivityID": [],
        }

    def log_entry(self, log, t, value, geometry_log, ActivityID):
        """Log"""
        self.log["Message"].append(log)
        self.log["Timestamp"].append(datetime.datetime.fromtimestamp(t))
        self.log["Value"].append(value)
        self.log["Geometry"].append(geometry_log)
        self.log["ActivityID"].append(ActivityID)

    def get_log_as_json(self):
        json = []
        for msg, t, value, geometry_log in zip(
            self.log["Message"],
            self.log["Timestamp"],
            self.log["Value"],
            self.log["Geometry"],
        ):
            json.append(
                dict(
                    type="Feature",
                    geometry=shapely.geometry.mapping(geometry_log)
                    if geometry_log is not None
                    else "None",
                    properties=dict(
                        message=msg, time=time.mktime(t.timetuple()), value=value
                    ),
                )
            )
        return json


class LoadingFunction:
    """
    Create a loading function and add it a processor.
    This is a generic and easy to read function, you can create your own LoadingFunction class and add this as a mixin.

    loading_rate: the rate at which units are loaded per second
    load_manoeuvring: the time it takes to manoeuvring in minutes
    """

    def __init__(self, loading_rate, load_manoeuvring=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.loading_rate = loading_rate
        self.load_manoeuvring = load_manoeuvring

    def loading(self, origin, destination, amount):
        """
        Determine the duration based on an amount that is given as input with processing.
        The origin an destination are also part of the input, because other functions might be dependent on the location.
        """

        if not hasattr(self.loading_rate, "__call__"):
            return amount / self.loading_rate + self.load_manoeuvring * 60
        else:
            return (
                self.loading_rate(self.container.level, self.container.level + amount)
                + self.load_manoeuvring * 60
            )


class UnloadingFunction:
    """
    Create an unloading function and add it a processor.
    This is a generic and easy to read function, you can create your own LoadingFunction class and add this as a mixin.

    unloading_rate: the rate at which units are loaded per second
    unload_manoeuvring: the time it takes to manoeuvring in minutes
    """

    def __init__(self, unloading_rate, unload_manoeuvring=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""
        self.unloading_rate = unloading_rate
        self.unload_manoeuvring = unload_manoeuvring

    def unloading(self, origin, destination, amount):
        """
        Determine the duration based on an amount that is given as input with processing.
        The origin an destination are also part of the input, because other functions might be dependent on the location.
        """

        if not hasattr(self.unloading_rate, "__call__"):
            return amount / self.unloading_rate + self.unload_manoeuvring * 60
        else:
            return (
                self.unloading_rate(self.container.level, self.container.level - amount)
                + self.unload_manoeuvring * 60
            )


class LoadingSubcycle:
    """
    loading_subcycle: pandas dataframe with at least the columns EventName (str) and Duration (int or float in minutes)
    """

    def __init__(self, loading_subcycle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

        self.loading_subcycle = loading_subcycle

        if type(self.loading_subcycle) != pd.core.frame.DataFrame:
            raise AssertionError("The subcycle table has to be a Pandas DataFrame")
        else:
            if "EventName" not in list(
                self.loading_subcycle.columns
            ) or "Duration" not in list(self.loading_subcycle.columns):
                raise AssertionError(
                    "The subcycle table should specify events and durations with the columnnames EventName and Duration respectively."
                )


class UnloadingSubcycle:
    """
    unloading_subcycle: pandas dataframe with at least the columns EventName (str) and Duration (int or float in minutes)
    """

    def __init__(self, unloading_subcycle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

        self.unloading_subcycle = unloading_subcycle

        if type(self.unloading_subcycle) != pd.core.frame.DataFrame:
            raise AssertionError("The subcycle table has to be a Pandas DataFrame")
        else:
            if "EventName" not in list(
                self.unloading_subcycle.columns
            ) or "Duration" not in list(self.unloading_subcycle.columns):
                raise AssertionError(
                    "The subcycle table should specify events and durations with the columnnames EventName and Duration respectively."
                )


class Processor(SimpyObject):
    """Processor class

    Adds the loading and unloading components and checks for possible downtime. 
    
    If the processor class is used to allow "loading" or "unloading" the mixins "LoadingFunction" and "UnloadingFunction" should be added as well. 
    If no functions are used a subcycle should be used, which is possible with the mixins "LoadingSubcycle" and "UnloadingSubcycle".
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Initialization"""

        message = "{} has no (un)loading(_subcycle) attribute".format(self)
        assert (
            hasattr(self, "loading")
            or hasattr(self, "unloading")
            or hasattr(self, "loading_subcycle")
            or hasattr(self, "unloading_subcycle")
        ), message

        # Inherit the (un)loading functions
        if not hasattr(self, "loading"):
            self.loading = None
        if not hasattr(self, "unloading"):
            self.unloading = None

        # Inherit the subcycles
        if not hasattr(self, "loading_subcycle"):
            self.loading_subcycle = None
        if not hasattr(self, "unloading_subcycle"):
            self.unloading_subcycle = None

    # noinspection PyUnresolvedReferences
    def process(self, ship, desired_level, site):
        """Moves content from ship to the site or from the site to the ship to ensure that the ship's container reaches
        the desired level. Yields the time it takes to process."""

        # Before starting to process, check the following requirements
        # Make sure that both objects have storage
        assert isinstance(ship, HasContainer) and isinstance(site, HasContainer)
        # Make sure that both objects allow processing
        assert isinstance(ship, HasResource) and isinstance(site, HasResource)
        # Make sure that the processor (self), container and site can log the events
        assert isinstance(self, Log) and isinstance(ship, Log) and isinstance(site, Log)
        # Make sure that the processor, origin and destination are all at the same location
        assert self.is_at(site)
        assert ship.is_at(site)

        current_level = ship.container.level
        if current_level < desired_level:
            amount = desired_level - current_level
            origin = site
            destination = ship
            rate = self.loading
            subcycle = self.loading_subcycle
        else:
            amount = current_level - desired_level
            origin = ship
            destination = site
            rate = self.unloading
            subcycle = self.unloading_subcycle

        if rate:
            duration = rate(origin, destination, amount)

            yield from self.check_possible_downtime(
                origin, destination, duration, ship, site, desired_level, amount
            )

        elif type(subcycle) == pd.core.frame.DataFrame:
            duration = 0

            for _ in range(int(amount)):
                for i in subcycle.index:
                    duration += subcycle.iloc[i]["Duration"] * 60
                    yield from self.check_possible_downtime(
                        origin, destination, duration, ship, site, desired_level, 1
                    )

        # Shift volumes in containers
        start_time = self.env.now
        yield origin.container.get(amount)
        end_time = self.env.now
        if start_time != end_time:
            self.log_entry(
                log="waiting origin content start",
                t=start_time,
                value=amount,
                geometry_log=self.geometry,
                activityID=self.ActivityID,
            )
            self.log_entry(
                log="waiting origin content stop",
                t=end_time,
                value=amount,
                geometry_log=self.geometry,
                activityID=self.ActivityID,
            )

        # Checkout the time
        origin.log_entry(
            "unloading start",
            self.env.now,
            origin.container.level,
            self.geometry,
            self.ActivityID,
        )
        destination.log_entry(
            "loading start",
            self.env.now,
            destination.container.level,
            self.geometry,
            self.ActivityID,
        )

        if self != origin and self != destination:
            self.log_entry(
                "loading start", self.env.now, 0, self.geometry, self.ActivityID
            )

        yield self.env.timeout(duration)

        # Add spill the location where processing is taking place
        self.addSpill(origin, destination, amount, duration)

        # Shift soil from container volumes
        self.shiftSoil(origin, destination, amount)

        # Compute the energy use
        self.computeEnergy(duration, origin, destination)

        origin.log_entry(
            "unloading stop",
            self.env.now,
            origin.container.level + amount,
            self.geometry,
            self.ActivityID,
        )
        destination.log_entry(
            "loading stop",
            self.env.now,
            destination.container.level + amount,
            self.geometry,
            self.ActivityID,
        )

        if self != origin and self != destination:
            self.log_entry(
                "loading stop", self.env.now, amount, self.geometry, self.ActivityID
            )

        start_time = self.env.now
        yield destination.container.put(amount)
        end_time = self.env.now
        if start_time != end_time:
            self.log_entry(
                log="waiting destination content start",
                t=start_time,
                value=amount,
                geometry_log=self.geometry,
                activityID=self.ActivityID,
            )
            self.log_entry(
                log="waiting destination content stop",
                t=end_time,
                value=amount,
                geometry_log=self.geometry,
                activityID=self.ActivityID,
            )

        logger.debug("  process:        " + "%4.2f" % (duration / 3600) + " hrs")

    def check_possible_downtime(
        self, origin, destination, duration, ship, site, desired_level, amount
    ):
        # Activity can only start if environmental conditions allow it
        time = 0

        # Waiting event should be combined to check if all conditions allow starting
        while time != self.env.now:
            time = self.env.now

            # Check weather
            yield from self.checkWeather(origin, destination, duration)

            # Check tide
            yield from self.checkTide(
                ship=ship, site=site, desired_level=desired_level, duration=duration
            )

            # Check spill
            yield from self.checkSpill(origin, destination, amount)

    def computeEnergy(self, duration, origin, destination):
        """
        duration: duration of the activity in seconds
        origin: origin of the moved volume (the computed amount)
        destination: destination of the moved volume (the computed amount)

        There are three options:
          1. Processor is also origin, destination could consume energy
          2. Processor is also destination, origin could consume energy
          3. Processor is neither destination, nor origin, but both could consume energy
        """

        # If self == origin --> unloading
        if self == origin:
            if isinstance(self, EnergyUse):
                energy = self.energy_use_unloading(duration)
                message = "Energy use unloading"
                self.log_entry(
                    message, self.env.now, energy, self.geometry, self.ActivityID
                )
            if isinstance(destination, EnergyUse):
                energy = destination.energy_use_loading(duration)
                message = "Energy use loading"
                destination.log_entry(
                    message, self.env.now, energy, destination.geometry, self.ActivityID
                )

        # If self == destination --> loading
        elif self == destination:
            if isinstance(self, EnergyUse):
                energy = self.energy_use_loading(duration)
                message = "Energy use loading"
                self.log_entry(
                    message, self.env.now, energy, self.geometry, self.ActivityID
                )
            if isinstance(origin, EnergyUse):
                energy = origin.energy_use_unloading(duration)
                message = "Energy use unloading"
                origin.log_entry(
                    message, self.env.now, energy, origin.geometry, self.ActivityID
                )

        # If self != origin and self != destination --> processing
        else:
            if isinstance(self, EnergyUse):
                energy = self.energy_use_loading(duration)
                message = "Energy use loading"
                self.log_entry(
                    message, self.env.now, energy, self.geometry, self.ActivityID
                )
            if isinstance(origin, EnergyUse):
                energy = origin.energy_use_unloading(duration)
                message = "Energy use unloading"
                origin.log_entry(
                    message, self.env.now, energy, origin.geometry, self.ActivityID
                )
            if isinstance(destination, EnergyUse):
                energy = destination.energy_use_loading(duration)
                message = "Energy use loading"
                destination.log_entry(
                    message, self.env.now, energy, destination.geometry, self.ActivityID
                )

    def checkSpill(self, origin, destination, amount):
        """
        duration: duration of the activity in seconds
        origin: origin of the moved volume (the computed amount)
        destination: destination of the moved volume (the computed amount)

        There are three options:
          1. Processor is also origin, destination could have spill requirements
          2. Processor is also destination, origin could have spill requirements
          3. Processor is neither destination, nor origin, but both could have spill requirements

        Result of this function is possible waiting, spill is added later on and does not depend on possible requirements
        """

        # If self == origin --> destination is a placement location
        if self == origin:
            if (
                isinstance(destination, HasSpillCondition)
                and isinstance(self, HasSoil)
                and isinstance(self, HasPlume)
            ):
                density, fines = self.get_properties(amount)
                spill = self.sigma_d * density * fines * amount

                waiting = destination.check_conditions(spill)

                if 0 < waiting:
                    self.log_entry(
                        "waiting for spill start",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )
                    yield self.env.timeout(waiting - self.env.now)
                    self.log_entry(
                        "waiting for spill stop",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )

        # If self == destination --> origin is a retrieval location
        elif self == destination:
            if (
                isinstance(origin, HasSpillCondition)
                and isinstance(origin, HasSoil)
                and isinstance(self, HasPlume)
            ):
                density, fines = origin.get_properties(amount)
                spill = self.sigma_d * density * fines * amount

                waiting = origin.check_conditions(spill)

                if 0 < waiting:
                    self.log_entry(
                        "waiting for spill start",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )
                    yield self.env.timeout(waiting - self.env.now)
                    self.log_entry(
                        "waiting for spill stop",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )

        # If self != origin and self != destination --> processing
        else:
            if (
                isinstance(destination, HasSpillCondition)
                and isinstance(origin, HasSoil)
                and isinstance(self, HasPlume)
            ):
                density, fines = origin.get_properties(amount)
                spill = self.sigma_d * density * fines * amount

                waiting = destination.check_conditions(spill)

                if 0 < waiting:
                    self.log_entry(
                        "waiting for spill start",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )
                    yield self.env.timeout(waiting - self.env.now)
                    self.log_entry(
                        "waiting for spill stop",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )

            elif (
                isinstance(origin, HasSpillCondition)
                and isinstance(origin, HasSoil)
                and isinstance(self, HasPlume)
            ):
                density, fines = origin.get_properties(amount)
                spill = self.sigma_d * density * fines * amount

                waiting = origin.check_conditions(spill)

                if 0 < waiting:
                    self.log_entry(
                        "waiting for spill start",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )
                    yield self.env.timeout(waiting - self.env.now)
                    self.log_entry(
                        "waiting for spill stop",
                        self.env.now,
                        0,
                        self.geometry,
                        self.ActivityID,
                    )

    def checkTide(self, ship, site, desired_level, duration):
        if hasattr(ship, "calc_depth_restrictions") and isinstance(site, HasWeather):
            max_level = max(ship.container.level, desired_level)
            fill_degree = max_level / ship.container.capacity
            yield from ship.check_depth_restriction(site, fill_degree, duration)

    def checkWeather(self, origin, destination, amount):
        if (
            isinstance(origin, HasWorkabilityCriteria)
            and isinstance(origin, Movable)
            and isinstance(destination, HasWeather)
        ):
            yield from origin.check_weather_restriction(destination, amount)
        elif (
            isinstance(destination, HasWorkabilityCriteria)
            and isinstance(destination, Movable)
            and isinstance(origin, HasWeather)
        ):
            yield from destination.check_weather_restriction(origin, amount)

    def addSpill(self, origin, destination, amount, duration):
        """
        duration: duration of the activity in seconds
        origin: origin of the moved volume (the computed amount)
        destination: destination of the moved volume (the computed amount)

        There are three options:
          1. Processor is also origin, destination could have spill requirements
          2. Processor is also destination, origin could have spill requirements
          3. Processor is neither destination, nor origin, but both could have spill requirements

        Result of this function is possible waiting, spill is added later on and does not depend on possible requirements
        """

        if isinstance(origin, HasSoil):
            density, fines = origin.get_properties(amount)

            # If self == origin --> destination is a placement location
            if self == origin:
                if isinstance(self, HasPlume) and isinstance(destination, HasSpill):
                    spill = destination.spillPlacement(self, self)

                    if 0 < spill and isinstance(destination, HasSpillCondition):
                        for condition in destination.SpillConditions["Spill limit"]:
                            condition.put(spill)

            # If self == destination --> origin is a retrieval location
            elif self == destination:
                if isinstance(self, HasPlume) and isinstance(origin, HasSpill):
                    spill = origin.spillDredging(
                        self, self, density, fines, amount, duration
                    )

                    if 0 < spill and isinstance(origin, HasSpillCondition):
                        for condition in origin.SpillConditions["Spill limit"]:
                            condition.put(spill)

            # If self != origin and self != destination --> processing
            else:
                if isinstance(self, HasPlume) and isinstance(destination, HasSpill):
                    spill = destination.spillPlacement(self, self)

                    if 0 < spill and isinstance(destination, HasSpillCondition):
                        for condition in destination.SpillConditions["Spill limit"]:
                            condition.put(spill)

                if isinstance(self, HasPlume) and isinstance(origin, HasSpill):
                    spill = origin.spillDredging(
                        self, self, density, fines, amount, duration
                    )

                    if 0 < spill and isinstance(origin, HasSpillCondition):
                        for condition in origin.SpillConditions["Spill limit"]:
                            condition.put(spill)

    def shiftSoil(self, origin, destination, amount):
        """
        origin: origin of the moved volume (the computed amount)
        destination: destination of the moved volume (the computed amount)
        amount: the volume of soil that is moved

        Can only occur if both the origin and the destination have soil objects (mix-ins)
        """

        if isinstance(origin, HasSoil) and isinstance(destination, HasSoil):
            soil = origin.get_soil(amount)
            destination.put_soil(soil)

        elif isinstance(origin, HasSoil):
            soil = origin.get_soil(amount)

        elif isinstance(destination, HasSoil):
            soil = SoilLayer(0, amount, "Unknown", 0, 0)
            destination.put_soil(soil)


class DictEncoder(json.JSONEncoder):
    """serialize a simpy openclsim object to json"""

    def default(self, o):
        result = {}
        for key, val in o.__dict__.items():
            if isinstance(val, simpy.Environment):
                continue
            if isinstance(val, EventsContainer) or isinstance(val, simpy.Container):
                result["capacity"] = val.capacity
                result["level"] = val.level
            elif isinstance(val, simpy.Resource):
                result["nr_resources"] = val.capacity
            else:
                result[key] = val

        return result


def serialize(obj):
    return json.dumps(obj, cls=DictEncoder)
