# Generated by Django 4.2.3 on 2023-09-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_alter_contdb_mail_alter_contdb_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contdb',
            name='cmt',
            field=models.TextField(null=True),
        ),
    ]
