# Generated by Django 2.1.12 on 2020-06-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200630_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(choices=[('accept', 'accept'), ('declined', 'declined'), ('waiting', 'waiting')], default='waiting', max_length=202),
        ),
    ]