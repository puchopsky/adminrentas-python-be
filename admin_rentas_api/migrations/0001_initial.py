# Generated by Django 2.2.3 on 2019-07-24 20:03

import admin_rentas_api.models.SubProperyModel
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacteristicsCatalog',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EstadosRepublicaCatalog',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LeasingTypeCatalog',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OwnedProperty',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('property_name', models.CharField(max_length=200)),
                ('property_alias', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('num_ext', models.CharField(max_length=30)),
                ('num_int', models.CharField(max_length=30, null=True)),
                ('colonia', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=5)),
                ('municipio', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=50)),
                ('belongs_to', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypeCatalog',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SubProperty',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('subproperty_alias', models.CharField(max_length=200)),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('characteristics', djongo.models.fields.EmbeddedModelField(model_container=admin_rentas_api.models.SubProperyModel.Characteristics, null=True)),
                ('billing_period', models.IntegerField()),
                ('belongsTo', models.CharField(max_length=200)),
            ],
        ),
    ]