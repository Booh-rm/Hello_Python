"""Module for functions related to the evacuation stage.
"""

#-----------------------------------------------------------------------#
import persons as p

#======================================================================

#-----------------------------------------------------------------------#
#Function to determine whether or not a user has programming experience:
def is_prgmr(is_programmer):
  if is_programmer.capitalize() == 'No':
    return False
  return True
    
#======================================================================

#-----------------------------------------------------------------------#
#Function to determine to which stage of evacuation a person with 
#programming experience belongs:
def obtain_stage(is_programmer, programming_language, age):
  if programming_language.capitalize() != 'Python':

    #-----------------------------------------------------------------------#
    #If the programming language the user knows is different from Python 
    #then it is assigned to evacuation stage 2:
    print("You belong to the Stage 2 evacuation of the planet.")
    print("")
    return False
  #-----------------------------------------------------------------------#
  print('You belong to Stage 1 of evacuation of the planet.')
  return True

#======================================================================

#-----------------------------------------------------------------------#
#Function to determine to which evacuation stage the user who does not 
#know any programming language belongs:
def age_1(date):
  age = p.calculate_age(date)
  #-----------------------------------------------------------------------#
  #If the user is over 50 years of age, he/she will be assigned to evacuation stage 4.
  #If under 50 years of age, the user will be assigned to evacuation stage 3.:
  if age >= 50:
    print("You belong to Stage 4 of evacuation of the planet.")
    print("")
    print('================================================================')
    return False
  print("You belong to Stage 3 of evacuation of the planet.")
  print("")
  print('================================================================')
  return True