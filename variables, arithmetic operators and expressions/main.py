from math import pi

#-------------------------------------------------------------------------------------------
# @author Booh-rm
#-------------------------------------------------------------------------------------------

#===========================================================================================
#                         D A T A   E N T E R E D   B Y   U S E R
#===========================================================================================

print("\n")
width_door_mts = float(input('Enter the width of the door in meters: '))
diameter_pulley_cms = float(input('Enter the diameter of the pulley in centimeters: '))
print("")


#===========================================================================================
#                   V E RI F I C A T I O N   O F   D A T A   I N P U T
#===========================================================================================

def input_data_by_user():

    print("==================================================================================================")
    print("--------------------------------------------------------------------------------------------------","\n")
    print('\033[1m', "You have entered the following data:", '\033[0m')
    print("")
    print("The door width is: ",width_door_mts, "meters")
    print("The pulley diameter is: ", diameter_pulley_cms, "centimeters")
    print("")
    print("--------------------------------------------------------------------------------------------------","\n") 


#===========================================================================================
#                       P R O B L E M   S O L V I N G   P R O C E S S
#===========================================================================================

def problem_solving_process():
    
    print('\033[1m', "Conversions and data to be used to solve the problem:", '\033[0m')
    print("")

    '''
    Since the image of the problem forms an equilateral triangle, it is determined 
    that the height of the wall is equal to the length of the door.
    '''
    wall_height = width_door_mts
    print("The height of the wall is: ", wall_height, "meters")


    #Conversion from meters to centimeters of wall height.
    wall_height_in_cm = (wall_height*100)/1
    print("The height of the wall in centimeters is: ", wall_height_in_cm, "centimeters")

    pulley_radius = diameter_pulley_cms/2
    print("The pulley radius is: ", pulley_radius, "centimeters")


    '''
    #laps = Height/(2*π*r)
    
    The variable number_of_turns is made global in order to access it
    from the to be able to access it from the results function.
    '''
    global number_of_turns
    number_of_turns =  (wall_height_in_cm)/((2*pi)*pulley_radius)


    '''
    Number of Chewbaccas to use:
    '''
    Number_of_Chewbaccas = (1*number_of_turns)/3
    '''
    But since the number of Chewbaccas to be used cannot be a
    number with decimals then the resulting number must be approximated to the nearest number you have.
    
    The variable Chewbaccas is also made global so that 
    it can be accessed from the results function. the results function.
    '''
    global Chewbaccas
    Chewbaccas = round(Number_of_Chewbaccas)  


    '''
    Since you want to close the door in a given maximum number of minutes, 
    here you need to find the speed at which the pulley must rotate to close the door on time.

    You also make the variable minutes_given global so that you can access it 
    from the results function.
    '''
    global minutes_given
    minutes_given = float(5)
    print("The minutes given to close the door are:", minutes_given, "minutes")
    
    #minutes to seconds conversion:
    time_seconds = (minutes_given*60)/1
    print("The minutes given to close the door converted to seconds are:", time_seconds, "seconds")

    global speed
    speed = (wall_height_in_cm)/(time_seconds)


#===========================================================================================
#                                       R E S U L T S
#===========================================================================================


def results(): 

    print("")
    print("--------------------------------------------------------------------------------------------------") 
    print("")
    print('\033[1m', "The results obtained are as follows:", '\033[0m')
    print("")
    print("The turns that must be made to close the door completely are: ", number_of_turns, "laps")
    print("The number of Chewbaccas to use to close the door are: ", Chewbaccas, "Chewbaccas")
    print("The speed required to close the door in ", minutes_given, "minutes is from: ", speed, "cm/sec")
    print("")
    print("==================================================================================================")
    print("--------------------------------------------------------------------------------------------------","\n")


#===========================================================================================
#                   A P P L I C A T I O N   S T A R T   S P A C E
#===========================================================================================

def application_start():
    input_data_by_user()
    problem_solving_process()
    results()

application_start()
