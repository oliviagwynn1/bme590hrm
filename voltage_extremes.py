def voltage_extremes(voltage_array):
    """Tuple containing minimum and maximum lead voltages"""
    voltage_min = min(voltage_array)
    voltage_max = max(voltage_array)
    voltage_extremes_val = (voltage_min, voltage_max)
    return voltage_extremes_val
