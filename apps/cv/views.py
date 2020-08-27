from django.shortcuts import render, get_object_or_404, redirect
from apps.cv.models import Item, CV, Category
from .forms import CVForm, ItemForm, CategoryForm
from django.contrib.auth.decorators import login_required

def home_page(request):
    categories = Category.objects.all()
    cv = CV.objects.all()
    items = Item.objects.all()
    return render(request, 'cv/home.html', {'categories': categories, 'cv': cv, 'items': items})

@login_required
def edit_page(request):
    cvs = CV.objects.all()
    if cvs.count() == 0:
        cv = CV()
    else:
        cv = cvs.first()
    categories = Category.objects.all()
    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('/cv/', pk=cv.pk)
    else:
        form = CVForm(instance=cv)
    return render(request, 'cv/edit.html', {'categories': categories, 'form': form})

@login_required
def add_item(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            core_skill = form.save(commit=False)
            core_skill.category = category
            core_skill.save()
            categories = Category.objects.all()
            form = CVForm()
            return redirect('/cv/edit', {'categories': categories, 'form': form})
    else:
        form = ItemForm()
    return render(request, 'cv/add_item.html', {'form': form, 'category': category})

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            categories = Category.objects.all()
            form = CVForm()
            return redirect('/cv/edit', {'categories': categories, 'form': form})
    else:
        form = CategoryForm()
    return render(request, 'cv/add_category.html', {'form': form})