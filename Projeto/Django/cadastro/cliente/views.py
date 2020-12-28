from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
	if request.method == "POST":
		username = request.POST['username']
		nome = request.POST['nome']
		endereço = request.POST['endereço']
		telefone = request.POST['telefone']
		data_de_nascimento=request.POST['data_de_nascimento']

		cliente = UserManager._create_user(username=username,telefone = telefone,nome = nome,endereço = endereço,data_de_nascimento=data_de_nascimento)
		cliente.save();
		print('criou')
		return redirect('/')
	else:
		return render(request, 'register.html')