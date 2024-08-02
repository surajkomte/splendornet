# Generated by Django 5.0.7 on 2024-08-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reviewModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movieTitle', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=100)),
                ('reviewContent', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('createaAt', models.DateField()),
                ('reviewer_email_id', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(max_length=20)),
                ('generes', models.CharField(max_length=40)),
            ],
        ),
    ]
