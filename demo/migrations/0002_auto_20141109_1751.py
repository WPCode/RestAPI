# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objects',
            old_name='name',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='objects',
            name='description',
        ),
        migrations.RemoveField(
            model_name='objects',
            name='end',
        ),
        migrations.AddField(
            model_name='objects',
            name='firstName',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objects',
            name='lastName',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
