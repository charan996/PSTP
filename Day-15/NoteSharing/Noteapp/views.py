from django.shortcuts import render,redirect
from Noteapp.forms import UsForm
# Create your views here.
def home(re):
	return render(re,'html/home.html')
def about(re):
	return render(re,'html/about.html')
def contact(re):
	return render(re,'html/contact.html')
def regi(re):
	if re.method=="POST":
		a=UsForm(re.POST)
		if a.is_valid():
			a.save()
			return redirect('/lg')
	a=UsForm()
	return render(re,'html/register.html',{'u':a})
def dashboard(re):
	return render(re,'html/dashboard.html')