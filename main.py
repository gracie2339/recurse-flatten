def flatten(l):
   result = []
   for el in l:
     if isinstance(el, list):
       flat = flatten(el)
       result += flat
     else:
       result.append(el)
   return result


my_list = ['hi', 'grace', ['my', 'name'], [['is']], 'Optimus', ['Prime']]
print(flatten(my_list))