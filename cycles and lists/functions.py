import random

JACs_quantity = 20
addresses_quantity = 2000
addresses=["-L","-R"]

#========================================================================================
#========================================================================================

def obtain_list_JACs():
 
  list_JACs = []
  list_JACs=[random.randrange(addresses_quantity)+1] #The first number is never repeated.
  n = 1
  while n<JACs_quantity:  
    num = random.randrange(addresses_quantity)+1  
    not_repeated = True #It is initially assumed that the generated number is not repeated.
    while not_repeated:  
      for j in range(len(list_JACs)):  
        if num == list_JACs[j]:  
         not_repeated = False #Detects if the number is repeated.
      if not_repeated:
        list_JACs.append(num) #If the number is not repeated, it is added to the list.
        n += 1 
  list_JACs.sort() #Order the items in the list from lowest to highest.

  return list_JACs

#========================================================================================
#========================================================================================

def obtain_list_addresses( list_JACs ):

  addresses_list = []
  n = 0
  while n <= addresses_quantity:
    if n not in list_JACs:
      addresses_list.append(str(n) +random.choice(addresses))#The numbers in the address list are randomly appended with '-L' or '-R'.
    n += 1
  
  return addresses_list

#========================================================================================
#========================================================================================

def assign_jobs(addresses, JACs):

  assignments = obtain_listing_by_JAC( len(JACs) )

  for address in addresses:
    n = 0
    num_address = obtain_address_number(address)
    minor = addresses_quantity+1
    minor_index = 0
    while n < len(JACs):

      distance = (abs(num_address-JACs[n])) #Calculates the distance between a JAC and an address.
      if distance < minor:
        minor = distance 
        minor_index = n
      n += 1
    assignments[minor_index].append(address)
    
  return assignments

#========================================================================================
#========================================================================================

def obtain_listing_by_JAC(size):

  return [[] for i in range( size )]

#========================================================================================
#========================================================================================

def obtain_address_number(full_address):

  address_number = int(full_address.split("-")[0]) #Convert to integer and remove '-L' or '-R' from the address list.
  return address_number

#========================================================================================
#========================================================================================

def appointment_assignment(JACs_addresses):

  appointments = []
  quantity = len(JACs_addresses)
  n = 0
  day = 1 #Appointment assignment begins on day 1.
  hour = 0
  minute = 0
  while n < quantity:
    format = str(day)+"-"+str(hour)+":"+str(minute)
    appointments.append(format)
    if hour == 4 and minute == 40: #If the 5-hour limit is reached in one day, the next day will be used for appointment assignment.
      minute = 0
      hour = 0
      day += 1
    elif minute == 40:
      minute = 0
      hour += 1
    else:
      minute += 20 #Assignments are made every 20 minutes.
    n += 1
  return appointments

#========================================================================================
#========================================================================================