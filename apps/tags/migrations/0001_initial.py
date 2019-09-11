# Generated by Django 2.2.1 on 2019-05-11 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('desc', models.TextField(max_length=500, verbose_name='分类描述')),
            ],
            options={
                'verbose_name': '标签分类',
                'verbose_name_plural': '标签分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名称')),
                ('is_index', models.BooleanField(default=False, verbose_name='是否指标')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('sort', models.IntegerField(default=1, verbose_name='排序')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.TagCategory', verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
    ]
