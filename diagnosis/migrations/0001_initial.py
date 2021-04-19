# Generated by Django 3.1.7 on 2021-04-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionResult',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('way', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=10)),
                ('processed_img_path', models.CharField(max_length=100)),
                ('img_path', models.CharField(max_length=100)),
                ('patient_id', models.CharField(max_length=20)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
