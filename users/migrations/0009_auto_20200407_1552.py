# Generated by Django 3.0.5 on 2020-04-07 11:22

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_department_workon_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='workon_countries',
        ),
        migrations.AddField(
            model_name='department',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='countries', to='users.Country'),
        ),
    ]