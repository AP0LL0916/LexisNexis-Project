import os
import time
import json
import pandas as pd
from datetime import datetime

#Beginning of the program, program will ask for github urls 
def start():
  
    print("-------------------------------------------------------------")
    print("Welcome to the trufflehog scanner CLI interface.")
    print("-------------------------------------------------------------")
    print("\n\n\n\n\n\n")

    print("-------------------------------------------------------------")
    URLnum = input("How many repos will you be entering?\n")
    print("-------------------------------------------------------------")
    print("\n\n\n\n\n\n")
   
    
   

    URLnum = int(URLnum)
    ScanConfig(URLnum)

def ScanConfig(urls):
    #Collects array of URLS and gets them ready for scanning
    print()
    UrlSet = set()
    #Populates set with URLs entered by user 
    for x in range(urls):
        print("-------------------------------------------------------------")
        URLname = input("Enter URL \n")
        print("-------------------------------------------------------------")
        UrlSet.add(URLname)
    print("\n\n\n\n\n\n")
    
   

    print("-------------------------------------------------------------")
    auto = input("Do you want the program to have automated scanning? \n")
    print("-------------------------------------------------------------")
    print()

    
    #Takes user input to set timer for automated scanning
    if auto == "yes" or auto == "Yes" or auto == "YES":
        print("-------------------------------------------------------------")
        timer = input("Enter how many seconds the program should wait until next scan. \n")
        print("-------------------------------------------------------------")
        print()
        timer = int(timer)
    else:
        timer = "DONE"
    #passes timer and set of URLS to scanning function
    URLScan(UrlSet, timer)

def URLScan(UrlArray, timer):
    #Example URL (https://github.com/trufflesecurity/test_keys)
    
    #Scans through all the URLS and outputs results to results.txt in JSON format
    for val in UrlArray:
        repository = val.replace('https://github.com/', '')
        repoName, extra = repository.split("/", 1)

        now = datetime.now()
        current_date = now.date()
        current_date = str(current_date)

        current_time = now.time()
        current_time = str(current_time)
        time, extra2 = current_time.split(".", 1)

        #Concantenates the names for the JSON and CSV file
        fileName = repoName + '_' + current_date + '_' + time + ".json"
        csvName = repoName + '_' + current_date + '_' + time + ".csv"
        

        #Builds command to be sent to shell
        scan = "trufflehog3 "
        scan += val
        reportJ = " -f JSON >> "
        scanReport =  scan
        scanReport += reportJ
        scanReport += fileName

       

        os.system(scan)
        os.system(scanReport)
     
   #Passes URL set and timer to timer function
    CSV_Report(UrlArray, timer, fileName, csvName)

def CSV_Report(UrlArray, timer, fileName, csvName):

    #uses panda module inside virtual environment to conver
    #JSON into a CSV file to be uploaded to SQL server.
    csvCommand = "touch " + csvName
    os.system(csvCommand)

    df = pd.read_json(fileName)
    df.to_csv(csvName)

   
    
    Timer(UrlArray, timer)




def Timer(UrlArray, timer):

    if timer == "DONE":
        print("Scanning completed. \n\n\n")
        print("Exiting program. \n\n\n")
        quit()

    #https://github.com/AP0LL0916/test-keys-private
    #Counts down till next scan and then sends the set of URLs to scanned again looping until user pushes CTRL + C during timer function
    try:
        timer = str(timer)
        print("-----------------------------------------------------------------------------")
        print("PROGRAM IS NOW GOING TO SLEEP FOR " + timer + " seconds.")
        print("-----------------------------------------------------------------------------")
        print("TO QUIT OUT PROGRAM PUSH CTRL + C")
        print("-----------------------------------------------------------------------------")
        timer = int(timer)
        time.sleep(timer)
        print()
        URLScan(UrlArray, timer)

    except KeyboardInterrupt:
        print("\n CLOSING PYTHON VIRTUAL ENVIRONMENT")
        print(" RAISING SYSTEM EXIT")
        raise SystemExit
    

#starts up python virtual env using bash script
print("STARTING UP VIRTUAL ENVIRONMENT")



start()







