# Generated by Django 5.0.6 on 2024-06-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]