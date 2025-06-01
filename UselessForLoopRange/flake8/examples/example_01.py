def count(events,i,j):
    count = 0
    for n in range (len(events)):
        if events[n] == (i,j):
            count += 1

    return (count)
