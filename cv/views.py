from django.shortcuts import render, get_object_or_404, redirect
from cv.models import Item, CV, Category
from .forms import CVForm, CoreSkillForm

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/cv/')

    items = Item.objects.all()
    return render(request, 'cv/home.html', {'items': items})

def edit_page(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/cv/', pk=post.pk)
    else:
        form = CVForm()
    return render(request, 'cv/edit.html', {'form': form})

def add_core_skill(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CoreSkillForm(request.POST)
        if form.is_valid():
            core_skill = form.save(commit=False)
            core_skill.category = category
            core_skill.save()
            return redirect('edit_page', pk=category.pk)
    else:
        form = CoreSkillForm()
    return render(request, 'cv/add_core_skill.html', {'form': form})