# Generated by Django 3.0.2 on 2020-02-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0011_free_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free',
            name='comments',
            field=models.PositiveIntegerField(null=True, verbose_name='댓글수'),
        ),
    ]