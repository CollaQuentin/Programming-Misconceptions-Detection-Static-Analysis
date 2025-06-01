def count(events, i, j):
    count = 0
    for k in range(len(events)):
        if i == j:
            if events[k][0] == i and events[k][1] == i:
                count+=1
        else:
            if events[k][0] == i and events[k][1] == j:
                count+=1
    return count
