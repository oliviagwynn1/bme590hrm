def validate(time_array, voltage_array):
    from length import length
    from negative import neg
    from exceed import exceed
    final = ""
    s1 = "Time and Voltage arrays have different lengths."
    s2 = "Time has negative values."
    s3 = "Voltage exceeds 300mV."


    try:
        length(time_array, voltage_array)
    except:
        final += s1
    try:
        neg(time_array)
    except:
        final += s2
    try:
        exceed(voltage_array)
    except:
        final += s3

    if final != "":
        raise TypeError(final)


if __name__ == "__main__":
    import numpy as np
    validate(time_array = np.array([0,-1,2,3,4,5]),
             voltage_array=np.array([-5,3,9,10,305,-3,2]))