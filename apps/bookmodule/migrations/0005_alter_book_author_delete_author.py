# Generated by Django 5.1.2 on 2024-12-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0004_author_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
