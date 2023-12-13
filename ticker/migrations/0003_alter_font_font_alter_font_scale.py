# Generated by Django 5.0 on 2023-12-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_ticker_text_alter_font_color_alter_font_font_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='font',
            field=models.CharField(choices=[(3, 'COMPLEX'), (0, 'SIMPLEX')], default=3, max_length=50),
        ),
        migrations.AlterField(
            model_name='font',
            name='scale',
            field=models.PositiveIntegerField(),
        ),
    ]
