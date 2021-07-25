import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_number_of_men_women(inhabitants):

  inhabitants_by_sex = inhabitants.groupby(['sex']).size()

  #-------------------------------------------------------------------------------------------

  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  print('The number of inhabitants distributed by sex is: ','\n', inhabitants_by_sex,'\n')
  plt.bar(['Women','Men'], inhabitants_by_sex, label = 'Number of inhabitants by sex')
  plt.show()

  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')



def plot_number_of_persons_by_employment(inhabitants):

  inhabitants_by_employment = inhabitants.groupby(['employment']).size()

  #-------------------------------------------------------------------------------------------

  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  print('The number of inhabitants distributed by employment is: ','\n', inhabitants_by_employment,'\n')
  plt.bar(['1','2','3','4','5','6','7','8', '9','10','11','12','13','14','15','16','17','18','19'], inhabitants_by_employment, label = 'Inhabitants by employment')
  plt.show()

  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')



def plot_amount_of_people_vaccinated(inhabitants):

  vaccinated_inhabitants = inhabitants.groupby(['vaccinated']).size()

  #-------------------------------------------------------------------------------------------

  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  print('The number of vaccinated and unvaccinated inhabitants is as follows: ','\n', vaccinated_inhabitants,'\n')
  plt.bar(['Inhab. unvaccinated','Inhab. vaccinated'], vaccinated_inhabitants, label = 'Immunization')
  plt.show()

  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')



def plot_number_of_adult_children(inhabitants):

  inhab = inhabitants

  children = inhab[ (inhab['age'] <= 24)].index.tolist()
  person_condition = inhab.iloc[children,[1,2,5]] #Search and print the inhabitants that meet the given condition.
  series = pd.Series(children) #Converts to a 'series' the number of people who meet the condition. 
  inhab_condition = series.size #Calculate the total number of inhabitants that meet the condition.

  #---------------------------------------------------------------------------------------

  adult = inhab[ (inhab['age'] >= 25)].index.tolist()
  adult_condition = inhab.iloc[adult,[1,2,5]] #Search and print the inhabitants that meet the given condition.
  series_a = pd.Series(adult) #Converts to a 'series' the number of people who meet the condition. 
  adult_cond = series_a.size #Calculate the total number of inhabitants that meet the condition.


  #-------------------------------------------------------------------------------------------


  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')


  print('The number of children is:',inhab_condition)
  print('\n')

  y_pos =np.arange(len(children))
  plt.bar(('Number of childrens'),y_pos )
  plt.show()

  print('==========================================================================','\n')

  print('The number of adults is:',adult_cond)
  
  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  y_pos_2 =np.arange(len(adult))
  plt.bar(('Number of adults'),y_pos_2 )
  plt.show()



def plot_number_of_people_by_street_side(inhabitants):

  address_in_L_and_in_R = []
  left = 0
  Right = 0
  for i in inhabitants['address']: #Cycle to find the number of addresses on each side of the street.
    if 'L' in i:
      left += 1
    elif 'R' in i:
      Right += 1

  address_in_L_and_in_R.append(left) #The number of addresses on the left side of the street is stored.
  address_in_L_and_in_R.append(Right)#The number of addresses on the right side of the street is stored.


  #-------------------------------------------------------------------------------------------


  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')
  print('Inhabitants living on the left side of the street are:',left,'\n')
  print('Inhabitants living on the right side of the street are:',Right)
  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  plt.bar(['Left side','Right side'],address_in_L_and_in_R, label='L R')
  plt.show()



