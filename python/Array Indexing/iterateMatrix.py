def iterMatrix():
    arr = [ [12,3,4],[34,56,7],[36,7,90] ]
    for row in arr:
        for item in row:
            print(item, end=' ')
        print()

iterMatrix()