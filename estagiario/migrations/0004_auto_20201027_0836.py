# Generated by Django 3.1.2 on 2020-10-27 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201019_1549'),
        ('estagiario', '0003_auto_20201027_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagiario',
            name='curso',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='estagiario',
            name='instituicao_edu',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.instituicao', verbose_name='Instituição de ensino'),
        ),
    ]
