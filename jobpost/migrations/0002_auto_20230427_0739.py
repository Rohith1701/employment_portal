# Generated by Django 3.2 on 2023-04-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='will_relocate',
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='city',
            field=models.CharField(default='Bangalore', max_length=10),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='companyname',
            field=models.CharField(default='ABc', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='email',
            field=models.CharField(default='Abc@gmail.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='jobname',
            field=models.CharField(default='frontend', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='mobile',
            field=models.CharField(default='0123456789', max_length=10),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='salery',
            field=models.IntegerField(default='10000'),
        ),
    ]
