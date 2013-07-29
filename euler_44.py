import math
from pprint import pprint

def pentagonal(index):
    return index*(3*index - 1)/2.0

def is_pentagonal(n):
    x = int((1 + (1+4*3*(2*n))**0.5)/float(6))
    return x*(3*x-1)/2.0 == n

def difference(n,d):
    return abs(d*(3*n + 3*d**2/2.0 - d/2.0))

print difference(2000,1)
print difference(1021,2)

def makelist(row,columns):
    l = []
    for i in range(1,columns+1):
        l.append((row,i))
    return l

def makearray(rows,columns):
    l =[]
    for i in range(1,rows+1):
        l.append(makelist(i,columns))
    return l

# l = (makearray(10,10))
# print l[5][3]

def test(rows,columns):
    a = makearray(rows,columns)
    rows_covered = 0
    n = a[0][0][0]
    d = a[0][0][1]
    #print a[:3]
    print n
    print d
    numiterations = 0
    while True:
        
        #print 'trying n, d = ', (n,d)
        if is_pentagonal(pentagonal(n+d) - pentagonal(n)) and is_pentagonal(pentagonal(n+d)+pentagonal(n)):
            print pentagonal(n+d) - pentagonal(n)
            print n
            print d
            break
        else:
            numiterations += 1
            a[n-1].pop(0)
            d = {}
            for i in range(rows_covered+2):
                d[(i)] = difference(a[i][0][0],a[i][0][1])
            mins = [k for k,v in d.iteritems() if v == min(d.values())]
            #print 'dictionary of differences by row index ', d
            #print 'mins list ', mins
             
            k = mins[0]
            rows_covered = max(k,rows_covered)
            n = a[k][0][0]
            d = a[k][0][1]
            #for i in range(rows_covered):
             #   print a[i][0]
            #print 'new n = ', n
            #print 'new d = ', d
            #print numiterations

print test(2500,2500)





        







