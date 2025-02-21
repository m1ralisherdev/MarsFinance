from django.db import models

# Create your models here.


class Xodimlar(models.Model):
    full_name = models.CharField(max_length=255)
    user_id = models.BigIntegerField(unique=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class ExcelModel(models.Model):
    file = models.FileField(upload_to='uploads/')

    CHOISE = (
         ("Yanvar","Yanvar"),
         ("Fevral", "Fevral"),
         ("Mart","Mart"),
         ("Aprel","Aprel"),
         ("May","May"),
        ("Iyun", "Iyun"),
        ("Iyul", "Iyul"),
        ("Avgust", "Avgust"),
        ("Sentabr", "Sentabr"),
        ("Oktabr", "Oktabr"),
        ("Noyabr", "Noyabr"),
        ('Dekabr', "Dekabr"),




    )
    month = models.CharField(choices=CHOISE,max_length=30,unique=True)
