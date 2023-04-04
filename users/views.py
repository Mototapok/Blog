from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""регистрирует нового пользователя"""
	if request.method !='POST':
		# выводит пустую форму регистрации
		form = UserCreationForm()
	else:
		# Обработка заполненной формы
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# выполнение входа и перенаправление на домашнюю страницу
			login(request, new_user)
			return redirect('blogs:index')

	# вывести пустую или не действительную форму
	context = {'form': form}
	return render(request, 'registration/register.html', context)
