def printNumbers(Lrange, Urange):
    if Lrange > Urange:
        return
    # print(Lrange)
    printNumbers(Lrange+1, Urange)
    print(Lrange)

printNumbers(1,5)