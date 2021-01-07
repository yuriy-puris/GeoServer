# Generated by Django 3.0.1 on 2020-02-21 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='shop_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Shop'),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='adress_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Address'),
        ),
    ]