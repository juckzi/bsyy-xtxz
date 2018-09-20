from django.db import models
import uuid

# Create your models here.


class Host(models.Model):

    VENDOR_CHOICES = (
        ('DELL', '戴尔'),
        ('IBM', 'IBM'),
        ('HP', '惠普'),
        ('华为', '华为'),
        ('浪潮', '浪潮'),
        ('联想', '联想'),
        ('Cisco', '思科'),
        ('其他', '其他')
    )

    NETWORK_ADAPTER_SPEED_CHOICES = (
        ('100M', '百兆网卡'),
        ('1G', '千兆网卡'),
        ('10G', '万兆网卡')
    )

    RAID_TYPE_CHOICES = (
        ('Raid0','Raid0'),
        ('Raid1','Raid1'),
        ('Raid10','Raid10'),
        ('Raid5','Raid5'),
        ('Raid6','Raid6'),
        ('none','无Raid'),
    )
    # 服务器的基本情况

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=50, unique=True,verbose_name='主机名称')
    manufactor = models.CharField(
        max_length=50, choices=VENDOR_CHOICES, blank=True,verbose_name='制造商')
    serial_number = models.CharField(max_length=50, blank=True,verbose_name='序列号')
    model = models.CharField(max_length=50, blank=True,verbose_name='主机型号')
    warranty = models.BooleanField(verbose_name='是否在保')

    # 网卡相关

    nerwork_adapter_speed = models.CharField(
        max_length=50, choices=NETWORK_ADAPTER_SPEED_CHOICES, blank=True,verbose_name='网卡速率')
    network_adapters = models.PositiveSmallIntegerField(blank=True,verbose_name='网卡数量')

    # 运算相关

    processor_type = models.CharField(max_length=50, blank=True,verbose_name='处理器型号')
    logical_processors = models.PositiveSmallIntegerField(blank=True,verbose_name='逻辑处理器数量')
    memory = models.PositiveSmallIntegerField(blank=True,verbose_name='内存大小')
    max_memory = models.PositiveSmallIntegerField(blank=True,verbose_name='最大内存容量')

    #存储相关
    hard_disk_counts = models.PositiveSmallIntegerField(blank=True,verbose_name='磁盘数量')
    raid_type = models.CharField(max_length=50,choices=RAID_TYPE_CHOICES,blank=True,verbose_name='RAID类型')

    #管理相关
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    def __str__(self):
        return self.host_name
