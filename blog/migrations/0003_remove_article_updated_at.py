# Generated by Django 3.2.5 on 2021-08-20 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]