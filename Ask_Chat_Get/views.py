from django.shortcuts import render
from Ask_Chat_Get.models import Ask,GET
from userauthentification.models import Profile


def index(request):
    user = request.user
    posts = Ask.objects.all()
    profile = Profile.objects.get(user=user)
    profiles = Profile.objects.all()

    
    context= {
        'profile': profile,
        'profiles': profiles,
        'post_items':posts,
        'user': user,

    }
    

    
    return render(request,"index-ask.html",context)

def ans(request, ask_id):
    user = request.user
    que = Ask.objects.get(id = ask_id)
    profile = Profile.objects.get(user=user)
    profiles = Profile.objects.all()
    get = GET.objects.filter(ask = que)
    
    
    context= {
        'profile': profile,
        'profiles': profiles,
        'ask':que,
        'post_items' : get,
        'user': user,

    }
    

    
    return render(request,"index-ans.html",context)

