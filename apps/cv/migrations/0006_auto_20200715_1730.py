# Generated by Django 2.2.13 on 2020-07-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20200702_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='cv',
            name='education_and_qualifications',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='hobbies_and_interests',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='relevant_experience',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='work_history',
        ),
    ]
