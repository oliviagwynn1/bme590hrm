import numpy as np

voltage = [-14, 0, 9, 107, -8]
voltage_array = np.array(voltage)

def voltage_extremes(voltage_array):
    """Tuple containing minimum and maximum lead voltages"""
    voltage_min = min(voltage_array)
    voltage_max = max(voltage_array)
    voltage_extremes_val = (voltage_min, voltage_max)
    return voltage_extremes_val
print(voltage_extremes(voltage_array))