from django.db import models

class UserRegister(models.Model):

    phone = models.CharField(max_length=11,verbose_name="注册手机号")
    password = models.CharField(max_length=128,verbose_name="用户密码")

    class Meta:
        db_table = "user_register"

        verbose_name = "用户注册表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone

class UserCenter(models.Model):

    nick_name = models.CharField
