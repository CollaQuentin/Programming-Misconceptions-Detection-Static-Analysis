
def fibonacci(n):
    fa = 0
    fb = 1

    if n==1:
        return 1
    else:
        for times in range(n-1):
            fc = max(fa, fb)
            fa += fb
            fb = fc
            return( fa)
