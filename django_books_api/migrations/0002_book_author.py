# Generated by Django 3.2.4 on 2021-08-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_books_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Author',
            field=models.CharField(default='yusuf', max_length=150),
        ),
    ]
