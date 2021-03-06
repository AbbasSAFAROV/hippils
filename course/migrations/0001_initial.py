# Generated by Django 2.1.12 on 2020-06-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('phone_number', models.CharField(max_length=220)),
                ('mail', models.EmailField(max_length=254)),
                ('applicant_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('accept', 'accept'), ('declined', 'declined'), ('waiting', 'waiting')], default='waiting', max_length=202)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_date', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[('accept', 'accept'), ('declined', 'declined'), ('waiting', 'waiting')], default='waiting')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=220)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('starting_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(auto_now=True)),
                ('course_place', models.CharField(max_length=220)),
                ('price', models.SmallIntegerField()),
                ('max_apply', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('passive', 'passive'), ('active', 'active')], default='passive', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('publication_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('tel', models.CharField(max_length=220)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('alinan_kurs', models.ForeignKey(on_delete=True, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='TestPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_branch',
            field=models.ForeignKey(on_delete=True, to='course.CourseBranch'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicant_name',
            field=models.ForeignKey(on_delete=True, to='course.Student'),
        ),
        migrations.AddField(
            model_name='application',
            name='taken_course',
            field=models.ForeignKey(on_delete=True, to='course.Course'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='taken_course',
            field=models.ForeignKey(on_delete=True, to='course.Course'),
        ),
    ]
