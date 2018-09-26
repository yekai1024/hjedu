from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class HJClass(models.Model):
    class_name = models.TextField("课程名称", max_length=32, unique=True)
    short_url = models.TextField("课程短网址", max_length=128)
    long_url = models.TextField("课程真实网址", max_length=256)
    in_use = models.BooleanField("使用中",  default=True)

    class Meta:
        verbose_name = "课程管理"
        verbose_name_plural = verbose_name