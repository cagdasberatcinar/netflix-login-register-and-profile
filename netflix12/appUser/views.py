from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from appUser.models import *

# Create your views here.

def profilePage(request):
    context = {}
    profile_list = Profile.objects.filter(user=request.user, isview=True)
    profile_delete_list = Profile.objects.filter(user=request.user, isview=False)
# olan profil adı varsa ve silinmişte tekrar eski profilini getirmel ister misin yoksa yenisi mi oluşsun
    if request.method == "POST":
        submit = request.POST.get("submit")
        title = request.POST.get("title")
        image = request.FILES.get("image")
        if submit == "profileCreate":
            if len(profile_list) < 4:

                if title and image:
                    
                    if profile_delete_list.filter(title=title).exists(): # silinen profil olup olmadığını tespit et
                        context.update({"is_delete_title":True, "title":title, "image":image})
                        profile = Profile(title=title,image=image,user=request.user, isview=False, isnew=True) # aynı isme sahip yeni profil
                        profile.save()
                        
                    else:
                        profile = Profile(title=title,image=image,user=request.user)
                        profile.save()
                        return redirect("profilePage")
                    
                else:
                    messages.warning(request, "Boş bırakılan yerler var")
        elif submit == "newProfileCreate":
            profiledelete = profile_delete_list.get(title=title, isnew=False) # aynı isme sahip eski profil
            profiledelete.delete()
            profile = Profile.objects.get(user=request.user, isnew=True) # yeni oluşturduğumuz profili getir.
            profile.isnew = False
            profile.isview = True
            profile.save()            
            return redirect("profilePage")
        elif submit == "oldProfileCreate":
            profil = Profile.objects.get(title=title,isnew=True)
            profil.delete()
            
            profiledelete = profile_delete_list.get(title=title,isnew=False)
            profiledelete.isview = True
            profiledelete.save()
            return redirect("profilePage")
        
        elif submit == "profileUpdate":
            if title and image:
                profileid = request.POST.get("profileid")
                profile = Profile.objects.get(user=request.user, id=profileid)
                if title:
                    profile.title = title
                if image:
                    profile.image = image
                profile.save()
                return redirect("profilePage")
            
    context.update({
        "profile_list": profile_list,
    })
    return render(request, "profile.html", context)

def profileDelete(request, pid):
    profile = Profile.objects.get(user=request.user, id=pid)
    profile.isview = False
    profile.save()
    return redirect("profilePage")

#=============

def profileLogin(request,pid):
    profile_list = Profile.objects.filter(user=request.user) # kullanıcınını tüm profilleri
    profile_list.update(islogin=False) # tüm listedeki islogin False olsun
    
    profile = Profile.objects.get(user=request.user, id=pid) # tıklanan profil
    profile.islogin = True # tıklanan profili girişli olarak ayarla
    profile.save() # kaydet
    return redirect('browseindexPage')
#=============
def hesapPage(request):
    context = {}
    return render(request, "hesap.html", context)

def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        rememberme = request.POST.get("rememberme")
    
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            
            if rememberme:
                request.session.set_expiry(604800) # beni 1 hafta boyunca hatırla
            
            return redirect("profilePage")
        else:
            messages.error(request, "Kullanıcı Adı veya Şifre Yanlış.")

    
    context = {}
    return render(request, "user/login.html", context)

def registerPage(request):
    
    context = {}
    
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        site = request.POST.get("check-site")
        kvkk = request.POST.get("check-kvkk")
        
        if fname and lname and username and email and password1 and site and kvkk:
            if password1 == password2:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        num_bool = up_bool = False
                        # password control
                        for k in password1: # => asd123
                            if k.isnumeric(): num_bool = True
                            if k.isupper(): up_bool = True


                        if len(password1)>= 8 and num_bool and up_bool:
                            # kayıt edilebilir
                            user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password1 )
                            user.save()
                            return redirect("loginPage")
                        else:
                            messages.error(request, "Şifrenizin 8 veya daha uzun olması gerekiyor.")
                            messages.error(request, "Şifrenizde en az bir rakam olması gerekiyor.")
                            messages.error(request, "Şifrenizde en az bir büyük harf olması gerekiyor.")
                    else:
                        messages.error(request, "Bu email zaten kullanılıyor.")
                else:
                    messages.error(request, "Kullanıcı adı daha önceden alınmış.")
            else:
             messages.error(request, "Şifreler Aynı Değil !!")    
        else:
             messages.warning(request, "Boş bırakılan yerleri lütfen doldurunuz.")
             context.update({
                 "fname":fname,"lname":lname,"username":username,"email":email
                 })

    return render(request, "user/register.html", context)


