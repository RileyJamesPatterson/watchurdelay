import csv
'''script used to determine field names and field types
 to define flight model. Takes all headers in csv. 
 Will need to repoint it at fresh data
 pasted terminal output to create the flight model class.  
'''
#import populateflight
GOODFIELDS=["demo"]

def isint(str):
# helper function to check if string can be cast as int
    try:
        int(str)
    except ValueError:
        return False
    else:
        return True

def isfloat(str):
# helper function to check if string can be cast as float
    try:
        float(str)
    except ValueError:
        return False
    else:
        return True

if __name__=="__main__":
    with open("On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2022_9.csv") as file:
        data=csv.reader(file)
        headers=next(data)
        demodata=next(data)
        for col in zip(headers,demodata):
            #print(col)
            fieldname=col[0]
            if isint(col[1]):
                fieldtype="models.BigIntegerField(null=True, blank=True)"
            elif isfloat(col[1]):
                fieldtype="models.FloatField(null=True, blank=True)"
            else:
                fieldtype="models.CharField(max_length=100, null=True, blank=True)"
            print(f"{fieldname}={fieldtype}")
            print(GOODFIELDS)

        '''
        print(demo)
        for field in zip(headers,demo) :
            print (field)
        print(GOODFIELDS)
        '''

