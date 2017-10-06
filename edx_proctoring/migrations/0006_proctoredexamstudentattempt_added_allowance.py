# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_proctoring', '0005_proctoredexam_hide_after_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='proctoredexamstudentattempt',
            name='added_allowance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
