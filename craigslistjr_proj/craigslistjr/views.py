from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from .models import Category, Post
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def index(request):
    categories = Category.objects.all()
    return render(request, 'craigslistjr/index.html', {"categories":categories})

def cat_view(request, category_id):
    cat_posts= Post.objects.filter(category_id=category_id)
    cat= Category.objects.get(id=category_id)
    return render(request, 'craigslistjr/cat_view.html', {'posts': cat_posts, 'category':cat})

@csrf_exempt
def cat_new(request):
    if request.method == "POST":
        body = json.loads(request.body)
        newCat = Category(title = body["title"])
        newCat.save()
        return JsonResponse({})
    
    return render(request, 'craigslistjr/cat_new.html')

@csrf_exempt
def cat_edit(request, category_id):
    if request.method == "POST":
        body = json.loads(request.body)
        Category.objects.filter(id=body['id']).delete()
        return JsonResponse({})
    elif request.method == "PUT":
        body = json.loads(request.body)
        Category.objects.filter(id=category_id).update(title=body['title'])
        return JsonResponse({})
    cat=Category.objects.get(id=category_id)
    return render(request, 'craigslistjr/cat_edit.html',{'category':cat})

@csrf_exempt
def post_new(request, category_id):
    if request.method == "POST":
        body = json.loads(request.body)
        newPost = Post(title = body["title"], description = body["description"],posted_by  = body["posted_by"],email=body["email"], category_id = category_id)
        newPost.save()
        return JsonResponse({})
    cat=Category.objects.get(id=category_id)
    return render(request, 'craigslistjr/post_new.html', {'category':cat})

def post_view(request, category_id, post_id):
    post=  Post.objects.get(id = post_id)
    cat=Category.objects.get(id=category_id)
    return render(request, 'craigslistjr/post_view.html',{'category':cat,'post':post})

@csrf_exempt    
def post_edit(request, category_id, post_id):
    if request.method == "POST":
        body = json.loads(request.body)
        Post.objects.filter(id=body['id']).delete()
        return JsonResponse({})
    elif request.method == "PUT":
        body = json.loads(request.body)
        Post.objects.filter(id=post_id).update(title = body["title"], description = body["description"],posted_by  = body["posted_by"],email=body["email"])
        return JsonResponse({})
    cat=Category.objects.get(id=category_id)
    post=Post.objects.get(id=post_id)
    return render(request, 'craigslistjr/post_edit.html',{'category':cat,'post':post})

def handler404(request, exception):
    return render(request, "craigslistjr/404.html", {}) 


def handler500(request, exception=None):
    return render(request, "craigslistjr/404.html", {})




