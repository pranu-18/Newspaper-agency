# Generated by Django 2.1.2 on 2018-11-08 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('amount', models.FloatField(default=0)),
                ('due', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Distributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('d_phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ('paper_name',),
            },
        ),
        migrations.CreateModel(
            name='Subscript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('subscription', models.ManyToManyField(default='', to='agency.Publications')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Customers')),
                ('distributor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Distributors')),
            ],
        ),
        migrations.CreateModel(
            name='WithHold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Customers')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='subscription',
            field=models.ManyToManyField(default='', to='agency.Publications'),
        ),
    ]
