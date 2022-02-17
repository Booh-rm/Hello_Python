import random
import colorama

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'

def help():

    print (colorama.Fore.WHITE)
    print("==============================================================================" + "\n")
    print("                     Welcome To My Shell !!               ")
    print("                     Command help section !!    " + "\n")
    print("==============================================================================")
    print("")
    print(colorama.Fore.CYAN + 
            " Option                 meaning           " + "\n")

    print(colorama.Fore.WHITE + 
          ''' cd <directory>        changes the current directory to <directory>.

 PWD                    Prints the current working directory.
 
 clr                    Clean the screen.
 
 dir <directory>        Lists the contents of <directory>.
 
 environ                Displays all environment variables.
 
 echo <comment>      Displays <comment> on the screen followed by a new line.
 
 help                   Displays the user's manual.
  
 quit                   Exits the mandate interpreter.''')

    print("\n" + "==============================================================================")
    print(colorama.Fore.GREEN)