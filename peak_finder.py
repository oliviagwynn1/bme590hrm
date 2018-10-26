def peak(threshold=0.7, voltage=None):
    import peakutils
    indexes = peakutils.indexes(voltage, thres=threshold, min_dist=30)
    return indexes




