# import os

# def listdirectory():
#     for i in os.listdir():
#         print(i)

# listdirectory();

#=================================================================================
#Dictionary practice

dictionary1 = {'a':1, 'b': 10, 'c': 9}
dictionary1['a'] = 2
#print(dictionary1.get['a'])
# for i in dictionary1.keys():
#     print(i)
# for i in dictionary1.values():
#     print(i)
#print(dictionary1['a'])
# for i in dictionary1:
#     if dictionary1[i] == 4:
#         print(i)
list1 = ['a', 'a', 'a', 'c']
for i in list1:
    if dictionary1.get(i):
        dictionary1[i] += 1
dictionary1.pop('a')
dictionary1.update({'d': 100})
dictionary2 = {'b':3, 'e':1, 'f': 4, 'g': 9}
for i in dictionary2:
    if dictionary1.get(i):
        #print("exist")
        dictionary1.update({i:(dictionary1[i] + dictionary2[i])})
    else:
        #print(i)
        dictionary1.update({i:dictionary2[i]})
#dictionary1.update(dictionary2)

for i in dictionary1:
    print(i + " : " + str(dictionary1[i]))
