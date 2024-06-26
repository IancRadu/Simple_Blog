# Generated by Django 5.0.3 on 2024-03-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='caption',
        ),
        migrations.AddField(
            model_name='tag',
            name='caption',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
