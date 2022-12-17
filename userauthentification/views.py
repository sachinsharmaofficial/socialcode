from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import resolve
from post.models import Post, Follow, Stream
from userauthentification.models import Profile
from post.models import Follow
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from userauthentification.forms import EditProfileForm
from django.contrib.auth import authenticate, login, logout
from userauthentification.models import UserOTP
from django.contrib import messages

import random
from django.core.mail import send_mail
from django.conf import settings


def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    profiles = Profile.objects.all()
    url_name = resolve(request.path).url_name
    
    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        posts = user.profile.favourite.all()
        
    # Profile Stats
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()
    
    # Follow
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()
    
    # pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {    
        'profile':profile,
        'posts': posts,
        'posts_paginator':posts_paginator,
        'url_name': url_name,
        'posts_count':posts_count,
        'following_count':following_count,
        'followers_count':followers_count,
        'follow_status' : follow_status,
        'profiles' : profiles,
        
        
    }
    return render(request, 'profile.html', context)    


def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=request.user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)[:25]
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=request.user, date=post.posted, following=following)
                    stream.save()
        return HttpResponseRedirect(reverse('profile', args=[username]))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))

def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.image = form.cleaned_data.get('image')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile', profile.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'form':form,
    }
    return render(request, 'edit-profile.html', context)

def sign(request):
    return render(request,"test.html") 

def signup(request):
    if request.method == "POST":
        
        
        getotp= request.POST.get('otp')
        if getotp:
            get_usr = request.POST.get('name')
            print("this is get_usr ", get_usr)
            user = User.objects.get(username=get_usr)
            
            if int(getotp) == UserOTP.objects.filter(user = user).last().otp:
                print("Hit getotp")
                user.is_active = True
                user.save()
                messages.success(request, f'Account is Created For {user.username}')
                
                return redirect('sign')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'user/signup.html', {'otp': True, 'usr': user})
        
        username = request.POST["Name"]
        First_name = request.POST["fname"]
        Last_name = request.POST["lname"]
        Email = request.POST["Email"]
        password = request.POST["Password"]

        if User.objects.filter(username=username):
            return render(request,'test.html')

        user = User.objects.create_user(username,Email,password)
        user.is_active = False
        user.save()

        profile = Profile.objects.create(user=user,first_name=First_name,last_name=Last_name)
        profile.save()
        f = Follow.objects.create(follower = user,following = user) 
        
        f.save()
        
        # OTP
        user_otp = random.randint(111111, 999999)
        
        UserOTP.objects.create(user = user, otp = user_otp)
        
        message = f"Hello {user.first_name} Thank You for signing in to Social Code \n\n Your OTP for Signing in verify YOur Account is {user_otp}"
        


        messages.success(request,"Your Account has been sussfully saved.")
        
        # send_mail(
        #     "Welcome  to Social Code - Please Verify Your Mail",
        #     message, settings.EMAIL_HOST_USER,
        #     [user.email],
        #     fail_silently = False
        # )
        send_mail(
            subject= 'Welcome  to Social Code - Please Verify Your Mail',
            message=message,
            from_email= 'team.socialcode@outlook.com',
            recipient_list=[user.email],
            fail_silently= False,
            
            auth_password= 'Ullu_Gang',
        )
        
       
        return render(request,"test.html", {'otp': True, 'user': user})
        # return redirect("home")
    
    else:
        return redirect("/sign")   

def signin(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        Email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password,email = Email)

        if user is not None:
            login(request, user)
            name = user.first_name
            messages.success(request,"Successfully Loged In")
            # return render(request, "index.html",{'fname': name})
            return redirect("index")
            
        else:
            messages.error(request, "Bad Credentials")
            return redirect("/sign")

    else:
        return render(request,"test.html")
        # return redirect("/")

def outout(request):
    logout(request)
    return redirect('sign')
