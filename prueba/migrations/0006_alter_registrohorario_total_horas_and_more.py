# Generated by Django 5.1.2 on 2024-11-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prueba", "0005_alter_usuario_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrohorario",
            name="total_horas",
            field=models.CharField(
                blank=True,
                help_text="Total de horas trabajadas",
                max_length=150,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="solicitudjustificante",
            name="evidencia_pdf",
            field=models.FileField(blank=True, null=True, upload_to="documentos_pdfs/"),
        ),
    ]
