from django.db import models

# Create your models here.
class requirement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    root = models.IntegerField(help_text='requirement root id')
    pre = models.IntegerField(help_text='requirement pre id')
    status = models.IntegerField(help_text="状态用数字表示")
    extend1 = models.CharField(max_length=50,help_text="备用1",null=True,blank=True)
    extend2 = models.CharField(max_length=50, help_text="备用2",null=True,blank=True)
    extend3 = models.CharField(max_length=50, help_text="备用3",null=True,blank=True)

    class Meta:
        db_table=('requirement2')
        verbose_name = '需求表'
        verbose_name_plural = '需求表'
        ordering = ['time']
    def __str__(self):
        return self.name

class test(models.Model):
    id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(requirement)
    name = models.CharField(max_length=50)
    doc = models.FileField(upload_to='./upload/yxtest3/test')#这个可以存路径或者用models.FileField(upload_to='./upload/')
    creator = models.CharField(max_length=20,help_text="负责人")#这个是否要关联人员表
    time = models.DateTimeField()
    status = models.IntegerField(help_text="状态用数字表示")
    extend1 = models.CharField(max_length=50, help_text="备用1",null=True,blank=True)
    extend2 = models.CharField(max_length=50, help_text="备用2",null=True,blank=True)
    extend3 = models.CharField(max_length=50, help_text="备用3",null=True,blank=True)

    class Meta:
        db_table = ('testtable2')
        verbose_name = '测试表'
        verbose_name_plural = '测试表'
        ordering = ['time']
    def __str__(self):
        return self.name

class scriptVersion(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(test)
    name = models.CharField(max_length=50)
    doc = models.FileField(upload_to='./upload/yxtest3/scriptVersion')  # 这个可以存路径或者用models.FileField(upload_to='./upload/')
    creator = models.CharField(max_length=20, help_text="负责人")  # 这个是否要关联人员表
    time = models.DateTimeField()
    remarks = models.CharField(max_length=200,help_text="备注内容")
    extend1 = models.CharField(max_length=50, help_text="备用1",null=True,blank=True)
    extend2 = models.CharField(max_length=50, help_text="备用2",null=True,blank=True)
    extend3 = models.CharField(max_length=50, help_text="备用3",null=True,blank=True)

    class Meta:
        db_table = ('scriptversion2')
        verbose_name = '脚本表'
        verbose_name_plural = '脚本表'
        ordering = ['time']
    def __str__(self):
        return self.name

