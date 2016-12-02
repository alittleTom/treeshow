from django.db import models

# Create your models here.
class rwd_kmk_cjhz(models.Model):
    mingxi=models.CharField(max_length=50,primary_key=True)
    huizong1=models.CharField(max_length=50,primary_key=True)
    huizong2=models.CharField(max_length=50,primary_key=True)
    kemu=models.CharField(max_length=50,primary_key=True)
    leixing=models.IntegerField()
    shujuyuan=models.CharField(max_length=50)
    酬金名称=models.CharField(max_length=50,null=True,blank=True)
    酬金结果表=models.CharField(max_length=50,null=True,blank=True)
    存储过程=models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        db_table=('rwd_kmk_cjhz')

