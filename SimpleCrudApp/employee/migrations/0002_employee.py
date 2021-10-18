# Generated by Django 3.2.8 on 2021-10-18 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=90)),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='employee.department')),
            ],
        ),
    ]