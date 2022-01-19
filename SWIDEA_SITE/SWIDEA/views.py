from http.client import HTTPResponse
from pickle import NONE
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import json
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def idea_list(request):
    ideaList = Idea.objects.all()
    ctx = {'ideaList': ideaList}
    return render(request, 'SWIDEA/idea_list.html', ctx)


def idea_detail(request, pk):
    idea = Idea.objects.get(pk=pk)
    ctx = {'idea': idea}
    return render(request, 'SWIDEA/idea_detail.html', ctx)


def idea_new(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            new_idea = form.save()
            return idea_detail(request, new_idea.pk)
    else:
        form = IdeaForm()
    
    ctx = {'form': form}
    return render(request, 'SWIDEA/idea_new.html', context=ctx)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return idea_detail(request, idea.pk)
    
    else:
        form = IdeaForm(instance=idea)
        ctx = {'form': form}

        return render(request, 'SWIDEA/idea_update.html', context=ctx)

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()

    return redirect('SWIDEA:idea_list')

    ###########################################################################################################

def dev_list(request):
    devList = Develop.objects.all()
    ctx = {'devList': devList}
    return render(request, 'SWIDEA/dev_list.html', ctx)

def dev_detail(request, pk):
    dev = Develop.objects.get(pk=pk)
    idea = Idea.objects.all().filter(develop=dev)
    ctx = {'dev': dev, 'idea': idea}
    return render(request, 'SWIDEA/dev_detail.html', ctx)


def dev_new(request):
    if request.method == "POST":
        form = DevelopForm(request.POST)
        if form.is_valid():
            new_dev = form.save()
            return dev_detail(request, new_dev.pk)
    else:
        form = DevelopForm()
    
    ctx = {'form': form}
    return render(request, 'SWIDEA/dev_new.html', context=ctx)

def dev_update(request, pk):
    dev = get_object_or_404(Develop, pk=pk)
    
    if request.method == "POST":
        form = DevelopForm(request.POST, instance=dev)
        if form.is_valid():
            dev = form.save(commit=False)
            dev.save()
            return dev_detail(request, dev.pk)
    
    else:
        form = DevelopForm(instance=dev)
        ctx = {'form': form}

        return render(request, 'SWIDEA/dev_update.html', context=ctx)

def dev_delete(request, pk):
    dev = get_object_or_404(Develop, pk=pk)
    dev.delete()

    return redirect('SWIDEA:dev_list')


###############################################################################

def idea_plus(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)

    idea.rate += 1
    idea.save()

    ctx = {'idea_rate': idea.rate}
    return JsonResponse(ctx)




def idea_minus(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)

    idea.rate -= 1
    idea.save()

    ctx = {'idea_rate': idea.rate}
    return JsonResponse(ctx)
