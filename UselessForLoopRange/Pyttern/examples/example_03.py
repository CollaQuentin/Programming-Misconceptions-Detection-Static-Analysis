def count(events,i,j):
    count = 0
    for a in range (len(events)) :
        if a == (i,j):
            count +=1
    return count
