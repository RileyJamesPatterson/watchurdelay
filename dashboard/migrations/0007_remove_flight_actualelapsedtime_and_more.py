# Generated by Django 4.1.7 on 2023-03-10 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_flight_arrtimeblk_alter_flight_carrierdelay_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='ActualElapsedTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='AirTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='ArrDel15',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='CRSArrTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='CRSElapsedTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DOT_ID_Reporting_Airline',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DestAirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DestAirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DestCityMarketID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DestStateFips',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DestWac',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1Airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1AirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1AirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1LongestGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1TailNum',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1TotalGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1WheelsOff',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div1WheelsOn',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2Airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2AirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2AirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2LongestGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2TailNum',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2TotalGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2WheelsOff',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div2WheelsOn',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3Airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3AirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3AirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3LongestGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3TailNum',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3TotalGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3WheelsOff',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div3WheelsOn',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4Airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4AirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4AirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4LongestGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4TailNum',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4TotalGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4WheelsOff',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div4WheelsOn',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5Airport',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5AirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5AirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5LongestGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5TailNum',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5TotalGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5WheelsOff',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Div5WheelsOn',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DivActualElapsedTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DivAirportLandings',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DivArrDelay',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DivDistance',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='DivReachedDest',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='FirstDepTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='FlightDate',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Flight_Number_Reporting_Airline',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='IATA_CODE_Reporting_Airline',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='LongestAddGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='OriginAirportID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='OriginAirportSeqID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='OriginCityMarketID',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='OriginStateFips',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='OriginWac',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Reporting_Airline',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='Tail_Number',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='TaxiIn',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='TaxiOut',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='TotalAddGTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='WheelsOff',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='WheelsOn',
        ),
    ]