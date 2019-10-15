a = [1,2,3,4,4]


def duplicates(a):
   b = []
   for i in a:
       if i not in b:
           b.append(i)
   return b

print(duplicates(a))
#or set(a)
#set is a constructor that's defined in python