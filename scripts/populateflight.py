'''To run a script in the django context
1)Create a py file in the scirpts folder (this file)
2)Define a run() function below
3) call the script using the terminal command:
 python manage.py runscript file_name


 This script populates the flight data model with the contents of a csv file.
'''
import csv
import os
import sys

currentdir=os.path.dirname(__file__)
parentdir=os.path.dirname(currentdir)
print("------------------------")
sys.path.append(parentdir)

fileName="On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2022_9.csv" #point this at data file and figure out how to loop through all files in data

from dashboard import models

file_path=os.path.join(currentdir,fileName)
sys.path.append(parentdir)

# a list of field headers to be added to the DB. Other Fields will be ignored
GOODFIELDS=[
 "Year","Quarter","Month","DayofMonth","DayOfWeek","Origin","OriginCityName","OriginState","OriginStateName","Dest","DestCityName","DestState","DestStateName","CRSDepTime","DepTime","DepDelay","DepDelayMinutes","DepartureDelayGroups","DepTimeBlk","ArrTime","ArrDelay","ArrDelayMinutes","ArrivalDelayGroups","ArrTimeBlk","Cancelled","CancellationCode","Diverted","Flights","Distance","DistanceGroup","CarrierDelay","WeatherDelay","NASDelay","SecurityDelay","LateAircraftDelay",
]

def run():
    print("Populating Flight table in db with csv data")
    with open(file_path) as file:
        data=csv.reader(file)
        #take first row as headers
        headers=data.__next__()
        
        for row in data:
            #each row becomes a dictionary
            dic={key:(val if val!="" else None) for key,val in zip(headers,row) if key in GOODFIELDS}

            instance=models.Flight(**dic)
            instance.save()
    print("flight table upload complete")    
    

        


