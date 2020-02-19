def slices(series, length):
    if len(series) == 0 or length > len(series) or length < 1:
        raise ValueError(".+")

    slices = []
    for i in range(len(series) - length + 1):
        slices.append(series[i: i+length])

    return slices
