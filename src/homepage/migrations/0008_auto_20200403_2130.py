# Generated by Django 3.0.4 on 2020-04-04 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200403_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='Artist',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='Artwork_Title',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='Comment_Box',
        ),
    ]
