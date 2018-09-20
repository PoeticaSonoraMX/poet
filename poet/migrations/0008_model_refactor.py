# Generated by Django 2.1.1 on 2018-09-20 01:57

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poet', '0007_historicalcomposicion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(blank=True, null=True)),
                ('alt_name', models.TextField(blank=True, null=True)),
                ('entity_type', models.CharField(choices=[('PERSONA', 'Persona'), ('GRUPO', 'Grupo'), ('ORGANIZACIÓN', 'Organización'), ('FESTIVAL', 'Festival'), ('UNIVERSIDAD', 'Universidad'), ('COLECTIVO', 'Colectivo'), ('ESTACIÓN RADIOFÓNICA', 'Estación radiofónica'), ('EDUCACIÓN E INVESTIGACIÓN', 'Educación e investigación'), ('ARCHIVO SONORO', 'Archivo sonoro'), ('SERVICIOS DE STREAMING', 'Servicios de streaming'), ('MUSEO', 'Museo'), ('EDITORIAL', 'Editorial'), ('SELLO DISCOGRÁFICO', 'Sello discográfico'), ('CENTRO CULTURAL', 'Centro cultural'), ('BANDA MUSICAL', 'Banda musical')], default='PERSONA', max_length=32)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('from_date_end', models.DateField(blank=True, null=True)),
                ('to_date_end', models.DateField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('file_path', models.FilePathField(blank=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, null=True, size=None)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('release_state', models.CharField(choices=[('PUBLICADO', 'Published'), ('DEPOSITAR', 'Deposited'), ('PENDIENTE', 'Pending'), ('REJECTED', 'Rejected')], default='PENDIENTE', max_length=32)),
            ],
            options={
                'db_table': 'poet_entity',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EntityToEntityRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contains', models.BooleanField(default=False, verbose_name='Is part of')),
                ('role', models.TextField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('from_date_end', models.DateField(blank=True, null=True)),
                ('to_date_end', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('from_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_entity', to='poet.Entity')),
                ('to_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_entity', to='poet.Entity')),
            ],
            options={
                'db_table': 'poet_entity_to_entity_rel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EntityToWorkRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Lectura en voz alta', 'Lectura en voz alta'), ('Interpretación musical', 'Interpretación musical'), ('Ingeniería de sonido', 'Ingeniería de sonido'), ('Producción', 'Producción'), ('Dirección', 'Dirección'), ('Post-producción', 'Post-producción'), ('Auxiliar de sonido', 'Auxiliar de sonido'), ('Contribuidor', 'Contribuidor'), ('Publicador', 'Publicador'), ('Composición', 'Composición'), ('Traducción', 'Traducción')], max_length=128)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('from_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poet.Entity')),
            ],
            options={
                'db_table': 'poet_entity_to_work_rel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalEntity',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('full_name', models.TextField(blank=True, null=True)),
                ('alt_name', models.TextField(blank=True, null=True)),
                ('entity_type', models.CharField(choices=[('PERSONA', 'Persona'), ('GRUPO', 'Grupo'), ('ORGANIZACIÓN', 'Organización'), ('FESTIVAL', 'Festival'), ('UNIVERSIDAD', 'Universidad'), ('COLECTIVO', 'Colectivo'), ('ESTACIÓN RADIOFÓNICA', 'Estación radiofónica'), ('EDUCACIÓN E INVESTIGACIÓN', 'Educación e investigación'), ('ARCHIVO SONORO', 'Archivo sonoro'), ('SERVICIOS DE STREAMING', 'Servicios de streaming'), ('MUSEO', 'Museo'), ('EDITORIAL', 'Editorial'), ('SELLO DISCOGRÁFICO', 'Sello discográfico'), ('CENTRO CULTURAL', 'Centro cultural'), ('BANDA MUSICAL', 'Banda musical')], default='PERSONA', max_length=32)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('from_date_end', models.DateField(blank=True, null=True)),
                ('to_date_end', models.DateField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('file_path', models.FilePathField(blank=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, null=True, size=None)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('release_state', models.CharField(choices=[('PUBLICADO', 'Published'), ('DEPOSITAR', 'Deposited'), ('PENDIENTE', 'Pending'), ('REJECTED', 'Rejected')], default='PENDIENTE', max_length=32)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical entity',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEntityToEntityRel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('contains', models.BooleanField(default=False, verbose_name='Is part of')),
                ('role', models.TextField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('from_date_end', models.DateField(blank=True, null=True)),
                ('to_date_end', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('from_model', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Entity')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_model', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Entity')),
            ],
            options={
                'verbose_name': 'historical entity to entity rel',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEntityToWorkRel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('role', models.CharField(choices=[('Lectura en voz alta', 'Lectura en voz alta'), ('Interpretación musical', 'Interpretación musical'), ('Ingeniería de sonido', 'Ingeniería de sonido'), ('Producción', 'Producción'), ('Dirección', 'Dirección'), ('Post-producción', 'Post-producción'), ('Auxiliar de sonido', 'Auxiliar de sonido'), ('Contribuidor', 'Contribuidor'), ('Publicador', 'Publicador'), ('Composición', 'Composición'), ('Traducción', 'Traducción')], max_length=128)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('from_model', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Entity')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical entity to work rel',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalWork',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('full_name', models.TextField(blank=True, null=True)),
                ('alt_name', models.TextField(blank=True, null=True)),
                ('work_type', models.CharField(choices=[('ALBUM', 'Album'), ('SERIE', 'Series'), ('COMPOSICION', 'Composition'), ('PISTA SON', 'Recording'), ('PRIVILEGIO', 'Copyright')], default='COMPOSICION', max_length=32)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('path_to_file', models.FilePathField(blank=True, null=True)),
                ('file_type', models.CharField(choices=[('AUDIO', 'Audio'), ('IMAGE', 'Image')], max_length=25, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, null=True, size=None)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('release_state', models.CharField(choices=[('PUBLICADO', 'Published'), ('DEPOSITAR', 'Deposited'), ('PENDIENTE', 'Pending'), ('REJECTED', 'Rejected')], default='PENDIENTE', max_length=32)),
                ('copyright', models.TextField(blank=True, null=True)),
                ('copyright_country', models.TextField(blank=True, null=True)),
                ('copyright_date', models.DateField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical work',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalWorkToWorkRel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('contains', models.BooleanField(default=False, verbose_name='Is part of')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical work to work rel',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(blank=True, null=True)),
                ('alt_name', models.TextField(blank=True, null=True)),
                ('work_type', models.CharField(choices=[('ALBUM', 'Album'), ('SERIE', 'Series'), ('COMPOSICION', 'Composition'), ('PISTA SON', 'Recording'), ('PRIVILEGIO', 'Copyright')], default='COMPOSICION', max_length=32)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('path_to_file', models.FilePathField(blank=True, null=True)),
                ('file_type', models.CharField(choices=[('AUDIO', 'Audio'), ('IMAGE', 'Image')], max_length=25, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, null=True, size=None)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('release_state', models.CharField(choices=[('PUBLICADO', 'Published'), ('DEPOSITAR', 'Deposited'), ('PENDIENTE', 'Pending'), ('REJECTED', 'Rejected')], default='PENDIENTE', max_length=32)),
                ('copyright', models.TextField(blank=True, null=True)),
                ('copyright_country', models.TextField(blank=True, null=True)),
                ('copyright_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'poet_work',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WorkToWorkRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contains', models.BooleanField(default=False, verbose_name='Is part of')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('additional_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('from_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_work', to='poet.Work')),
                ('to_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_work', to='poet.Work')),
            ],
            options={
                'db_table': 'poet_work_to_work_rel',
                'managed': True,
            },
        ),
        # migrations.RenameField(
        #     model_name='coberturalicencia',
        #     old_name='cobertura_lic_id',
        #     new_name='id',
        # ),
        # migrations.AlterField(
        #     model_name='cobertura',
        #     name='cobertura_lic',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poet.CoberturaLicencia', to_field='cobertura_lic_id'),
        # ),
        migrations.AddField(
            model_name='work',
            name='self_relation',
            field=models.ManyToManyField(blank=True, through='poet.WorkToWorkRel', to='poet.Work'),
        ),
        migrations.AddField(
            model_name='historicalworktoworkrel',
            name='from_model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Work'),
        ),
        migrations.AddField(
            model_name='historicalworktoworkrel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalworktoworkrel',
            name='to_model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Work'),
        ),
        migrations.AddField(
            model_name='historicalentitytoworkrel',
            name='to_model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='poet.Work'),
        ),
        migrations.AddField(
            model_name='entitytoworkrel',
            name='to_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poet.Work'),
        ),
        migrations.AddField(
            model_name='entity',
            name='self_relation',
            field=models.ManyToManyField(blank=True, through='poet.EntityToEntityRel', to='poet.Entity'),
        ),
        migrations.AddField(
            model_name='entity',
            name='work_relation',
            field=models.ManyToManyField(blank=True, through='poet.EntityToWorkRel', to='poet.Work'),
        ),
    ]