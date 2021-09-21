# Generated by Django 2.2.24 on 2021-09-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profileuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'мужчина'), ('F', 'женщина'), ('MP', 'разнополый_гуманоид')], max_length=1, verbose_name='пол'),
        ),
    ]