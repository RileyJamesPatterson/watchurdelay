import csv


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
                fieldtype="models.BigIntegerField()"
            elif isfloat(col[1]):
                fieldtype="models.FloatField()"
            else:
                fieldtype="models.CharField(max_length=100)"
            print(f"{fieldname}={fieldtype}")

        '''
        print(demo)
        for field in zip(headers,demo) :
            print (field)
        '''

