####euler 3
##for i in range(100):
##    if i%19==0 and i%20==0:
##        print i
##        

##def sumofsquares(n):
##    result=0
##    for i in range(n+1):
##        result+=i**2
##    return result
##
##def squareofsums(n):
##    result=0
##    for i in range(n+1):
##        result+=i
##    result=result**2
##    return result
##
####print sumofsquares(100)
####print squareofsums(100)-sumofsquares(100)
####        
##



##
##dic1={0:1,1:1,}
##print dic1[0]
##dic1[2]=2
##dic1[3]=3
##dic1[4]=5
##print dic1
###for i in range(8):
###    if i in dic1:
###        print dic1[i]
##
##def fibonacci(n):
##    if n==0 or n==1:
##        return 1
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##
##print fibonacci(23)
##
##def fib(n):
##    if n in dic1:
##        return dic1[n]
##    else:
##        dic1[n]=fib(n-1)+fib(n-2)
##    return dic1[n]
##
##print fib(23)
import math
dicprime={1:2,2:3,3:5,} #dictionary for the first few primes that we'll add to for subsequent ones

def prime(n):  ##function to call the nth prime number. see bottom for other version that worked
    if n in dicprime:
        return dicprime[n]
    else:
        z=dicprime[n-1]+2
        divisors=0
        result=1
        while result>0:
            for i in range(1,n):
                if z%dicprime[i]==0:
                    divisors+=1
                    break
                if dicprime[i]>math.sqrt(z):
                    break
            if divisors==0:
                result=0
            else:
                z+=2
                divisors=0
        dicprime[n]=z
        return dicprime[n]

n=20000

for i in range(1,n+1):
    prime(i)

#print dicprime[500]

def last_prime_less_than_x(x):
    numguesses=0
    n=int(x/math.log(x))
    while prime(n)<x:
        numguesses+=1
        n+=1
    print numguesses
    print n-1
    return prime(n-1)

#print last_prime_less_than_x(20000)


def prime_close_to_x(x):
    low=int(x/math.log(x))
    high=int(2*x/math.log(x))
    n=int((low+high)/2)
    numguesses=0
    while abs(x-prime(n))>int(5*math.log(x)):
        numguesses+=1
        if prime(n)>x:
            high=n
        else:
            low=n
        n=int((high+low)/2)
    print numguesses
    print n-1
    return prime(n-1)

#print prime(168)


print prime_close_to_x(200000)

#print dicprime

##list_of_primes=[]
##for i in range(1,17985):
##    list_of_primes+=[dicprime[i],]
##
###print list_of_primes
##
##print sum(list_of_primes)


##list1=[]
##
##a='600851475143'
##for i in range(len(a)):
##    list1+=([a[i]])
##
##b=600851475143
##
##for i in range(len(list1)):
##    list1[i]=int(list1[i])
##
##list1+=[5]
##
##print list1
##
##
##
##print sum(list1)
##
##list2=[]
##
##def findprimefactors(n):    #recursive function that finds the prime factors
##    for i in range(1,n):
##        if n%i==0:
##            c=i
##            print n/c
##            findprimefactors(c)
##        
##
##print findprimefactors(1024)


##for i in range(1,100000000,2):
##        if b%i==0:
##            c=i
##            print b/c
##            list2+=[i]





##for i in range(len(list1)):
##    print int(list1[i])
##
##for i in range(len(list1)):
##    print sum(int(list1[i]))



##def prime(n):  ##function to call the nth prime number. works as written up through 37
##    if n in dicprime:
##        return dicprime[n]
##    else:
##        z=prime(n-1)+2
##        #print z
##        divisors=0
##        result=1
##        while result>0:
##        
##            #print prime(i),'='+'prime i'
##            #print z%prime(i),'='+'current guess z modulo prime i'
##            for i in range(1,n):
##                if z%prime(i)==0:
##                    divisors+=1
##            if divisors==0:
##                result=0
##            else:
##                z+=2
##                divisors=0
##        return z
            










##            z+=1          ##should be able to insert testfunction here, but it doesn't work
##            divisors=0
##            for i in range(1,n):
##                if z%prime(i)==0:
##                    divisors+=1
##            if divisors==0:
##                return z
##            else:
##                z+=1
##                divisors=0
##                for i in range(1,n):
##                    if z%prime(i)==0:
##                        divisors+=1
##                if divisors==0:
##                    return z
##                else:
##                    z+=1
##                    divisors=0
##                    for i in range(1,n):
##                        if z%prime(i)==0:
##                            divisors+=1
##                    if divisors==0:
##                        return z
##                    else:
##                        z+=1
##                        divisors=0
##                        for i in range(1,n):
##                            if z%prime(i)==0:
##                                divisors+=1
##                        if divisors==0:
##                            return z
##                        else:
##                            z+=1
##                            divisors=0
##                            for i in range(1,n):
##                                if z%prime(i)==0:
##                                    divisors+=1
##                            if divisors==0:
##                                return z
##                            else:
##                                z+=1
##                                divisors=0
##                                for i in range(1,n):
##                                    if z%prime(i)==0:
##                                        divisors+=1
##                                if divisors==0:
##                                    return z
##                            
##    return z

##def testfunction(z,n):  ##recursive function to insert into prime function (see note below)
##    divisors=0
##    for i in range(1,n):
##        print prime(i)
##        if z%prime(i)==0:
##            divisors+=1
##            print divisors
##            
##        if divisors==0:
##            return z
##        else:
##            return testfunction(z+1,n)
##
##print testfunction(24,7)
            
#for i in range(12,14):
 #   print prime(i)





            
        



##def testfunction(n):
##    z=30
##    for i in range(2,n):
##        while z%i==0:
##            z+=1
##    return z
##

##    
##def prime(n):
##    if n==1:
##        return 2
##    else:
##        z=prime(n-1)+1
##        #print z
##        while i<n:
##            #print prime(i),'='+'prime i'
##            #print z%prime(i),'='+'current guess z modulo prime i'
##            if z%prime(i)!=0:
##                return z
##        
##            else:
##                z+=1
##                #print z,'='+'new guess for z'
##        return z
##        
##
##                
##    
##
##for i in range(1,14):
##    print prime(i)
####
####def testfunction(n):
####    z=20
####    for i in range(2,n):
####        if z%i!=0:
####            return z
####        else:
####            z+=1
####    
##
##
##z=range(100)
##print z
##print z[3]
##z.pop(3)
##print z
##
##def prime(n):
##    potentialprimes=range(2,n+1)
##    
            

##def prime(n):  ##function to call the nth prime number. 
##    if n in dicprime:
##        return dicprime[n]
##    else:
##        z=prime(n-1)+1
##        divisors=0
##        result=1
##        while result>0:
##            for i in range(1,n):
##                if z%prime(i)==0:
##                    divisors+=1
##            if divisors==0:
##                result=0
##            else:
##                z+=1
##                divisors=0
##        dicprime[n]=z
##        return dicprime[n]
##
##for i in range(1,20):
##    print prime(i)
