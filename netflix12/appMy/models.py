from django.db import models

# Create your models here.


class Category(models.Model):
    titles = models.CharField(("Başlıks"), max_length=50)
    def __str__(self):
        return self.titles


class Video(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    image = models.ImageField(("Resim"), upload_to='img/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isnew = models.BooleanField(("Yeni mi?"), default=False)
    def __str__(self):
        return self.title