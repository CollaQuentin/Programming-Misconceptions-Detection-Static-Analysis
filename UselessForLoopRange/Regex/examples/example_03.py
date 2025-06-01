def count(events, i, j):
    count = 0
    for t in range(len(events)):
        if (i,j) == events[t]:
            count += 1
    return count
