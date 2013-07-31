

import math
import itertools as it


def makeprimes(n):
  '''returns a list of prime numbers up to n'''
  list1=[]
  for i in range(n):
      list1+=[1,]


  i = 2
  while i <= math.sqrt(n):
    
    if list1[i] == 0:
      i += 1
      continue

    maxMultiple = int(math.ceil(float(n)/i))
    for j in range(2, maxMultiple):
      list1[i*j] = 0    ## all the multiples of the current i get set to zero 
    i += 1


  listprimes=[]
  for i in range(2,n):
      if list1[i]!=0:
          listprimes+=[i,]
  return listprimes


listprimes = makeprimes(10000000)
def prime(n):
  return listprimes[n-1]

def makelist(*strings):
  return [string for string in strings]

def make_perms_of_two(*strings):
  x = it.permutations(makelist(*strings),2)
  return [int(elem[0]+elem[1]) for elem in x] 

def check_list_for_all_primes(l):
  result = 0
  for item in l:
    if item in listprimes:
      result += 1
  return result == len(l)


def findpairsets(ceiling,toprint=False):
  listprimes = makeprimes(ceiling)
  i = 1
  while i < len(listprimes) - 10:
    j = i + 1
    a = str(listprimes[i])
    while j < len(listprimes) - 9:
      k = j + 1
      b = str(listprimes[j])
      if toprint:
        print 'trying ', a,b
      if not check_list_for_all_primes(make_perms_of_two(a,b)):
        j += 1
        if j == len(listprimes) - 9:
          i += 1
        continue
      while k < len(listprimes) - 8:
        m = k + 1
        c = str(listprimes[k])
        if toprint:
          print 'trying ', a,b,c
        if not check_list_for_all_primes(make_perms_of_two(a,b,c)):
          k += 1
          if k == len(listprimes) - 8:
            j += 1
          continue
        while m < len(listprimes) - 7:
          n = m + 1
          d = str(listprimes[m])
          if toprint:
            print 'trying ', a,b,c,d
          if not check_list_for_all_primes(make_perms_of_two(a,b,c,d)):
            m += 1
            if m == len(listprimes) - 7:
              k += 1
            continue
          while n < len(listprimes) - 6:
            e = str(listprimes[n])
            if toprint:
              print 'trying ', a,b,c,d,e
            if check_list_for_all_primes(make_perms_of_two(a,b,c,d,e)):
              return sum([int(a),int(b),int(c),int(d),int(e)])
            else:
              n += 1
              if n == len(listprimes) - 6:
                m += 1

            
if __name__ == '__main__':
  print findpairsets(10000, toprint=True)





