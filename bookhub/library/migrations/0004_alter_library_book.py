# Generated by Django 5.0.3 on 2024-03-24 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_book_release_date'),
        ('library', '0003_alter_library_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='library_book', to='catalog.book'),
        ),
    ]
