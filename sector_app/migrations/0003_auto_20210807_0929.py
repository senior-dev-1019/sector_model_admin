# Generated by Django 3.2.5 on 2021-08-07 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sector_app', '0002_debts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Outlook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outlook_name', models.CharField(max_length=64)),
                ('outlook_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlook_entity', to='sector_app.rating_entity')),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_name', models.CharField(max_length=64)),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scale', to='sector_app.rating_scale')),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_name', models.CharField(max_length=64)),
                ('watch_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_entity', to='sector_app.rating_entity')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_date', models.DateField()),
                ('rating_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_assigned', to='sector_app.rating_value')),
                ('rating_debt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_debt', to='sector_app.debts')),
                ('rating_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_entity', to='sector_app.rating_entity')),
                ('rating_outlook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_outlook', to='sector_app.rating_outlook')),
                ('rating_scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_scale', to='sector_app.rating_scale')),
                ('rating_watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_watch', to='sector_app.rating_watch')),
            ],
        ),
        migrations.AlterField(
            model_name='debts',
            name='debt_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debt_class', to='sector_app.debt_class'),
        ),
    ]