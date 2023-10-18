# Generated by Django 4.2.6 on 2023-10-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_items_item_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-status']},
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('LT', 'Lost'), ('FD', 'Found')], default='LT', max_length=2),
        ),
    ]