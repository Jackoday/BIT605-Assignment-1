import time
import csv
import re

emailRegex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

class child:
  def __init__(self, lName, fName, DoB, gender, ethnicity, yearLvl):
    self.lName = lName
    self.fName = fName
    self.DoB = DoB
    self.gender = gender
    self.ethnicity = ethnicity
    self.yearLvl = yearLvl

class parent:
  def __init__(self, lName, fName, mblPhone, hmPhone, wrkPhone, email):
    self.lName = lName
    self.fName = fName
    self.mblPhone = mblPhone
    self.hmPhone = hmPhone
    self.wrkPhone = wrkPhone
    self.email = email #amended

  def emailCheck(self):
    if(re.search(emailRegex, self.email)):
      print(self.fName + " " + self.lName + " has a valid email")
    else:
      print(self.fName + " " + self.lName + " has an invalid email")

class address:
  def __init__(self, stNumber, street, suburb, city, postCode):
    self.stNumber = stNumber
    self.street = street
    self.suburb = suburb
    self.city = city
    self.postCode = postCode

#import unsorted list
list_unsorted = []
with open("BIT605_unsorted_data.csv") as csv_file:
  reader = csv.reader(csv_file, delimiter=",")
  for i in list(csv_file):
    list_unsorted.append(child((i.rsplit(',')[1]), (i.rsplit(',')[2]), "n/a", "n/a", "n/a", "n/a"))

#import sorted list (fixed as the list provided wasn't in alphabetical order)
list_sorted = []
with open("BIT605_sorted_data_byLastname.csv") as csv_file:
  reader = csv.reader(csv_file, delimiter=",")
  for i in list(csv_file):
    list_sorted.append(child((i.rsplit(',')[1]), (i.rsplit(',')[2]), "n/a", "n/a", "n/a", "n/a"))

#Linear search function
def search(array, first, last):   
  lfName = last + first; #combine last and first name for search 
  n = len(array)    
  for i in range (0, n):        
    if (array[i].lName + array[i].fName == lfName):          
      return i
  return -1

print ("--part 2a--")
starttime = time.time()
result = search(list_unsorted, "Ericka", "Jewess") 
print("Linear random-case",(time.time()-starttime)*1000)
print("Found at position",result)

starttime = time.time()
result = search(list_unsorted, "Harry", "Potter") 
print("Linear worst-case",(time.time()-starttime)*1000)
print("Found at position",result,"\n")

#Binary search function
def binary_search(array, first, last):
  lfName = last + first; #combine last and first name for search
  start  = 0
  end = len(array) - 1
 
  while start <= end:
    mid = start + (end - start) // 2 # middle of the list
    mid_value = array[mid].lName + array[mid].fName #get item to match with Last and first name
 
    if mid_value == lfName:
      return mid #we have matched the target Last
    elif mid_value < lfName:
      start = mid + 1 # left/lower side of the middle
    else:
      end = mid - 1 #right/upper side of the middle
  return -1 # Target not found

print ("--part 2b--")
starttime = time.time()
result = binary_search(list_sorted, "Ericka", "Jewess") 
print("Binary random-case",(time.time()-starttime)*1000)
print("Found at position",result)

starttime = time.time()
result = binary_search(list_sorted, "Harry", "Potter") 
print("Binary worst-case",(time.time()-starttime)*1000)
print("Found at position",result,"\n")

#Comparison tests
print ("--part 2c--")
starttime = time.time()
result = search(list_unsorted, "Terry", "Cormier") 
print("Linear search time for Terry Cormier",(time.time()-starttime)*1000)
print("Found at position",result)
starttime = time.time()
result = search(list_unsorted, "Jon", "Mann") 
print("Linear search time for Jon Mann",(time.time()-starttime)*1000)
print("Found at position",result)
starttime = time.time()
result = search(list_unsorted, "Earl", "Zulauf") 
print("Linear search time for Earl Zulauf",(time.time()-starttime)*1000)
print("Found at position",result,)

print("----")

starttime = time.time()
result = binary_search(list_sorted, "Terry", "Cormier") 
print("Binary search time for Terry Cormier",(time.time()-starttime)*1000)
print("Found at position",result)
starttime = time.time()
result = binary_search(list_sorted, "Jon", "Mann") 
print("Binary search time for Jon Mann",(time.time()-starttime)*1000)
print("Found at position",result)
starttime = time.time()
result = binary_search(list_sorted, "Earl", "Zulauf") 
print("Binary search time for Earl Zulauf",(time.time()-starttime)*1000)
print("Found at position",result)

#Create parent test list
parent_list = [
  parent("Digby", "Steve", "0273457723", "3845528", "0800734552", "steved@hotmail.com"),
  parent("McKay", "Liz", "0213778951", "3846225", "3477855", "mckaaaay@xtra.co.nz"),
  parent("Rodger", "Hannah", "0278966223", "n/a", "0800779595", "easy.peasy.com"),
  parent("Fay", "Rebecca", "0276884545", "9845560", "3376655", "Fay@xtra@xtra.com")
]

print("\n--part 3c--")
starttime = time.time()
for i in range (0, len(parent_list)):
  starttime = time.time()
  parent_list[i].emailCheck()
  print("Email check time = ",(time.time()-starttime)*1000)