from django.shortcuts import render, get_object_or_404, redirect
from cv.models import Item, CV, Category
from .forms import CVForm, ItemForm, CategoryForm

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/cv/')

    items = Item.objects.all()
    return render(request, 'cv/home.html', {'items': items})

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