def count(events, i, j):
    count = 0
    for i in range(len(events)):
        if (i,j)==events[0][i]:
            count += 1
    return count
