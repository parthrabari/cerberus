from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.views import generic
from django.views.generic import View

from .models import Table8
from .forms  import SignUp,Login

# Create your views here.

def index(request):
	return render(request,"base.html",{})

def lists(request):
	query_list   = Table8.objects.all()
    
	search = request.GET.get('Q')
	if search:
		query_list = query_list.filter(title__icontains=search)


	paginator = Paginator(query_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		query = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		query = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		query = paginator.page(paginator.num_pages)
	context = {
		'game_list':query,
	}
	return render(request,"lists.html",context)

#sign up and auto login
class UserSignUpView(View):
	form_class = SignUp
	template_name = 'form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			user = authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('listings:list')

def loginview(request):
	form = Login(request.POST or None)
	if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			login(request,user)
			return redirect('listings:list')
	
	return render(request,"form.html",{"form":form})
	

def logoutview(request):
	logout(request)
	return render(request,"logout.html",{})