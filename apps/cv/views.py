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
    return render(request, 'cv/edit_category.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            categories = Category.objects.all()
            form = CVForm()
            return redirect('/cv/edit', {'categories': categories, 'form': form})
    else:
        form = CategoryForm(instance=category)
    return render(request, 'cv/edit_category.html', {'form': form})

@login_required
def category_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('/cv/edit')


@login_required
def item_new(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.category = category
            item.save()
            url = '/cv/category/'+str(item.category.pk)+'/list/'
            return redirect(url)
    else:
        form = ItemForm()
    return render(request, 'cv/edit_item.html', {'form': form, 'category': category})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            url = '/cv/category/'+str(item.category.pk)+'/list/'
            return redirect(url)
    else:
        form = ItemForm(instance=item)
    return render(request, 'cv/edit_item.html', {'form': form})

@login_required
def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    url = '/cv/category/'+str(item.category.pk)+'/list/'
    return redirect(url)

@login_required
def item_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'cv/item_list.html', {'category': category})