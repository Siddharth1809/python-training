list1 = [9,7,5,8,3,6,2,3,1,4]
list2 = ['a','b','c','d']

#append list2 in list1
def list_append(list1,list2):
    print("List1 is:",list1)
    print("List2 is:", list2)
    list1.append(list2)
    print("after appending list2 in list1",list1)


#clear all elements from the list1
def list_clear(list1):
    print("List1 is:",list1)
    list1.clear()
    print("After performing clear operation:",list1)

#copies elements of list1 in in list2
def list_copy(list1):
    list2 = list1.copy()
    print("Orginial list is:",list1)
    print("Copied list is:",list2)

#count element repeat number of times in given list
def list_count(list1,n):
    print("List is:",list1)
    print("An digit want to count:",n)
    print("Total number of occurrence of",n,"in",list1,"is:",list1.count(9))

#add elements in list
def list_extend(list1,list2):
    print("List1 is:",list1)
    print("List2 you want to extend is:",list2)
    list1.extend(list2)
    print("Extended list is:",list1)

#insert elements at given index value
def list_insert(list1,n,a):
    print("original list is:",list1)
    print("Value",a," will be added at",n,"index")
    list1.insert(n,a)
    print("Final list is:",list1)


#gives index of an element between start and stop range
def list_index(list1,n):
    print("List1 1 is:",list1)
    print("Finding index of value",n)
    print("index value of",n,"in",list1,"is:",list1.index(n))


#pop an element
def list_pop(list1,n):
    print("Original list is:",list1)
    print("index is:",n)
    list1.pop(n)
    print("Modified list is:",list1)

#removes a given element
def list_remove(list1, n):
    print("Original list is:", list1)
    print("value you want to remove is:", n)
    list1.remove(n)
    print("Modified list is:", list1)

#return list in reverse order
def list_reverse(list1):
    print("actual list is:",list1)
    list1.reverse()
    print("reversed list is:",list1)

#sort list in ascending and descending order
def list_sort(list1):
    print("actual list is:", list1)
    list1.sort()
    print("sorted list in ascending order is:",list1)
    list1.sort(reverse=True)
    print("sorted list in descending order is:",list1)



#sorting a list
def list_sort_1(list1):
    print("Original list is:",list1)
    list1.sort(key=str)
    print(list1)
    list2=[]
    for i in list1:
        if type(i) == str:
            break
        else:
            list2.append(i)
            for i in range(len(list2)-1,0,-1):
                for j in range(i):
                    if list2[j]>list2[j+1]:
                        temp = list2[j]
                        list2[j] = list2[j+1]
                        list2[j+1] = temp
    #list2.sort(key=abs)
    print("After sorting:",list2)


#separate unique items in list
def list_unique(list1):
    #list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print("Before sorting:",list1)
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    print("After sorting:",result)


#separate unique and repetitive items in list
def list_unique_repeat(list1):
    #list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print("Original list is:",list1)
    unique = []
    repeat = []
    for i in list1:
        if i not in unique:
            unique.append(i)
        else:
            repeat.append(i)
    print("List of unique values:",unique)
    print("List of repititve values:",repeat)
    final= []
    for j in repeat:
        for k in j:
            final.append(k)
    print("Afrter converting",repeat,"in single list:",final)



#
#list1 = [{},{},{}]
