# Generated by Django 3.0.4 on 2020-03-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('MiddleName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Mobile', models.BigIntegerField()),
                ('AlternateMobile', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1)),
                ('DateOfBirth', models.DateField()),
                ('Photo', models.ImageField(upload_to='ProfilePhotos')),
                ('Course', models.CharField(max_length=200)),
                ('IsAdmin', models.BooleanField()),
            ],
        ),
    ]
