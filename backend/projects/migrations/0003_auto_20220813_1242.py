# Generated by Django 3.2 on 2022-08-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220608_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='body',
            new_name='meterial_a_description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='title_image',
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image11',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image12',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_a_image',
            field=models.ImageField(blank=True, null=True, upload_to='meterials/'),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_a_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_b_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_b_image',
            field=models.ImageField(blank=True, null=True, upload_to='meterials/'),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_b_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_c_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_c_image',
            field=models.ImageField(blank=True, null=True, upload_to='meterials/'),
        ),
        migrations.AddField(
            model_name='project',
            name='meterial_c_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_owner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]