# Generated by Django 5.1.4 on 2025-04-25 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitem',
            name='status',
            field=models.CharField(choices=[('collection', 'In Collection'), ('listed', 'Listed on Marketplace'), ('pending', 'Pending Trade')], default='collection', max_length=20),
        ),
    ]
