# Generated by Django 4.0.4 on 2022-05-25 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_remove_job_job_category_job_job_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='salary',
            new_name='salary_range',
        ),
    ]