def plot_number_of_women_software_developers(inhabitants):

  inhab = inhabitants

  women = inhab[ (inhab['sex'] == 'F') & (inhab['employment']=='Software Developer')].index.tolist()
  women_condition = inhab.iloc[women,[1,2,3,7]] #Search and print the inhabitants that meet the given condition.
  series = pd.Series(women) #Converts to a 'series' the number of people who meet the condition. 
  inhab_F_cond = series.size #Calculate the total number of inhabitants that meet the condition.

  #---------------------------------------------------------------------------------------

  men = inhab[ (inhab['sex'] == 'M') & (inhab['employment'] == 'Software Developer')].index.tolist()
  men_condition = inhab.iloc[men,[1,2,3,7]] #Search and print the inhabitants that meet the given condition.
  series_a = pd.Series(men) #Converts to a 'series' the number of people who meet the condition. 
  inhab_M_cond = series_a.size #Calculate the total number of inhabitants that meet the condition.



  #-------------------------------------------------------------------------------------------


  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  print('The number of women who are software developers is:',inhab_F_cond)
  print('\n')

  y_pos =np.arange(len(women))
  plt.bar(('Number of Women Software Developers'),y_pos )
  plt.show()

  print('==========================================================================','\n')

  print('The number of men who are software developers is:',inhab_M_cond)
  
  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  y_pos_2 =np.arange(len(men))
  plt.bar(('Number of men Software Developers'),y_pos_2 )
  plt.show()



def plot_amount_of_women_by_employment(inhabitants):

  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')

  women_for_employment = inhabitants.groupby([(inhabitants['sex']=='F'), 'employment']).size()
  print(women_for_employment)

  women_employment = inhabitants[(inhabitants['sex']=='F') & ( inhabitants['employment'] )]
  print('\n')
  print('',women_employment)


  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')



def show_statistics(inhabitants):

  inhab = inhabitants

  average_age = inhab['age'].median()

  maximum_age = inhab['age'].max()
  max_age = int(maximum_age)
  inhab_max = inhab[inhab['age']==max_age].index.tolist() #Searches the database for indexes where the maximum age appears and stores them in a list.
  person_max = inhab.iloc[inhab_max,[0,1,2,3,5]]


  minimum_age = inhab['age'].min()
  min_age = int(minimum_age)
  inhab_min = inhab[inhab['age']==min_age].index.tolist()
  person_min = inhab.iloc[inhab_min,[0,1,2,3,5]]


  systems_engineer = inhab[ (inhab['age'] >= 25) & (inhab['age'] <= 45) & (inhab['employment']=='Systems Engineer') ].index.tolist() #It extracts the index of the inhabitants that meet the condition and stores them in a list.
  
  person_cond = inhab.iloc[systems_engineer,[0,1,2,5,7]] #Search and print the inhabitants that meet the given condition.

  series = pd.Series(systems_engineer)
  inhab_cond = series.size #Calculate the total number of inhabitants that meet the condition.

  
  #-------------------------------------------------------------------------------------------


  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------')
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')
  
  print('The average age of the inhabitants of the city is:',average_age,'years old')
  print('\n')

  print('\033[;32m' + ""         )
  print('==========================================================================','\n')
  print("\n"+ '\033[0;m         ')
  
  print('The minimum age of the inhabitants is:',minimum_age,'years old','\n')
  print('The city\'s youngest inhabitants are:','\n')
  print(person_min)
  print('\n')

  print('\033[;32m' + ""         )
  print('==========================================================================','\n')
  print("\n"+ '\033[0;m         ')

  print('The maximum age of the inhabitants is:',maximum_age,'years old','\n')
  print('The oldest inhabitants of the city are:','\n')
  print(person_max)
  print('\n')

  print('\033[;32m' + ""         )
  print('==========================================================================','\n')
  print("\n"+ '\033[0;m         ')

  print('The number of inhabitants who are between 25 and 45 years old and as a job have "Systems Engineer" assigned to them are:',inhab_cond,'inhabitants','\n')
  print('The inhabitants that meet the condition are:','\n')
  print(person_cond)
  
  print('\n')
  print('\033[;32m' + ""         )
  print('-------------------------------------------------------------------------------')
  print('-------------------------------------------------------------------------------','\n')
  print("\n"+ '\033[0;m         ')