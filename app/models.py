from django.db import models

class Person(models.Model):
    name    = models.CharField(max_length = 200)
    age     = models.IntegerField()
    type    = models.CharField(max_length = 200, choices= (('FN', 'FN'), ('LN','LN')))
    
    def __str__(self):
        return self.name
    

class OtherName(models.Model):
    person  = models.ForeignKey(Person)
    name  = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name