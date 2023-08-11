# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:19:56 2023

@author: Gihan kurukulasooriya
"""
def binary_solver():
    binary_num = input("Please enter a binary number of your choosing:")
    binary_num_list = list(binary_num)
    total_as_dec = 0
    power = 0
    for i in reversed(binary_num_list):
        if(i=="0"):
            total_as_dec+=0
        elif(i=="1"):
            total_as_dec+=int(i)*pow(2,power)
        else:
            print("You have inputted a wrong number try again")
        power+=1
    print("The binary number:" , binary_num , "in decimal is: ", total_as_dec, "and in hexadecimal its: " , hex(total_as_dec))
    return total_as_dec

            
if __name__ == "__main__":
    choice = input("Welcome to the binary, hexa, and decimal converter, please type 1, 2 or 3 depending on what converter you want to use, 1 for binary, 2 for hexa, 3 for decimal or type exit to exit:")
    while(choice != "exit"):
        if(choice == "1"):
            binary_solver()
        else:
            break



