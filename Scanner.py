import os
import time
from datetime import datetime

#Beginning of the program, program will ask for github urls 
def start():
  
    
    print("Welcome to the trufflehog scanner CLI interface.")
    print("-------------------------------------------------------------")
    print()


    URLnum = input("How many repos will you be entering?")
    print("-------------------------------------------------------------")
    print()
    URLnum = int(URLnum)
    ScanConfig(URLnum)

def ScanConfig(urls):
    #Collects array of URLS and gets them ready for scanning
    print()
    UrlSet = set()
    #Populates set with URLs entered by user 
    for x in range(urls):
        URLname = input("Enter URL \n")
        print("-------------------------------------------------------------")
        UrlSet.add(URLname)
    print()
    
    #Takes user input to set timer for automated scanning
    timer = input("Enter how many seconds the program should wait until next scan. \n")
    print("-------------------------------------------------------------")
    print()
    timer = int(timer)
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

        fileName = repoName + '_' + current_date + '_' + time + ".json"

        scan = "trufflehog3 "
        scan += val
        report = " -f JSON >> "
        scanReport =  scan
        scanReport += report
        scanReport += fileName
        os.system(scan)
        os.system(scanReport)
   #Passes URL set and timer to timer function
    Timer(UrlArray, timer)


def Timer(UrlArray, timer):
    #https://github.com/AP0LL0916/test-keys-private
    #Counts down till next scan and then sends the set of URLs to scanned again looping until user pushes CTRL + C during timer function
    try:
        timer = str(timer)
        print("PROGRAM IS NOW GOING TO SLEEP FOR " + timer + " seconds.")
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
time.sleep(5)



start()







