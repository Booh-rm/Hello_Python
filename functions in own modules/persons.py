""" Module to validate mail chains Functions that return if a mail is valid or not
"""

#-----------------------------------------------------------------------#
#The datetime and relativedelta libraries are imported to calculate the user's age:
from datetime import datetime
from dateutil.relativedelta import relativedelta

#-----------------------------------------------------------------------#
def is_a_valid_email(email):
  #================================================================================

  #-----------------------------------------------------------------------#
  character = '*'
  quantity_at = email.count('@')
  quantity_m = email.count('m')

  
  if quantity_at >= 2 or quantity_at == 0:
    print('\n')
    print("Error!!!")
    return False
    if email.find('@frontiers.co') == -1:
      print('\n')
      print("Error!!!")
      return False
      if quantity_m >=3:
        print('\n')
        print("Error!!!")
        return False
        if email.find('=') == 0:
          print('\n')
          print("Error!!!")
          return False
          if email.find('+') == 0:
            print('\n')
            print('Error!!!')
            return False
            if email.find('&') == 0:
              print('\n')
              print('Error!!!')
              return False
              if email[2] is character:
                print('\n')
                print ("Error!!!")
                return False

  #-----------------------------------------------------------------------#
 #True is returned if the email is not considered invalid:
  return True

#================================================================================

#-----------------------------------------------------------------------#
def calculate_age( fecha ):

  #-----------------------------------------------------------------------#
  date_born = fecha

  #-----------------------------------------------------------------------#
  #Process to calculate the user's age:
  date_of_birth = datetime.strptime(date_born, "%d/%m/%Y")
  age = relativedelta(datetime.now(), date_of_birth)
  print("")
  print("Your age is: ",f"{age.years} years, {age.months} months y {age.days} days")
  print("")

  #-----------------------------------------------------------------------#
#ÛThe user's age in years is returned in order to define to which stage of evacuation the user belongs:
  return age.years