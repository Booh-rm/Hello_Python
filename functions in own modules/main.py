import persons
from stages import obtain_stage
from stages import is_prgmr
from stages import age_1

#-------------------------------------------------------------------------------------------
# @author Booh-rm
#-------------------------------------------------------------------------------------------

#======================================================================
#          E n t r y   p o i n t   t o   a p p l i c a t i o n
# =====================================================================

#-----------------------------------------------------------------------#

document = input("Enter your ID number: ")
name = input("Enter the full name: ")
email = input("Enter your e-mail address: ")
#-----------------------------------------------------------------------#

#======================================================================

#-----------------------------------------------------------------------#
#E-mail validation:
if persons.is_a_valid_email(email) is True:
  
  print('\n',"================================================================")
  print('\n',"E-mail Verified",'\n')

  #-----------------------------------------------------------------------#
  
  is__programmer = input("Do you have programming experience? (Yes, No): ")
  
#======================================================================
  
  #-----------------------------------------------------------------------#
  
  if is_prgmr(is__programmer) is True:
    print('\n')
    programming__language = input("Indicates in which programming language: ")

#======================================================================

    #-----------------------------------------------------------------------#
    #The user's date of birth is then asked in order to calculate the user's age:
    print('\n')
    date_born = input("Enter your date of birth in DD/MM/YYYY format: ")
    age = date_born 
    #-----------------------------------------------------------------------#    

#======================================================================

    #-----------------------------------------------------------------------#
    if persons.calculate_age(date_born):
      print("================================================================")
      print("")

#======================================================================

      #-----------------------------------------------------------------------#
      if obtain_stage(is__programmer, programming__language, age) is True:
        print("")
      
      print("================================================================")

#======================================================================      
    
  #-----------------------------------------------------------------------#

  elif is_prgmr(is__programmer) is False:
    date__born = input("Enter your date of birth in DD/MM/YYYY format: ")

    #-----------------------------------------------------------------------#

    age = date__born
    print("")
    print("================================================================")

#======================================================================     

    #-----------------------------------------------------------------------#

    if age_1(age) is True:
        print("")

#======================================================================
      
else:
  #-----------------------------------------------------------------------#

  print('\n')
  print("¡¡¡You are possibly a terrorist!!!", '\n')
  print("================================================================")

#======================================================================
