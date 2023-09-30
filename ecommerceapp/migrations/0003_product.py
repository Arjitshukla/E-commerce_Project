# Generated by Django 4.2.4 on 2023-09-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_alter_contact_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.ImageField(default=0, upload_to='')),
                ('desc', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
    ]