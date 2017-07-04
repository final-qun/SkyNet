from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogPost(models.Model):
    title = models.CharField('标题',max_length=150)
    body = models.TextField('正文')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    status = models.CharField('文章状态',max_length=1,)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('喜欢', default=0)
    praises = models.PositiveIntegerField('点赞', default=0)
    category = models.ForeignKey('Category',verbose_name='分类',null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-create_time',)

class Category(models.Model):
    names = models.CharField('类型名称',max_length=20)
    create_time = models.DateTimeField('创建s时间',auto_now_add=True)

    def __str__(self):
        return self.names


class BlogComment(models.Model):
    username = models.CharField('评论者姓名',max_length=100)
    email = models.EmailField

class User(AbstractUser):
    pass
