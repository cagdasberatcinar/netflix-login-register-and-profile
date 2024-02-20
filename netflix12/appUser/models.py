from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=250)
    isview = models.BooleanField(("Görüntlüle"), default=True)
    isnew = models.BooleanField(("Silinen Yeni Profil mi?"), default=False) # yeni profil olup olmadığını anlamamızı sağlayacak
    islogin = models.BooleanField(("Girişli Profil"), default=False)
def __str__(self) -> str:
    return self.title
