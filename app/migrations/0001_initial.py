# Generated by Django 3.2.13 on 2022-06-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("user_email", models.CharField(max_length=200)),
                ("bank_name", models.CharField(max_length=200)),
                ("requisite_number", models.CharField(max_length=200)),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("phone", "Phone"), ("bank_number", "Bank Num")],
                        default="phone",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lot",
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
                ("lot_initiator_email", models.CharField(max_length=64)),
                ("initiator_wallet", models.CharField(max_length=128)),
                ("price", models.FloatField()),
                ("supply", models.FloatField()),
                ("min_limit", models.FloatField()),
                ("max_limit", models.FloatField()),
                (
                    "lot_type",
                    models.CharField(
                        choices=[("buy", "Buy"), ("sell", "Sell")],
                        default="sell",
                        max_length=8,
                    ),
                ),
                (
                    "fiat_currency",
                    models.CharField(
                        choices=[("kzt", "Kzt"), ("usd", "Usd")],
                        default="kzt",
                        max_length=8,
                    ),
                ),
                (
                    "crypto_currency",
                    models.CharField(
                        choices=[("eth", "Eth"), ("erc20", "Erc20")],
                        default="eth",
                        max_length=8,
                    ),
                ),
                ("payment", models.ManyToManyField(to="app.Payment")),
            ],
        ),
    ]
