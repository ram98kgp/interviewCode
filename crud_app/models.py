from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50,null = True)
    age = models.IntegerField(null = True)
    address = models.TextField(null = True, blank = True)

    class Meta:
        db_table = "testAPP"
    
    def toDict(self):
        data = {}
        try:
            if(self.name):
                data["name"] = self.name
            if(self.age):
                data["age"] = self.age
            if(self.address):
                data["address"] = self.address
            return data
        except:
            return {}
        


# Create your models here.
