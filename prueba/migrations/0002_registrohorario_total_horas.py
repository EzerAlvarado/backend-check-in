# Generated by Django 5.1.2 on 2024-11-03 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohorario',
            name='total_horas',
            field=models.DurationField(blank=True, help_text='Total de horas trabajadas', null=True),
        ),
    ]
