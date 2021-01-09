from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank = True) #You don't necessarily need this.

    def __str__(self):  #returns actual info when accessing object instead of object(1)
        return self.title
