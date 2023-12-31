# Generated by Django 4.2.7 on 2023-11-20 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('descrip', models.CharField(default='Null', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('descrip', models.CharField(default='Null', max_length=250)),
                ('category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sub_Category', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='productimage/')),
                ('size', models.IntegerField(blank=True, default=0)),
                ('qty', models.IntegerField(blank=True, default=0)),
                ('colour', models.CharField(blank=True, default='', max_length=50)),
                ('brand', models.CharField(default='Null', max_length=250)),
                ('actual_amt', models.IntegerField(blank=True, default=0)),
                ('disc_amt', models.IntegerField(blank=True, default=0)),
                ('descrip', models.CharField(default='Null', max_length=50)),
                ('Category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='product.category')),
                ('Subcategory', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCategory', to='product.subcategory')),
            ],
        ),
    ]
