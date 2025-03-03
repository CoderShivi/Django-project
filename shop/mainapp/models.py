from django.db import models
# Create your models here.
# Now let's create the shema for our project
# Any time we make any change in the class definitions, especially the variables,
# We need to run two commands.
# 1. Python manage.py makemigrations
#       -> This generates python scripts inside the app's migrations folder.
#       -> it will track the models.py and check for changes.
#       -> Necessary DDL statements will be generated to be sent to the DB
# 2. python manage.py migrate
#       -> It executes the scripts, thereby running the DD: operations.

class Product(models.Model):
    # list out all the object variable below and initialize with certain classes.
    # For the classes to use for initialize the attributes.
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(null=False)
    desc = models.TextField()
    pic = models.ImageField(upload_to='products/', null=False)
    stock=models.PositiveBigIntegerField(default=1)


