# Generated by Django 4.2.6 on 2023-10-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveIndex(
            model_name='items',
            name='pages_items_publish_4b777d_idx',
        ),
        migrations.RemoveField(
            model_name='items',
            name='publish',
        ),
        migrations.AddIndex(
            model_name='items',
            index=models.Index(fields=['-status'], name='pages_items_status_238ac9_idx'),
        ),
    ]
