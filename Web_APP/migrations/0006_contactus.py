# Generated by Django 3.2.7 on 2022-03-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_APP', '0005_auto_20220315_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
