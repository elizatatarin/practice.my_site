# Generated by Django 4.2.2 on 2023-08-28 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_name',
            new_name='image',
        ),
    ]