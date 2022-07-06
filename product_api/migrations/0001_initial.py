# Generated by Django 4.0.2 on 2022-07-06 16:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='Название категории', max_length=100)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категория',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Теги',
                'verbose_name_plural': 'Тег',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Название', max_length=255, verbose_name='Название')),
                ('price', models.CharField(db_index=True, help_text='Цена', max_length=255, verbose_name='Цена')),
                ('description', models.TextField(help_text='Описание', verbose_name='Описание')),
                ('address', models.CharField(help_text='Место положения', max_length=255, verbose_name='Место положения')),
                ('average_rating', models.FloatField(db_index=True, default=0)),
                ('soft_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='categories_products', to='product_api.Category')),
                ('owner', models.ForeignKey(help_text='Владелец', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags_products', to='product_api.Tag')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукт',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_api.paymenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('path', models.ImageField(max_length=255, upload_to='uploads/products/%Y/%m/%d/')),
                ('soft_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(help_text='Продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_api.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Изображении',
                'verbose_name_plural': 'Изображение',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарии',
                'verbose_name_plural': 'Комментария',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='product_api.payment', verbose_name='Payment')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product_api.product', verbose_name='Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
                'ordering': ['-created_at'],
            },
        ),
    ]
