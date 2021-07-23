import functions as f

#-------------------------------------------------------------------------------------------
# @author Booh-rm
#-------------------------------------------------------------------------------------------

list_JACs = f.obtain_list_JACs()
list_addresses = f.obtain_list_addresses( list_JACs )

print("List of JACs:", list_JACs)

print("\n","List of addresses:", list_addresses)

print("\n",'-------------------------------------')

assignments_JACs = f.assign_jobs(list_addresses, list_JACs)

print("List of assignments:", assignments_JACs)
print("\n",'-------------------------------------')

for assignment_JAC in assignments_JACs:
  schedules_JACs = f.appointment_assignment(assignment_JAC)
  print(schedules_JACs)
  print('-------------------------------------')