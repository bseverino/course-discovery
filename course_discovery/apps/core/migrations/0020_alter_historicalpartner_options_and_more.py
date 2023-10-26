# Generated by Django 4.2.5 on 2023-10-05 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalpartner',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Partner', 'verbose_name_plural': 'historical Partners'},
        ),
        migrations.AlterModelOptions(
            name='historicalsalesforceconfiguration',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical salesforce configuration', 'verbose_name_plural': 'historical salesforce configurations'},
        ),
    ]