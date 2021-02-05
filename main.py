import pyfiglet as pyfiglet
from termcolor import colored

from colorama import Fore
from colorama import Style

import datetime

logiPython = colored(pyfiglet.figlet_format("LOGISCOOL PYTHON"), color="blue")
print(logiPython , "\n")

ElsoOra = colored(pyfiglet.figlet_format("1 . ORA"), color="red")
print(ElsoOra , "\n" , "\n" , "\n")

print ("Ezt a programot futtattad: ", datetime.datetime.now().strftime("%Y") , datetime.datetime.now().strftime("%B"), datetime.datetime.now().strftime("%d"),  " napon ", datetime.datetime.now().strftime("%X"), "-kor")
print('Hello World! :D \n-Laky730 \n \n ')

userName = input("Mi a neved? \n")
print(f"Üdvozöllek {Fore.GREEN}" , userName , f"{Style.RESET_ALL} ! \n \n")

userBirth = int(input("Mikor születtél? \n"))

print("Tehát a születési dátumod: " ,f"{Fore.RED}", userBirth, f"{Style.RESET_ALL}")
print("És a korod: " ,f"{Fore.RED}", int(datetime.datetime.now().strftime("%Y"))-int(userBirth), "\n \n", f"{Style.RESET_ALL}")

print("Mondj két számot! \n \n")
num1 = input("1.szám: \n")
num2 = input("2.szám: \n \n")

print("A két számod: \n")
print ("- Összeadva:",f"{Fore.BLUE}", int(num1) + int(num2), f"{Style.RESET_ALL}")
print ("- Kivonva:",f"{Fore.BLUE}", int(num1) - int(num2), f"{Style.RESET_ALL}")
print ("- Szorozva:",f"{Fore.BLUE}", int(num1) * int(num2), f"{Style.RESET_ALL}")
print ("- Osztva:",f"{Fore.BLUE}", int(num1) / int(num2), f"{Style.RESET_ALL}")
print ("- Maradékosan osztva:",f"{Fore.BLUE}", int(num1) % int(num2), f"{Style.RESET_ALL}")
print ("- Hatványozva:",f"{Fore.BLUE}", int(num1) ** int(num2), f"{Style.RESET_ALL}")
print ("- Osztva, majd kerekítve:",f"{Fore.BLUE}", int(num1) // int(num2), f"{Style.RESET_ALL}")

likedProgram = input("Tetszett a program? \n \n")

if(likedProgram == "Igen" or likedProgram == "igen" or likedProgram == "I" or likedProgram == "i"):
    print("Nagyon köszönöm! :)")

else:
    print("Nembaj. Attól még örülök, hogy kipróbáltad! :)")

input("")




