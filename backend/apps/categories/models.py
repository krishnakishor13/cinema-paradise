from django.db import models

class Category(models.Model):
    class Meta(object):
        db_table="category"
    name= models.CharField(
        "Name", blank= False, null= False, max_length= 50
    )
    created_at= models.DateTimeField(
        "Created DateTime", blank= True, auto_now_add= True
    )
    updated_at= models.DateTimeField(
        "Updated DateTime", blank= True, auto_now= True
    )

    def __str__(self):
        return self.name