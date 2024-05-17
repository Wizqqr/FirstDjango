# Generated by Django 5.0.4 on 2024-05-17 13:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telephone', '0003_comment_created_at_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='phone',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='telephone.phone'),
        ),
    ]