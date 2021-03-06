# Generated by Django 2.1.3 on 2018-11-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('job_category', models.CharField(max_length=255)),
                ('job_name', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('experience_time', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('job_info', models.CharField(max_length=5000)),
                ('request_num', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=800)),
                ('company_scale', models.CharField(max_length=255)),
                ('company_net', models.CharField(max_length=255)),
                ('company_property', models.CharField(max_length=255)),
                ('company_business', models.CharField(max_length=255)),
                ('issue_time', models.CharField(max_length=255)),
                ('remark', models.CharField(max_length=255, unique=True)),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'recruit_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
    ]
