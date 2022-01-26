from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def main(request):
    posts = Post.objects.all()
    form = CommentForm
    ctx = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'main.html', ctx)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect('main')
    
    else:
        form = PostForm()
    
    ctx = {'form': form}
    return render(request, 'create.html', ctx)

@csrf_exempt
def like(request):
    req =json.loads(request.body)
    id = req['id']
    type = req['type']
    post = Post.objects.get(id = id)

    if type == 'like':
        post.status = 1
    elif  type == 'dislike':
        post.status = 0
    
    post.save()
    return JsonResponse({'id': id, 'type': type})

@csrf_exempt
def add_comment(request):
    req = json.loads(request.body)
    id = req['id']
    type = req['type']
    content = req['content']
    
    comment = Comment()
    comment.post = Post.objects.get(id = id)
    comment.content = content
    comment_id = comment.id
    comment.save()
    return JsonResponse({'id': id, 'type': type, 'content': content, 'comment-id': comment_id})

@csrf_exempt
def del_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']
    
    comment = get_object_or_404(Comment, id = comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id})