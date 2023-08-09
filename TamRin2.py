

dicta = {}

def dicta_saz(lst):
   
    for i in lst:
        keys = dicta.keys()
        if i in keys:
            dicta[i] +=1
        else:
            dicta[i]= 1
    return dicta

#---------
lst = ['a','a','a','a','a','a',2,3,4,9,3,3]
result = dicta_saz(lst)
values =(result.values())
max_value = max(values)
print(max_value, end = '')
#----------
print(":",end='')
keys = list(dicta.keys())
#----------
for key,value in result.items():
    if value==max_value :
        print(key,end= ' ')


     