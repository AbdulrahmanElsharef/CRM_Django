# Generated by Django 4.2 on 2023-11-06 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Technical", "0005_alter_report_advice"),
    ]

    operations = [
        migrations.AddField(
            model_name="failer_detail",
            name="ref",
            field=models.CharField(
                default="No_Ref", max_length=25, verbose_name="REF_NUM"
            ),
        ),
        migrations.AddField(
            model_name="report",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Report_Product",
                to="Technical.product",
                verbose_name="Product",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="request",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="request_Report",
                to="Technical.request",
                verbose_name="Request",
            ),
        ),
    ]
