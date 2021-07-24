from funtions import *

#-------------------------------------------------------------------------------------------
# @author Booh-rm
#-------------------------------------------------------------------------------------------

identification_list = obtain_list_identifications()
print("authorized identifications:", identification_list)

print('\n')
print('=============================================================================================')
print('\n')


people_in_queue = []

inhabitants_processed = {}

while True:
  option = input("Enter an option:\n1. Request an appointment\n2. Attend a person from the queue\n3. Show final assignment report\n4. Exit\n")
  
  if option == "1":

    ID = int(input("Enter the person's ID number: "))
    assigned_shift = obtain_shift(identification_list, ID, people_in_queue, inhabitants_processed)
    if assigned_shift>= 0:

      if ID in identification_list and assigned_shift != 2 and assigned_shift != 3:
        people_in_queue.append( ID )
        print( ID, "was added to the queue." )
      elif assigned_shift == 2:
        break
      elif assigned_shift == 3:
        break
      elif assigned_shift not in identification_list:
        break
    else:

      print("It was not possible to validate that your identification complied with the requirements.")
  
  elif option == "2":

    if len(people_in_queue) > 0: #isEmpty
      person_identification_attended = people_in_queue.pop( 0 )
      print("Serving the inhabitant with ID:", person_identification_attended)
      
      obtain_data = obtain_assignment_data(person_identification_attended)
      inhabitants_processed[person_identification_attended]=obtain_data
      
      to_print(obtain_data)
    else:
      print("The queue is empty, there are no people to serve.")
  elif option == "3":

    show_report_assignment(inhabitants_processed)
  elif option == "4":
    break
  print('\n',"-------------------")
print("-------------------------","\n","You have left the program","\n","----------------------","\n")
