from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Category

class Movie(models.Model):
    MY_CHOICES= (
        ("Newly Released", "Newly Released"), ("Upcoming Movies", "Upcoming Movies")
    )
    class Meta(object):
        db_table='movie'
    name= models.CharField(
        "Name", blank= False, null= False, max_length= 50
    )
    description= models.TextField(
        "Description", blank= False, null= False, max_length= 500
    )
    movie_duration= models.IntegerField(
        "Movie Duration", blank= False, null= False, default= 60
    )
    image= CloudinaryField(
        "Image", blank= False, null= False
    )
    trailer_link= models.URLField(
        "Trailer Link", blank= False, null= False
    )
    category_id= models.ForeignKey(
        Category, on_delete= models.CASCADE
    )
    state= models.CharField(
        "State", blank= False, null= False, max_length= 50
    )
    ratings= models.IntegerField(
        "Rating", blank= False, null= False
    )
    release_type= models.CharField(
        "Released Type", blank= False, null= False, max_length= 50, choices= MY_CHOICES
    )
    released_date= models.IntegerField(
        "Released Date", blank= False, null= False
    )
    created_at= models.DateTimeField(
        "Created At", blank= False, null= False, auto_now_add=True
    )
    updated_at= models. DateTimeField(
        "Updated At", blank= False, null= False, auto_now=True
    )