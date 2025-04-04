# Generated by Django 5.1.3 on 2025-03-31 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.BigIntegerField(unique=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("balance", models.IntegerField(default=0)),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="category",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="user",
        ),
        migrations.AddField(
            model_name="transaction",
            name="points",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="description",
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name="transaction",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="App.customer",
            ),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
