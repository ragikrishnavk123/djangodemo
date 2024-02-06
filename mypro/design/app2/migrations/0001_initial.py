# Generated by Django 5.0.1 on 2024-01-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/places')),
            ],
        ),
    ]
