from django.db import models


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=100, blank=False)
    register_date = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    user_role = models.ManyToManyField(Roles)
    is_active = models.BooleanField(default=True)
    last_otp_code = models.CharField(max_length=20, null=True)
    last_otp_expire = models.DateTimeField(null=True)
    last_otp_create_time = models.DateTimeField(null=True)


class UserLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    log_date = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length=255, null=True)
    device_ip = models.CharField(max_length=15, null=True)
    device_user_agent = models.CharField(max_length=255, null=True)
    otp_code = models.CharField(max_length=20, null=False)
    otp_expire = models.DateTimeField(null=False)
