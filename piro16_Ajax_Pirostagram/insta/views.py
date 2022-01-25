from django.shortcuts import render
import json
from .models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts
    }
    return render(request, 'home.html', ctx)


@csrf_exempt
def like(request):
    req = json.loads(request.body)
    id = req['id']
    type = req['type']
    post = Post.objects.get(id = id)

    if type == 'like':
        post.like += 1
    else:
        post.like -= 1
    post.save()
    return JsonResponse({'id': id, 'type': type})

