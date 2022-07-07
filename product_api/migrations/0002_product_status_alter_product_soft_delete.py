# Generated by Django 4.0.2 on 2022-07-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, help_text='Активный/Не активный', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='soft_delete',
            field=models.BooleanField(default=False, help_text='Удаленный/Не удаленный', verbose_name='Удаленный'),
        ),
    ]
