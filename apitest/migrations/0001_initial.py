# Generated by Django 3.2.18 on 2023-07-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addcube',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.TextField()),
                ('character_name', models.CharField(max_length=12)),
                ('create_date', models.DateTimeField()),
                ('cube_type', models.CharField(max_length=12)),
                ('item_upgrade_result', models.CharField(max_length=12)),
                ('item_level', models.IntegerField()),
                ('target_item', models.CharField(max_length=20)),
                ('additional_potential_option_grade', models.CharField(max_length=4)),
                ('before_options_value1', models.CharField(max_length=30)),
                ('before_options_grade1', models.CharField(max_length=4)),
                ('before_options_value2', models.CharField(max_length=30)),
                ('before_options_grade2', models.CharField(max_length=4)),
                ('before_options_value3', models.CharField(max_length=30)),
                ('before_options_grade3', models.CharField(max_length=4)),
                ('after_options_value1', models.CharField(max_length=30)),
                ('after_options_grade1', models.CharField(max_length=4)),
                ('after_options_value2', models.CharField(max_length=30)),
                ('after_options_grade2', models.CharField(max_length=4)),
                ('after_options_value3', models.CharField(max_length=30)),
                ('after_options_grade3', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'Addcube',
            },
        ),
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.TextField()),
                ('character_name', models.CharField(max_length=12)),
                ('create_date', models.DateTimeField()),
                ('cube_type', models.CharField(max_length=12)),
                ('item_upgrade_result', models.CharField(max_length=12)),
                ('item_level', models.IntegerField()),
                ('target_item', models.CharField(max_length=20)),
                ('potential_option_grade', models.CharField(max_length=4)),
                ('before_options_value1', models.CharField(max_length=30)),
                ('before_options_grade1', models.CharField(max_length=4)),
                ('before_options_value2', models.CharField(max_length=30)),
                ('before_options_grade2', models.CharField(max_length=4)),
                ('before_options_value3', models.CharField(max_length=30)),
                ('before_options_grade3', models.CharField(max_length=4)),
                ('after_options_value1', models.CharField(max_length=30)),
                ('after_options_grade1', models.CharField(max_length=4)),
                ('after_options_value2', models.CharField(max_length=30)),
                ('after_options_grade2', models.CharField(max_length=4)),
                ('after_options_value3', models.CharField(max_length=30)),
                ('after_options_grade3', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'Cube',
            },
        ),
    ]