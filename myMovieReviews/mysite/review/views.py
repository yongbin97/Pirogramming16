from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .form import PostForm

def review_list(request):
    reviews = Review.objects.all()
    ctx = {'reviews': reviews}

    return render(request, template_name = 'list.html', context = ctx)

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    ctx = {'review': review}
    return render(request, template_name='detail.html', context = ctx)

def review_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('review:list')
    
    else:
        form = PostForm()
        ctx = {'form': form}
        return render(request, template_name = 'update.html', context =ctx)


def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
        return redirect('review:detail', pk)
    
    else:
        form = PostForm(instance=review)
        ctx = {'form': form}

        return render(request, template_name='update.html', context=ctx)

def review_delete(request, pk):
    review = get_object_or_404(Review, id=pk)
    review.delete()

    return redirect('review:list')