"""Inverter sensor"""
import logging

from custom_components.foxess_modbus.const import AC1
from custom_components.foxess_modbus.const import AIOH1
from custom_components.foxess_modbus.const import H1
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass

from .modbus_sensor import ModbusSensor
from .modbus_sensor import SensorDescription

_LOGGER: logging.Logger = logging.getLogger(__package__)

H1_SENSORS: list[SensorDescription] = [
    SensorDescription(
        key="pv1_voltage",
        address=31000,
        name="PV1 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    SensorDescription(
        key="pv1_current",
        address=31001,
        name="PV1 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    SensorDescription(
        key="pv1_power",
        address=31002,
        name="PV1 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    SensorDescription(
        key="pv2_voltage",
        address=31003,
        name="PV2 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    SensorDescription(
        key="pv2_current",
        address=31004,
        name="PV2 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    SensorDescription(
        key="pv2_power",
        address=31005,
        name="PV2 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
]

H1_AC1_SENSORS: list[SensorDescription] = [
    SensorDescription(
        key="battery_soc",
        address=31024,
        name="Battery SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    SensorDescription(
        key="battery_discharge",
        address=31022,
        name="Battery Discharge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
    ),
    SensorDescription(
        key="battery_charge",
        address=31022,
        name="Battery Charge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
    ),
    SensorDescription(
        key="feed_in",
        address=31014,
        name="Feed In",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
    ),
    SensorDescription(
        key="grid_consumption",
        address=31014,
        name="Grid Consumption",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
    ),
    SensorDescription(
        key="rvolt",
        address=31006,
        name="Grid Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    SensorDescription(
        key="rcurrent",
        address=31007,
        name="Grid Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    SensorDescription(
        key="rfreq",
        address=31009,
        name="Grid Frequency",
        device_class=SensorDeviceClass.FREQUENCY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="Hz",
        scale=0.01,
    ),
    SensorDescription(
        key="battery_temp",
        address=31023,
        name="Battery Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    SensorDescription(
        key="invtemp",
        address=31019,
        name="Inverter Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    SensorDescription(
        key="ambtemp",
        address=31018,
        name="Ambient Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    SensorDescription(
        key="load_power",
        address=31016,
        name="Load Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    SensorDescription(
        key="grid_ct",
        address=31014,
        name="Grid CT",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    SensorDescription(
        key="batvolt",
        address=31020,
        name="Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    SensorDescription(
        key="bat_current",
        address=31021,
        name="Battery Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
]

COMPAT: dict[str, list] = {
    H1: H1_SENSORS + H1_AC1_SENSORS,
    AIOH1: H1_SENSORS + H1_AC1_SENSORS,
    AC1: H1_AC1_SENSORS,
}


def sensors(base_model, controller, entry, inverter) -> list:
    """Return compatible sensors"""
    return list(
        ModbusSensor(controller, sensor, entry, inverter)
        for sensor in COMPAT[base_model]
    )