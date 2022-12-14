# Generated by Django 4.1.1 on 2022-09-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=200, verbose_name='Название')),
                ('description', models.CharField(help_text='Введите описание модели', max_length=500, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
