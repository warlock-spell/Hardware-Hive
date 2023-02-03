# Generated by Django 4.1.6 on 2023-02-03 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('item', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='category.category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]