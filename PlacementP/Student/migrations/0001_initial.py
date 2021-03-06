# Generated by Django 3.0.4 on 2020-03-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('MiddleName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Mobile', models.BigIntegerField()),
                ('AMobile', models.BigIntegerField(null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1)),
                ('DateOfBirth', models.DateField()),
                ('Address', models.CharField(max_length=300)),
                ('Lang1', models.CharField(max_length=100, null=True)),
                ('Lang2', models.CharField(max_length=100, null=True)),
                ('Lang3', models.CharField(max_length=100, null=True)),
                ('SchoolName10th', models.CharField(max_length=200)),
                ('BoardName10th', models.CharField(max_length=200)),
                ('Percentage10th', models.FloatField()),
                ('PassingYear10th', models.IntegerField()),
                ('CollegeName12th', models.CharField(max_length=200, null=True)),
                ('BoardName12th', models.CharField(max_length=200, null=True)),
                ('Percentage12th', models.FloatField(null=True)),
                ('PassingYear12th', models.IntegerField(null=True)),
                ('DiplomaInstituteName', models.CharField(max_length=200, null=True)),
                ('PercentageDiploma', models.FloatField(null=True)),
                ('PassingYearDiploma', models.IntegerField(null=True)),
                ('UGDegree', models.CharField(max_length=100)),
                ('UGCollegeName', models.CharField(max_length=200)),
                ('UGUniversity', models.CharField(max_length=200)),
                ('UGFYPercentage', models.FloatField()),
                ('UGSYPercentage', models.FloatField()),
                ('UGTYPercentage', models.FloatField()),
                ('UGPassingYear', models.IntegerField()),
                ('PGDegree', models.CharField(max_length=100)),
                ('PGCollegeName', models.CharField(max_length=200)),
                ('PGUniversity', models.CharField(max_length=200)),
                ('PGFYPercentage', models.FloatField()),
                ('PGSYPercentage', models.FloatField()),
                ('PGTYPercentage', models.FloatField()),
                ('PGPassingYear', models.IntegerField()),
                ('GAP', models.IntegerField()),
                ('ProjectName1', models.CharField(max_length=100)),
                ('ProjectTechnology1', models.CharField(max_length=200)),
                ('ProjectDesc1', models.CharField(max_length=300)),
                ('ProjectName2', models.CharField(max_length=100)),
                ('ProjectTechnology2', models.CharField(max_length=200)),
                ('ProjectDesc2', models.CharField(max_length=300)),
            ],
        ),
    ]
