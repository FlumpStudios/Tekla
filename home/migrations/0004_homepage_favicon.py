# Generated by Django 2.2.3 on 2020-04-13 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0003_blogindexpage_featurespage_formfield_formpage_pricingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='favicon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
