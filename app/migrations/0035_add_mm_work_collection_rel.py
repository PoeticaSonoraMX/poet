# Generated by Django 2.2.24 on 2021-09-23 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0034_add_license_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitytoworkrel',
            name='from_entity',
            field=models.ForeignKey(db_column='from_entity', on_delete=django.db.models.deletion.PROTECT, related_name='ew_from_model', to='app.Entity', verbose_name='From entity'),
        ),
        migrations.AlterField(
            model_name='entitytoworkrel',
            name='to_work',
            field=models.ForeignKey(db_column='to_work', on_delete=django.db.models.deletion.PROTECT, related_name='ew_to_model', to='app.Work', verbose_name='To recording'),
        ),
        migrations.CreateModel(
            name='WorkToCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.IntegerField(blank=True, null=True, verbose_name='Track number in that collection')),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='Additional commentary')),
                ('from_work', models.ForeignKey(db_column='from_work', on_delete=django.db.models.deletion.PROTECT, related_name='wc_from_model', to='app.Work', verbose_name='From work')),
                ('to_collection', models.ForeignKey(db_column='to_collection', on_delete=django.db.models.deletion.PROTECT, related_name='wc_to_model', to='app.WorkCollection', verbose_name='To collection')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'db_table': 'poet_work_to_collection_rel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalWorkToCollection',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('track_number', models.IntegerField(blank=True, null=True, verbose_name='Track number in that collection')),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='Additional commentary')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('from_work', models.ForeignKey(blank=True, db_column='from_work', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.Work', verbose_name='From work')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_collection', models.ForeignKey(blank=True, db_column='to_collection', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.WorkCollection', verbose_name='To collection')),
            ],
            options={
                'verbose_name': 'historical Member',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
