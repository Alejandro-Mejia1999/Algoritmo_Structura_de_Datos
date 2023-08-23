from Queue import *
x=100
A= Queue(x)
B= Queue(x)
C=Queue(x)
D=Queue(x)
queue=Queue(x)
cadena="aabbcddaaABbCDccd"


for person in ['a','a','b','c','A','d','B','a','b']:
   queue.insert(person)
   if(person=='a'):
      A.insert(person)
   if(person=='A'):
      print("el cliente A",person.__len__()," termino el pago")
      A.remove()
   if(person=='b'):
      B.insert(person)
   if(person=='B'):
      print("el cliente B",person.__len__()," termino el pago")
      B.remove()
   if(person=='c'):
      C.insert(person)
   if(person=='C'):
      print("el cliente C",person.__len__()," termino el pago")
      C.remove()
   if(person=='d'):
      D.insert(person)
   if(person=='D'):
      print("el cliente D",person.__len__()," termino el pago")
      D.remove()
   
print('After inserting', len(queue), 
      'persons on the queue, it contains:\n', queue)
print('Is queue full?', queue.isFull())

print('\n-->',len(A),A)
print('-->',len(B),B)
print('-->',len(C),C)
print('-->',len(D),D)



