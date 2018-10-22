# Generated by Django 2.1.2 on 2018-10-22 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0012_insert_relations'),
    ]

    operations = [
        migrations.RenameField('EntityToWorkRel', 'from_model', 'from_entity'),
        migrations.RenameField('EntityToWorkRel', 'to_model', 'to_work'),
        migrations.RenameField('EntityToWorkRel', 'comments', 'commentary'),
        migrations.RenameField('EntityToEntityRel', 'from_model', 'from_entity'),
        migrations.RenameField('EntityToEntityRel', 'to_model', 'to_entity'),
        migrations.RenameField('EntityToEntityRel', 'comment', 'commentary'),
        migrations.RenameField('WorkToWorkRel', 'from_model', 'from_work'),
        migrations.RenameField('WorkToWorkRel', 'to_model', 'to_work'),
        migrations.RenameField('WorkToWorkRel', 'comments', 'commentary'),
        migrations.RenameField('Work', 'comments', 'commentary'),
        migrations.RenameField('Entity', 'comments', 'commentary'),
        migrations.RenameField(
            model_name='historicalentitytoentityrel',
            old_name='from_model',
            new_name='from_entity',
        ),
        migrations.RenameField(
            model_name='historicalentitytoentityrel',
            old_name='to_model',
            new_name='to_entity',
        ),
        migrations.RenameField(
            model_name='historicalworktoworkrel',
            old_name='from_model',
            new_name='from_work',
        ),
        migrations.RenameField(
            model_name='historicalworktoworkrel',
            old_name='to_model',
            new_name='to_work',
        ),
        migrations.RemoveField(
            model_name='historicalentitytoworkrel',
            name='from_model',
        ),
        migrations.RemoveField(
            model_name='historicalentitytoworkrel',
            name='to_model',
        ),
        migrations.AddField(
            model_name='historicalentitytoworkrel',
            name='from_entity',
            field=models.ForeignKey(blank=True, db_column='from_entity', db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Entity'),
        ),
        migrations.AddField(
            model_name='historicalentitytoworkrel',
            name='to_work',
            field=models.ForeignKey(blank=True, db_column='to_work', db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Work'),
        ),
        migrations.AlterField(
            model_name='entitytoworkrel',
            name='from_entity',
            field=models.ForeignKey(db_column='from_entity', on_delete=django.db.models.deletion.CASCADE,
                                    to='poet.Entity'),
        ),
        migrations.AlterField(
            model_name='entitytoworkrel',
            name='to_work',
            field=models.ForeignKey(db_column='to_work', on_delete=django.db.models.deletion.CASCADE, to='poet.Work'),
        ),
        migrations.RunSQL("ALTER TABLE poet_entity_to_work_rel RENAME COLUMN from_entity TO from_entity_id"),
        migrations.RunSQL("ALTER TABLE poet_entity_to_work_rel RENAME COLUMN to_work TO to_work_id"),
    ]
