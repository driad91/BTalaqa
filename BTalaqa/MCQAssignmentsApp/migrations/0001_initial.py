# Generated by Django 2.1.7 on 2019-04-02 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
                'permissions': (('edit_answer', 'Can edit answer'), ('read_answer', 'Can read answer')),
            },
        ),
        migrations.CreateModel(
            name='AssignmentCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('exclusive_answer', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'permissions': (('edit_question', 'Can edit question'), ('read_question', 'Can read question')),
            },
        ),
        migrations.CreateModel(
            name='StudentTestAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'student answer',
                'verbose_name_plural': 'student answers',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('tag_color', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary'), ('success', 'success'), ('danger', 'danger'), ('warning', 'warning')], max_length=255)),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'tests',
                'permissions': (('edit_test', 'Can edit test'), ('read_test', 'Can read test')),
            },
        ),
        migrations.CreateModel(
            name='TestUserAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user_test',
                'verbose_name_plural': 'user_tests',
                'permissions': (('edit_assignment', 'Can edit assignment'), ('read_assignment', 'Can read assignment')),
            },
        ),
        migrations.AddField(
            model_name='test',
            name='assignment',
            field=models.ManyToManyField(related_name='assignment', through='MCQAssignmentsApp.TestUserAssignment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studenttestanswers',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.Test'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ManyToManyField(to='MCQAssignmentsApp.Test'),
        ),
        migrations.AddField(
            model_name='assignmentcreator',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.TestUserAssignment'),
        ),
        migrations.AddField(
            model_name='assignmentcreator',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCQAssignmentsApp.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='testuserassignment',
            unique_together={('user', 'test')},
        ),
        migrations.AlterUniqueTogether(
            name='studenttestanswers',
            unique_together={('student', 'test', 'question', 'answer')},
        ),
    ]
