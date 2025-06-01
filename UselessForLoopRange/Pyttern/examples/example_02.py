def count(events, i, j):
    sum=0
    for b in range (len(events)):
            if events[b][0]==i and events[b][1]==j:
                sum+=1
    return sum
