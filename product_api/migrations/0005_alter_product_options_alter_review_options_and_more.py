# Generated by Django 4.0.2 on 2022-06-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0004_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукт'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pk'], 'verbose_name': 'Комментарии', 'verbose_name_plural': 'Комментария'},
        ),
        migrations.AlterField(
            model_name='product',
            name='average_rating',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, help_text='Название', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(db_index=True, help_text='Цена', max_length=255, verbose_name='Цена'),
        ),
    ]