from django.db import models

class HJClass(models.Model):
    class_name = models.CharField("课程名称", max_length=32, unique=True)
    short_url = models.CharField("课程短网址", max_length=128)
    long_url = models.CharField("课程真实网址", max_length=256)
    in_use = models.BooleanField("使用中",  default=True)

    def __unicode__(self):
        return "%s" % self.class_name

    def __str__(self):
        return "%s" % self.class_name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name