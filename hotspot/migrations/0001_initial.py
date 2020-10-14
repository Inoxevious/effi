# Generated by Django 3.0.8 on 2020-09-06 05:33

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('version_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('app_version', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('app_upload_date', models.DateTimeField()),
                ('app_expire_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'AppVersion',
                'verbose_name_plural': 'AppVersion',
            },
        ),
        migrations.CreateModel(
            name='Hotspot',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('reference', models.CharField(db_index=True, max_length=100)),
                ('current_volume', models.CharField(blank=True, max_length=100, null=True)),
                ('capacity', models.CharField(blank=True, choices=[('Meters', 'Meters'), ('Kilograms', 'Kilograms'), ('Liters', 'Liters'), ('Mililitres', 'Mililitres')], default='Kilograms', max_length=100, null=True)),
                ('qrCode', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('available', models.BooleanField(default=True)),
                ('courierState', models.CharField(blank=True, choices=[('pickupPoint', 'pickupPoint'), ('intransit', 'intransit'), ('delivered', 'delivered'), ('returning', 'returning'), ('returned', 'returned')], default='pickupPoint', max_length=100, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('city', models.CharField(blank=True, choices=[('Gweru', 'Gweru'), ('Harare', 'Harare'), ('Mutare', 'Mutare'), ('Bulawayo', 'Bulawayo'), ('Victoria Falls', 'Victoria_Falls'), ('Beitbridge', 'Beitbridge')], default='Gweru', max_length=100, null=True)),
                ('residence', models.CharField(blank=True, max_length=100, null=True)),
                ('neigbhourhood', models.CharField(blank=True, max_length=100, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('country', models.CharField(blank=True, choices=[('Zimbabwe', 'Zimbabwe'), ('Zambia', 'Zambia')], default='Zimbabwe', max_length=100, null=True)),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hotspot',
                'verbose_name_plural': 'Hotspots',
            },
        ),
        migrations.CreateModel(
            name='ActiveHotspot',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('desiel_pump', models.BooleanField(default=True)),
                ('desiel_pump_price', models.FloatField(blank=True, max_length=100, null=True)),
                ('petrol_pump', models.BooleanField(default=True)),
                ('petrol_pump_price', models.FloatField(blank=True, max_length=100, null=True)),
                ('gas_pump', models.BooleanField(default=True)),
                ('gas_pump_price', models.FloatField(blank=True, max_length=100, null=True)),
                ('hotspot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotspot.Hotspot')),
            ],
        ),
    ]