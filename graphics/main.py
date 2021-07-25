import pandas as pd
import graphics as gf

#-------------------------------------------------------------------------------------------
# @author Booh-rm
#-------------------------------------------------------------------------------------------

inhabitants = pd.read_csv('data/inhabitants.csv')

while True:
	print('\n')
	print(
	    '\033[1m' +"Enter the desired option:"+ '\033[0m'"\n \n1. Graph of number of women and men present in the city. \n \n2. Graph of number of people assigned by type of employment. \n \n3. Graph of number of people who have already been vaccinated. \n \n4. Graph of number of children and number of adults (In the city, adulthood starts at age 25).\n \n5. Graph of the number of people living on the right side of the street and on the left side of the street (remember that the direction ends in -R or -L). \n \n6. Graph of the number of men and women with the job \"Software Developer\".\n \n7. Graph of the number of women assigned to each job. \n \n8. Relevant data (Average age, oldest and youngest person, number of people between 25 and 45 with the job\"Systems Engineer\")\n \n9. Exit. \n"
	)
	opcion = input("Enter the desired option: ")
	if opcion == "1":
		gf.plot_number_of_men_women(inhabitants)
	elif opcion == "2":
		
		gf.plot_number_of_persons_by_employment(inhabitants)
	elif opcion == "3":

		gf.plot_amount_of_people_vaccinated(inhabitants)
	elif opcion == "4":

		gf.plot_number_of_adult_children(inhabitants)
	elif opcion == "5":

		gf.plot_number_of_people_by_street_side(inhabitants)
	elif opcion == "6":

		gf.plot_number_of_women_software_developers(inhabitants)
	elif opcion == "7":

		gf.plot_amount_of_women_by_employment(inhabitants)
	elif opcion == "8":

		gf.show_statistics(inhabitants)
	elif opcion == "9":

		print('\n',
		     '\033[1m' +"Thank you for viewing our city's statistics, come back soon!"+ '\033[0m', '\n'
		)
		break