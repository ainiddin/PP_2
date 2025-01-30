#Check if "apple" is present in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Insert "watermelon" as the third item,GIve position and item that u want to insert 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove the first occurrence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Set the values in the new list to upper case
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#Sort the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#there are three types of copying list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist = list(thislist)
mylist = thislist[:]
print(mylist)

#join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
