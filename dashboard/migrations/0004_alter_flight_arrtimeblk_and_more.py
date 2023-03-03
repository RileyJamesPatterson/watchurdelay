# Generated by Django 4.1.7 on 2023-03-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_flight_actualelapsedtime_alter_flight_airtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='ArrTimeBlk',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='CancellationCode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='CarrierDelay',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DepTimeBlk',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Dest',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DestCityName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DestState',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DestStateName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1Airport',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1AirportID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1AirportSeqID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1LongestGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1TailNum',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1TotalGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1WheelsOff',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div1WheelsOn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2Airport',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2AirportID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2AirportSeqID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2LongestGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2TailNum',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2TotalGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2WheelsOff',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div2WheelsOn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3Airport',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3AirportID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3AirportSeqID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3LongestGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3TailNum',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3TotalGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3WheelsOff',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div3WheelsOn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4Airport',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4AirportID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4AirportSeqID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4LongestGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4TailNum',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4TotalGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4WheelsOff',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div4WheelsOn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5Airport',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5AirportID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5AirportSeqID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5LongestGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5TailNum',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5TotalGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5WheelsOff',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Div5WheelsOn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DivActualElapsedTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DivArrDelay',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DivDistance',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DivReachedDest',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='FirstDepTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='FlightDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='IATA_CODE_Reporting_Airline',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='LateAircraftDelay',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='LongestAddGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='NASDelay',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='OriginCityName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='OriginState',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='OriginStateName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Reporting_Airline',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='SecurityDelay',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Tail_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='TotalAddGTime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='WeatherDelay',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
