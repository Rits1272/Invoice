# Generated by Django 2.2.3 on 2019-08-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice_data',
            name='exp_data',
        ),
        migrations.AddField(
            model_name='invoice_data',
            name='exp_date',
            field=models.CharField(default=5, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice_data',
            name='free',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
