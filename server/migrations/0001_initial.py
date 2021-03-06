# Generated by Django 2.0 on 2018-08-28 07:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='主机名称')),
                ('manufactor', models.CharField(blank=True, choices=[('DELL', '戴尔'), ('IBM', 'IBM'), ('HP', '惠普'), ('华为', '华为'), ('浪潮', '浪潮'), ('联想', '联想'), ('Cisco', '思科'), ('其他', '其他')], max_length=50, verbose_name='制造商')),
                ('serial_number', models.CharField(blank=True, max_length=50, verbose_name='序列号')),
                ('model', models.CharField(blank=True, max_length=50, verbose_name='主机型号')),
                ('warranty', models.BooleanField(verbose_name='是否在保')),
                ('nerwork_adapter_speed', models.CharField(blank=True, choices=[('100M', '百兆网卡'), ('1G', '千兆网卡'), ('10G', '万兆网卡')], max_length=50, verbose_name='网卡速率')),
                ('network_adapters', models.PositiveSmallIntegerField(blank=True, verbose_name='网卡数量')),
                ('processor_type', models.CharField(blank=True, max_length=50, verbose_name='处理器型号')),
                ('logical_processors', models.PositiveSmallIntegerField(blank=True, verbose_name='逻辑处理器数量')),
                ('memory', models.PositiveSmallIntegerField(blank=True, verbose_name='内存大小')),
                ('max_memory', models.PositiveSmallIntegerField(blank=True, verbose_name='最大内存容量')),
                ('hard_disk_counts', models.PositiveSmallIntegerField(blank=True, verbose_name='磁盘数量')),
                ('raid_type', models.CharField(blank=True, choices=[('Raid0', 'Raid0'), ('Raid1', 'Raid1'), ('Raid10', 'Raid10'), ('Raid5', 'Raid5'), ('Raid6', 'Raid6'), ('none', '无Raid')], max_length=50, verbose_name='RAID类型')),
            ],
        ),
    ]
