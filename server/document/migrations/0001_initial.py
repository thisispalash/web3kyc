# Generated by Django 3.1 on 2020-08-19 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=47)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('links', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.person')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(blank=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('filehash', models.TextField()),
                ('doctype', models.CharField(choices=[('PASS', 'Passport'), ('DVL', 'driving licence'), ('PAN', 'pan card'), ('AADH', 'aadhar card')], max_length=4)),
                ('filetype', models.CharField(choices=[('PDF', 'PDF document'), ('PNG', 'PNG image'), ('JPG', 'JPG/JPEG image')], max_length=3)),
                ('location', models.SlugField()),
                ('iden', models.CharField(max_length=20)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='document.person')),
            ],
        ),
    ]