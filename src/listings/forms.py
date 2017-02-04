from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,

)

User = get_user_model()
class SignUp(forms.ModelForm):
	password =forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model  = User
		fields = ['username','email','password']
	

class Login(forms.Form):
	username = forms.CharField()
	password =forms.CharField(widget = forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		if not user:
			raise forms.ValidationError("not a valid user")

		if not user.check_password(password):
			raise forms.ValidationError("wrong password")

		if not user.is_active:
			raise forms.ValidationError("User is inactive")

		return super(Login,self).clean(*args,**kwargs)

	
		