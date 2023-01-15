from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Doctors(models.Model):
    serial_no = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    tokens = models.CharField(max_length=300,blank=True,default="")
    current_token = models.CharField(max_length=10,blank=True,default="")
    next_token = models.CharField(max_length=10,blank=True,default="")


    class Meta:
        verbose_name_plural = "Doctors"

    def full_name(self):
        return f"{self.serial_no}.{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



