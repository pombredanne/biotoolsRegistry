# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elixir', '0003_publication_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='gridid',
            field=models.TextField(null=True, blank=True),
        ),
    ]
