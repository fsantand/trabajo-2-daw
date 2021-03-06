# Generated by Django 3.1.2 on 2020-11-19 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20201105_1601'),
        ('atencion', '0006_auto_20201106_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='estado',
            field=models.PositiveSmallIntegerField(choices=[(0, 'solicitado'), (1, 'aceptado'), (2, 'confirmado'), (3, 'sesion'), (4, 'finalizado'), (5, 'cancelado')], default=0),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='fecha_reserva',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='interprete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='atenciones', to='usuario.interprete'),
        ),
    ]
