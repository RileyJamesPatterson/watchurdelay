'''To run a script in the django context
1)Create a py file in the scirpts folder (this file)
2)Define a run() function below
3) call the script using the terminal command:
 python manage.py runscript file_name


 This script populates the flight data model with the contents of a csv file.
'''

import os
import sys
import json
from django.db import transaction
from dashboard import models

currentdir=os.path.dirname(__file__)
parentdir=os.path.dirname(currentdir)
print("------------------------")
fileName="airports_of_concern.json" 
sys.path.append(parentdir)
file_path=os.path.join(currentdir,fileName)
sys.path.append(parentdir)



def run():
    print("Populating airport table in db with json data")
    with open(file_path) as file:
        data=json.load(file)
        with transaction.atomic():
            for key in data:
                dic=data[key]
                print(dic["iata"])
                instance= models.Airport(iata=dic["iata"],name=dic["name"],lat=dic["lat"],lon=dic["lon"])
                instance.save()
    print("flight table upload complete")  
    #connections=
            
    

    print("airport upload complete")