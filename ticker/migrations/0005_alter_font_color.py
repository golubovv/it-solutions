# Generated by Django 5.0 on 2023-12-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0004_font_name_alter_font_font'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='color',
            field=models.CharField(choices=[('255 0 0', 'Red'), ('0 255 0', 'Green'), ('0 0 255', 'Blue'), ('255 255 255', 'White'), ('0 0 0', 'Black')], default='White', max_length=20),
        ),
    ]
