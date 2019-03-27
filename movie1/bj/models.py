from django.db import models

class nuoMi_db(models.Model):
     movie_name = models.CharField(max_length=30)
     adress_name = models.CharField(max_length=100)
     wan_name = models.CharField(max_length=100)

class taopp_db(models.Model):
    movie_name = models.CharField(max_length=30)
    adress_name = models.CharField(max_length=20)
    wan_name = models.CharField(max_length=100)

class catEye_db(models.Model):
    movie_name = models.CharField(max_length=30)
    adress_name = models.CharField(max_length=20)
    wan_name = models.CharField(max_length=100)
class Users(models.Model):
    u_name = models.CharField(max_length=10)
    u_password = models.CharField(max_length=255)
    u_ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'bj_user'