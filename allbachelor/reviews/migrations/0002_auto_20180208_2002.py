# Generated by Django 2.0.2 on 2018-02-08 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user_name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.Wine')),
            ],
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='wine',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
