from DoublyLinkedList import *

dlist = DoublyLinkedList()
x=1
p=0
print("-->")
while(x!=0):
   p=int(input("donde quieres agregar: 1.left 2.ringh: "))
   data=input("DIgite numero de una cifra: ")
   if p==1:
      for i in data:
         dlist.insertLeft(i)
      
   if p==2:
       for i in data:
         dlist.insertRingh(i)
   print(dlist)   
   x=int(input("desea agregar mas datos: "))  
dlist.peekLeft(1)  



# for data in [(1968),(1969),(1970)]:
#    dlist.insertLeft(data)
# for data in [(2015),(2016)]:
#    dlist.insertRingh(data)
# # print('After inserting', len(dlist), 
# #       'entries into the doubly linked list, it contains:\n', dlist, 
# #       'and empty =', dlist.isEmpty())
# dlist.deleteFirst()
# # print("-->",dlist.isEmpty())
# # print('Traversing backwards through the list:')
# print(dlist)


# print('Deleting first entry returns:', dlist.deleteFirst())
# print('Deleting last entry returns:', dlist.deleteLast())
# def year(x): return x[0]
# for date in [1967, 2015]:
#    print('Deleting entry with key', date, 'returns', 
#          dlist.delete(date, key=year))
# print('List after deletions contains:', dlist)

# for date in [1968, 2015]:
#    data = (date + 1, '?')
#    print('Inserting', data, 'after', date, 'returns',
#          dlist.insertAfter(date, data, key=year))
# print('List after insertions contains:', dlist)

# print('Traversing backwards through the list:')
# dlist.traverseBackwards()
