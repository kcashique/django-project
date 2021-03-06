# Generated by Django 4.0.4 on 2022-05-16 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_country_state_district'),
        ('jobs', '0002_job_job_location_state_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile',
        ),
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='job',
            name='job_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_state', to='core.state'),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
