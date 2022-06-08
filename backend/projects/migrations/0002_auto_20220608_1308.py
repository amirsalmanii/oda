# Generated by Django 3.2 on 2022-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
