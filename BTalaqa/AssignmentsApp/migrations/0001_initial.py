# Generated by Django 2.1.7 on 2019-03-15 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MCQAssignmentsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.Test')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'assignment',
                'verbose_name_plural': 'assignments',
                'permissions': (('edit_assignment', 'Can edit assignment'), ('read_assignment', 'Can read assignment')),
            },
        ),
        migrations.AlterUniqueTogether(
            name='assignments',
            unique_together={('user_id', 'test_id')},
        ),
    ]
