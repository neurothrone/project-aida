# Generated by Django 3.2.8 on 2021-10-13 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aida', '0002_rename_training_exercise_workout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weightset',
            name='exercise',
        ),
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ('-trained_at',)},
        ),
        migrations.RenameField(
            model_name='workout',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='workout',
            old_name='trained',
            new_name='trained_at',
        ),
        migrations.RenameField(
            model_name='workout',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.DeleteModel(
            name='CardioSet',
        ),
        migrations.DeleteModel(
            name='WeightSet',
        ),
    ]
