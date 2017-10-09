# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_proctoring', '0006_proctoredexamstudentattempt_added_allowance'),
    ]

    operations = [
        migrations.AddField(
            model_name='proctoredexam',
            name='section_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='proctoredexamstudentattempt',
            name='added_allowance',
            field=models.IntegerField(default=0),
        ),
    ]
