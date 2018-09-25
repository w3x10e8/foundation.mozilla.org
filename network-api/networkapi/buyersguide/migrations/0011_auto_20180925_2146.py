# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-25 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0010_auto_20180925_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='update',
        ),
        migrations.AddField(
            model_name='product',
            name='update1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update1', to='buyersguide.Update'),
        ),
        migrations.AddField(
            model_name='product',
            name='update2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update2', to='buyersguide.Update'),
        ),
        migrations.AddField(
            model_name='product',
            name='update3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update3', to='buyersguide.Update'),
        ),
        migrations.AddField(
            model_name='product',
            name='update4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update4', to='buyersguide.Update'),
        ),
        migrations.AddField(
            model_name='product',
            name='update5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update5', to='buyersguide.Update'),
        ),
    ]