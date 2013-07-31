

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

    max_multiple = int(math.ceil(float(n)/i))
    for j in range(2, max_multiple):
      list1[i*j] = 0    ## all the multiples of the current i get set to zero 
    i += 1


  listprimes=[]
  for i in range(2,n):
      if list1[i]!=0:
          listprimes+=[i,]
  return listprimes

def makeprimedict_reversed(listprimes):
  d = {}
  for i in range(len(listprimes)):
    d[listprimes[i]] = i
  return d



def makeprimedict(listprimes):
  d = {}
  for i in range(len(listprimes)):
    d[i] = listprimes[i]
  return d

listprimes = makeprimes(20000000)

def prime(n):
  return listprimes[n-1]

def makelist(*strings):
  return [string for string in strings]

def make_perms_of_two(*strings):
  x = it.permutations(makelist(*strings),2)
  return [int(elem[0]+elem[1]) for elem in x] 

def check_list_for_all_primes(l,d):
  result = 0
  for item in l:
    if d.get(item):
      result += 1
      
  return result == len(l)


      

def find_with_for_loops(ceiling,toprint=False):
  i = 1
  reverse_dict = makeprimedict_reversed(listprimes)
  primedict = makeprimedict(listprimes)
  t = 0
  newprimelist = listprimes[:ceiling]

  

  for prime1 in newprimelist[1:]:
    for prime2 in newprimelist[listprimes.index(prime1):]:
      if toprint:
        print 'trying ', prime1, prime2
      if check_list_for_all_primes(make_perms_of_two(str(prime1),str(prime2)),reverse_dict):
        for prime3 in newprimelist[listprimes.index(prime2):]:
          if toprint:
            print 'trying ', prime1, prime2,prime3
          if check_list_for_all_primes(make_perms_of_two(str(prime1),str(prime2),str(prime3)),reverse_dict):
            for prime4 in newprimelist[listprimes.index(prime3):]:
              if toprint:
                print 'trying ', prime1, prime2,prime3,prime4
              if check_list_for_all_primes(make_perms_of_two(str(prime1),str(prime2),str(prime3),str(prime4)),reverse_dict):
                for prime5 in newprimelist[listprimes.index(prime4):]:
                  if toprint:
                    print 'trying ', prime1, prime2,prime3,prime4,prime5
                  if check_list_for_all_primes(make_perms_of_two(str(prime1),str(prime2),str(prime3),str(prime4),str(prime5)),reverse_dict):
                    return sum([prime1,prime2,prime3,prime4,prime5])



if __name__ == '__main__':
  print find_with_for_loops(300,toprint=True)
  # d1 = makeprimedict(listprimes)
  # d2 = makeprimedict_reversed(listprimes)
  # print d1[11]
  # print d2[37]
  
  





