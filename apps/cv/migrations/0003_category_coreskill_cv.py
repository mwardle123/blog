# Generated by Django 2.2.13 on 2020-07-01 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('addresses', models.TextField()),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('personal_profile', models.TextField()),
                ('education_and_qualifications', models.TextField()),
                ('relevant_experience', models.TextField()),
                ('work_history', models.TextField()),
                ('hobbies_and_interests', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CoreSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_skills', to='cv.Category')),
            ],
        ),
    ]
