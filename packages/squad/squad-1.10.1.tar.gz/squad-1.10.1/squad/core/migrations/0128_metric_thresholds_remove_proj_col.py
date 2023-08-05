# Generated by Django 2.2.6 on 2020-03-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0127_metric_thresholds_migrate_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricthreshold',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Environment'),
        ),
        migrations.AlterUniqueTogether(
            name='metricthreshold',
            unique_together={('environment', 'name')},
        ),
        migrations.RemoveField(
            model_name='metricthreshold',
            name='project',
        ),
    ]
