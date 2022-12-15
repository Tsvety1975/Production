# Generated by Django 4.1.3 on 2022-12-04 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_externaltelekomtasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='externaltelekomtasks',
            name='office_descropton',
            field=models.CharField(blank=True, max_length=50, verbose_name='Помещение| Room'),
        ),
        migrations.AddField(
            model_name='externaltelekomtasks',
            name='place_building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.buildings', verbose_name='Изберете сградата в която работите| Choose workplace building'),
        ),
    ]
