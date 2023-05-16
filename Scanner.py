import os

#Beginning of the program, program will ask for github urls 
def start():
    i = 1
    while i == 289:
    
        print("Welcome to the trufflehog scanner CLI interface.")
        print("-------------------------------------------------------------")
        print()


        URLnum = input("How many repos will you be entering?")
        URLgather()

def  URLgather():
    print()
    URLSCAN()

def URLSCAN():
    REPORT()

def REPORT():
    print()


start()







