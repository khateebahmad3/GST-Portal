from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core import serializers

from GST_Portal import settings
from .forms import LoginForm, RegistrationForm, ReturnsForm, EditRegForm, EditRetForm
from .models import Registration, ReturnInfo

def index(request):
	return render(request, 'gstinfo/index.html')

def testit(request):
	return render(request, 'gstinfo/test.html')

def log_in(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					if user.is_superuser:
						form = LoginForm()
						message = "Invalid Username/Password"
						args = {'form': form, 'message': message}
					else:
						request.session['loggedin'] = 'True'
						request.session.set_expiry(3600)
						login(request, user)
						return redirect(settings.LOGIN_REDIRECT_URL)
			else:
				form = LoginForm()
				message = "Invalid Username/Password"
				args = {'form': form, 'message': message}
	else:
		form = LoginForm()
		args = {'form': form}
	return render(request, 'gstinfo/login.html', args)

def updateregform(request, value=None):
	if sessioncheck(request) == True:
		if value is not None:
			client = Registration.objects.get(trn=value)
			if request.method == 'POST':
				form = EditRegForm(request.POST, instance=client)
				if form.is_valid():
					form.save()
					return redirect('/gst/user/registrations/')
				else:
					return HttpResponse("Failed")
			else:
				form = EditRegForm(instance = client)
				args={'form': form, 'client': client}
				return render(request, 'gstinfo/edit_registration.html', args)
		else:
			return redirect('/gst/user/registrations/')
	else:
		return redirect("gstinfo:sessionexpire")

def updateretform(request, month, value=None):
	if sessioncheck(request) == True:
		if value is not None:
			client = ReturnInfo.objects.get(username=value, month=month)
			if request.method == "POST":
				form = EditRetForm(request.POST, instance=client)
				if form.is_valid():
					form.save()
					return redirect('gstinfo:returns')
				else:
					return HttpResponse("Failed")
			else:
				form = EditRetForm(instance=client)
				args = {'form': form, 'client': client}
				return render(request, 'gstinfo/edit_return.html', args)
		else:
			return redirect('/gst/user/returns')
	else:
		return redirect("gstinfo:sessionexpire")

def success(request):
	if sessioncheck(request) == True:
		return render(request, 'gstinfo/user-dashboard.html')
	else:
		return redirect('gstinfo:sessionexpire')

def registrations(request):
	if sessioncheck(request) == True:
		reg = Registration.objects.all()
		if reg:
			num = Registration.objects.all().count()
			args = {'reg': reg, 'num': num}
			return render(request, 'gstinfo/registrations.html', args)
		else:
			return render(request, 'gstinfo/registrations.html', {'message': "No registrations data found"})
	else:
		return redirect('gstinfo:sessionexpire')

def returns(request):
	if sessioncheck(request) == True:
		returns = ReturnInfo.objects.all()
		if returns:
			num = ReturnInfo.objects.all().count()
			args = {'returns': returns, 'num': num}
			return render(request, 'gstinfo/returns.html', args)
		else:
			return render(request, 'gstinfo/returns.html', {'message': "No returns data found"})
	else:
		return redirect('gstinfo:sessionexpire')

def addform(request, operation):
	if sessioncheck(request) == True:
		if operation == "registrations":
			if request.method == 'POST':
				form = RegistrationForm(request.POST)
				if form.is_valid():
					form.save()
					return redirect('/gst/user/registrations/')
				else:
					message = "Error Occured!"
					args = {'form': form, 'message': message}
			else:
				form = RegistrationForm()
				args = {'form': form}
		elif operation == "returns":
			if request.method == 'POST':
				form = ReturnsForm(request.POST)
				if form.is_valid():
					form.save()
					return redirect('/gst/user/returns/')
				else:
					message = "Error Occured!"
					args = {'form': form, 'message': message}
			else:
				form = ReturnsForm()
				args = {'form': form}
		return render(request, 'gstinfo/addform.html', args)
	else:
		return redirect("gstinfo:sessionexpire")

def log_out(request):
	try:
		request.session.flush()
	except KeyError:
		pass
	return render(request, 'gstinfo/logout.html')

def sessioncheck(request):
	if request.session.has_key('loggedin'):
		return True
	else:
		return False

def sessionexpire(request):
	try:
		request.session.clear_expired()
	except KeyError:
		print("ERROR")
	return render(request, 'gstinfo/sessionexpired.html')

def getClients(request):
	reg = Registration.objects.all()
	reg_json = serializers.serialize('json', reg)
	return HttpResponse(reg_json, content_type='application/json')

def getReturns(request):
	ret = ReturnInfo.objects.all()
	ret_json = serializers.serialize('json', ret)
	return HttpResponse(ret_json, content_type='application/json')