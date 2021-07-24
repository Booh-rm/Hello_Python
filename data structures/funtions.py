import datetime

MINIMUM_IDENTIFICATION  = 15000000 
MAXIMUM_IDENTIFICATION = 15000200


def obtain_list_identifications() -> list:
	return [i for i in range(MINIMUM_IDENTIFICATION , (MAXIMUM_IDENTIFICATION + 1))]


def obtain_shift(list_identifications, applicant_ID, inhabitants_in_queue,
                  processed_inhabitants):

	shift_number = 0

	if applicant_ID in list_identifications:

		if applicant_ID in processed_inhabitants.keys():  #The dictionary of already processed inhabitants is searched for the ID entered by the user.
			print(
			    'It was not possible to validate that your identification complied with the requirements.'
			)
		else:
			shift_number += 1

	else:
		print(
		    'It was not possible to validate that your identification complied with the requirements.'
		)

	if applicant_ID in processed_inhabitants.keys(
	):  #Conditional to determine whether the inhabitant has already been prosecuted.
		return 2

	if applicant_ID in inhabitants_in_queue:  #Conditional to determine if the inhabitant is already in the queue.
		print('Identification is already in the queue of inhabitants.')
		print('It was not possible to validate that your identification complied with the requirements.')
		return 3

	return shift_number


def obtain_assignment_data(ID):
	""" 
  This function calls the respective inhabitant according to his position in the queue and records the following data: ID, Name, Age, Assigned job.
  """
	assignment_data = {}
	id = input('Enter your ID: ')
	name = input('Enter your name: ')
	age = input('Enter your age: ')
	employment = input('Enter your employment:')

	date_and_time = datetime.datetime.now()

	d_t = date_and_time.strftime(
	    'Fecha: %d-%m-%y Hora: %H:%M')

	assignment_data[ID] = str( id ), name, age, employment, d_t  #The data entered by the user is assigned to the dictionary 'assignment_data'.

	return assignment_data


def to_print(obtain_assignment_data):

	for id in obtain_assignment_data:
		print('\n', 'User data entered -->', id, ':', obtain_assignment_data[id])


def show_report_assignment(inhabitants_processed):

	total_assigned = len(inhabitants_processed)

	print('Total inhabitants assigned:', total_assigned)