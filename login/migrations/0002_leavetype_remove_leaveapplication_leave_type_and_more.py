# Generated by Django 4.1.5 on 2023-01-16 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('leave_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_type', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='leaveapplication',
            name='leave_type',
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='leave_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.leavetype'),
        ),
    ]
