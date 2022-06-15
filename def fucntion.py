def hello(x):
    print ("hi how are you :",x)


times = int(input("how many names do you want to print?? :"))

list =[]

for i in range (times):
    name = input("enter the name :")
    list.append(name)

for x in list :
    hello(x)
    