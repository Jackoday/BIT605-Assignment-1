import datetime
import time
import csv

class child:
  def __init__(self, lName, fName, email):
    self.lName = lName
    self.fName = fName
    #self.DoB = datetime.date.DoB
    self.email = email


#import unsorted list
list_unsorted = []
with open("BIT605_unsorted_data.csv") as csv_file:
  reader = csv.reader(csv_file, delimiter=",")
  for i in list(csv_file):
    list_unsorted.append(child((i.rsplit(',')[1]), (i.rsplit(',')[2]), (i.rsplit(',')[3])))

#import sorted list
list_sorted = []
with open("BIT605_sorted_data__byLastname_.csv") as csv_file:
  reader = csv.reader(csv_file, delimiter=",")
  for i in list(csv_file):
    list_sorted.append(child((i.rsplit(',')[1]), (i.rsplit(',')[2]), (i.rsplit(',')[3])))

#Linear search function
def search(array, last, first):    
  n = len(array)    
  for i in range (0, n):        
    if (array[i].lName == last):
      if (array[i].fName == first):            
        return i
  return -1

starttime = time.time()
result = search(list_unsorted, "Jewess", "Ericka") 
print("Linear random-case",(time.time()-starttime)*1000)
print("Found at position",result)

starttime = time.time()
result = search(list_unsorted, "Potter", "Harry") 
print("Linear worst-case",(time.time()-starttime)*1000)
print("Found at position",result)

#Binary search function
def binary_search(array, last, first):
  start  = 0
  end = len(array) - 1
 
  while start <= end:
    mid = start + (end - start) // 2 # middle of the list
    mid_value = array[mid].lName #get item to match with Last
    print("Middle,value", mid,mid_value)
 
    if mid_value == last:
      return mid #we have matched the target Last
    elif mid_value < last:
      start = mid + 1 # left/lower side of the middle
    else:
      end = mid - 1 #right/upper side of the middle
  return -1 # Target not found

starttime = time.time()
result = binary_search(list_sorted, "Jewess", "Ericka") 
print("Binary random-case",(time.time()-starttime)*1000)
print("Found at position",result)

starttime = time.time()
result = binary_search(list_sorted, "Potter", "Harry") 
print("Binary worst-case",(time.time()-starttime)*1000)
print("Found at position",result)
#keep in mind if it finds last name but not first...