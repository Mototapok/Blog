from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

def  index(request):
	"""home page of blogs app, выводит список тем"""
	#blogs = BlogPost.objects.order_by('date_added')
	#context = {'blogs': blogs}
	#return render(request, 'blogs/index.html', context)
	return render(request, 'blogs/index.html')

@login_required
def  blogs(request):
	"""home page of blogs app, выводит список тем"""
	blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
	context = {'blogs': blogs}
	return render(request, 'blogs/blogs.html', context)

@login_required
def new_blog(request):
	"""определяет новый блог"""
	if request.method != 'POST':
		# данные не отправлялись; создается пустая форма
		form = BlogForm()	
	else:
		# Отправлены данные ПОСТ; обработать данные
		form = BlogForm(data=request.POST)
		if form.is_valid():
			new_blog = form.save(commit=False)
			new_blog.owner = request.user
			new_blog.save()
			return redirect('blogs:blogs') # перенаправляет на страницу index

	# вывести пустую или недействительную форму
	context = {'form': form}
	return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
	"""редактирует существующий блог"""
	
	blog = BlogPost.objects.get(id=blog_id)
	if blog.owner != request.user:
		return render(request, 'blogs/index.html') # отправляет на страницу index
		# raise Http404

	if request.method != 'POST':
		# Исходный запрос: форма заполняется данными текущей записи
		form = BlogForm(instance=blog)
		
	else:
		# Отправлены данные ПОСТ; обработать данные
		form = BlogForm(instance=blog, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:blogs')

	context = {'blog': blog, 'form': form}
	return render(request, 'blogs/edit.html', context)

