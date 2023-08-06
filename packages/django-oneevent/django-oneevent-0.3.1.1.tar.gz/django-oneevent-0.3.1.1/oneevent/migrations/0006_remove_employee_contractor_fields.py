from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneevent', '0005_create_employee_contractor_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='contractors_groups',
        ),
        migrations.RemoveField(
            model_name='event',
            name='employees_exception_groups',
        ),
        migrations.RemoveField(
            model_name='event',
            name='employees_groups',
        ),
        migrations.RemoveField(
            model_name='event',
            name='price_for_contractors',
        ),
        migrations.RemoveField(
            model_name='event',
            name='price_for_employees',
        ),
    ]
