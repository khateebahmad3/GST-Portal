import datetime

from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Registration, ReturnInfo

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs = {
			'id': 'unm',
			'placeholder': 'Enter Username',
			'name': 'username',
			'ng-model': 'username',
			'tabindex': '1',
			'autofocus': 'autofocus',
		}
	))
	password = forms.CharField(max_length=128, widget=forms.PasswordInput(
		attrs = {
			'id': 'txtPassword',
			'placeholder': 'Enter Password',
			'name': 'password',
			'ng-model': 'password',
			'tabindex': '2',
		}
	))

REGSTATUS = (
	('', 'Select'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
)

class RegistrationForm(forms.ModelForm):
	trn = forms.CharField(max_length=20)
	name = forms.CharField(max_length=150)
	email = forms.EmailField()
	epassword = forms.CharField(max_length=128, widget=forms.PasswordInput())
	phone_number = forms.CharField(max_length=10)
	status = forms.ChoiceField(choices = REGSTATUS)
	gstin = forms.CharField(max_length=50, required=False)
	username = forms.CharField(max_length=150, required=False)
	upassword = forms.CharField(max_length=128, widget=forms.PasswordInput(), required=False)

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['trn'].widget.attrs.update({
		    'id':'trn',
		    'placeholder':'Enter client TRN',
		    'name':'trn'})
		self.fields['name'].widget.attrs.update({
		    'id':'name',
		    'placeholder':'Enter client Name',
		    'name':'cname',})
		self.fields['email'].widget.attrs.update({
		    'id':'emailid',
		    'placeholder':'Enter client Email ID',
		    'name':'email'})
		self.fields['epassword'].widget.attrs.update({
		    'id':'epassword',
		    'placeholder':'Enter client Email Password',
		    'name':'epassword'})
		self.fields['phone_number'].widget.attrs.update({
		    'id':'mob',
		    'placeholder':'Enter client contact number',
		    'name':'mob',
		    'onfocus':'cnumber(this.id)'})
		self.fields['status'].widget.attrs.update({
		    'id':'status',
		    'name':'status',
		    'onchange':'makeVisible()'})
		self.fields['gstin'].widget.attrs.update({
		    'id':'gstin',
		    'placeholder':'Enter client GSTIN',
		    'name':'gstin'})
		self.fields['username'].widget.attrs.update({
		    'id':'unm',
		    'placeholder':'Enter client Username',
		    'name':'username'})
		self.fields['upassword'].widget.attrs.update({
		    'id':'upassword',
		    'placeholder':'Enter client username password',
		    'name':'upassword'})

	class Meta:
		model = Registration
		fields = (
			'trn',
			'name',
			'email',
			'epassword',
			'phone_number',
			'status',
			'gstin',
			'username',
			'upassword',
		)

RETSTATUS = (
	('', 'Select'),
    ('Not Filed', 'Not Filed'),
    ('Filed', 'Filed'),
)
MONTHS = (
	('', 'Select'),
	('January', 'January'),
	('February', 'February'),
	('March', 'March'),
	('April', 'April'),
	('May', 'May'),
	('June', 'June'),
	('July', 'July'),
	('August', 'August'),
	('September', 'September'),
	('October', 'October'),
	('November', 'November'),
	('December', 'December'),
)

def currMonth():
	months = [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December'
	]
	today = datetime.datetime.now()
	month = months[today.month-2]
	return month

class ReturnsForm(forms.ModelForm):
	name = forms.CharField(max_length=150)
	username = forms.CharField(max_length=150)
	upassword = forms.CharField(max_length=128, widget=forms.PasswordInput())
	phone_number = forms.CharField(max_length=10)
	email = forms.EmailField(required=False)
	epassword = forms.CharField(max_length=128, widget=forms.PasswordInput(), required=False)
	month = forms.ChoiceField(choices=MONTHS, initial=currMonth)
	status = forms.ChoiceField(choices=RETSTATUS)
	
	def __init__(self, *args, **kwargs):
		super(ReturnsForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
		    'id':'name',
		    'placeholder':'Enter client Name',
		    'name':'cname',
		    'autofocus': 'autofocus'})
		self.fields['username'].widget.attrs.update({
		    'id':'unm',
		    'placeholder':'Enter client Username',
		    'name':'username'})
		self.fields['upassword'].widget.attrs.update({
		    'id':'upassword',
		    'placeholder':'Enter client username password',
		    'name':'upassword'})
		self.fields['phone_number'].widget.attrs.update({
		    'id':'mob',
		    'placeholder':'Enter client contact number',
		    'name':'mob',
		    'onfocus':'cnumber(this.id)'})
		self.fields['email'].widget.attrs.update({
		    'id':'emailid',
		    'placeholder':'Enter client Email ID',
		    'name':'email'})
		self.fields['epassword'].widget.attrs.update({
		    'id':'epassword',
		    'placeholder':'Enter client Email Password',
		    'name':'epassword'})
		self.fields['month'].widget.attrs.update({
		    'id':'month',
		    'name':'month'})
		self.fields['status'].widget.attrs.update({
		    'id':'status',
		    'name':'status'})

	class Meta:
		model = ReturnInfo
		fields = (
			'name',
			'username',
			'upassword',
			'phone_number',
			'email',
			'epassword',
			'month',
			'status',			
		)

class EditRegForm(forms.ModelForm):
	trn = forms.CharField(max_length=20, required=False)
	name = forms.CharField(max_length=150, required=False)
	email = forms.EmailField(required=False)
	epassword = forms.CharField(max_length=128, required=False)
	phone_number = forms.CharField(max_length=10, required=False)
	status = forms.ChoiceField(choices = REGSTATUS)
	gstin = forms.CharField(max_length=50, required=False)
	username = forms.CharField(max_length=150, required=False)
	upassword = forms.CharField(max_length=128, required=False)

	def __init__(self, *args, **kwargs):
		super(EditRegForm, self).__init__(*args, **kwargs)
		self.fields['trn'].widget.attrs.update({
		    'id':'trn',
		    'placeholder':'Enter client TRN',
		    'name':'trn',
		    'readonly':'true',})
		self.fields['name'].widget.attrs.update({
		    'id':'name',
		    'placeholder':'Enter client Name',
		    'name':'cname',
		    'readonly':'true',})
		self.fields['email'].widget.attrs.update({
		    'id':'emailid',
		    'placeholder':'Enter client Email ID',
		    'name':'email',
		    'readonly':'true',})
		self.fields['epassword'].widget.attrs.update({
		    'id':'epassword',
		    'placeholder':'Enter client Email Password',
		    'name':'epassword',
		    'readonly':'true',})
		self.fields['phone_number'].widget.attrs.update({
		    'id':'mob',
		    'placeholder':'Enter client contact number',
		    'name':'mob',
		    'onfocus':'cnumber(this.id)',
		    'readonly':'true',})
		self.fields['status'].widget.attrs.update({
		    'id':'status',
		    'name':'status',
		    'onchange':'makeVisible()'})
		self.fields['gstin'].widget.attrs.update({
		    'id':'gstin',
		    'placeholder':'Enter client GSTIN',
		    'name':'gstin',
		    'readonly':'True',})
		self.fields['username'].widget.attrs.update({
		    'id':'unm',
		    'placeholder':'Enter client Username',
		    'name':'username',
		    'readonly':'True',})
		self.fields['upassword'].widget.attrs.update({
		    'id':'upassword',
		    'placeholder':'Enter client username password',
		    'name':'upassword',})
	class Meta:
		model = Registration
		fields = (
			'trn',
			'name',
			'email',
			'epassword',
			'phone_number',
			'status',
			'gstin',
			'username',
			'upassword',
		)

class EditRetForm(forms.ModelForm):
	name = forms.CharField(max_length=150, required=False)
	username = forms.CharField(max_length=150, required=False)
	upassword = forms.CharField(max_length=128, required=False)
	phone_number = forms.CharField(max_length=10, required=False)
	email = forms.EmailField(required=False)
	epassword = forms.CharField(max_length=128, required=False)
	month = forms.ChoiceField(choices=MONTHS, required=False)
	status = forms.ChoiceField(choices=RETSTATUS)
	
	def __init__(self, *args, **kwargs):
		super(EditRetForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
		    'id':'name',
		    'placeholder':'Enter client Name',
		    'name':'cname',
		    'autofocus': 'autofocus'})
		self.fields['username'].widget.attrs.update({
		    'id':'unm',
		    'placeholder':'Enter client Username',
		    'name':'username'})
		self.fields['upassword'].widget.attrs.update({
		    'id':'upassword',
		    'placeholder':'Enter client username password',
		    'name':'upassword'})
		self.fields['phone_number'].widget.attrs.update({
		    'id':'mob',
		    'placeholder':'Enter client contact number',
		    'name':'mob',
		    'onfocus':'cnumber(this.id)'})
		self.fields['email'].widget.attrs.update({
		    'id':'emailid',
		    'placeholder':'Enter client Email ID',
		    'name':'email'})
		self.fields['epassword'].widget.attrs.update({
		    'id':'epassword',
		    'placeholder':'Enter client Email Password',
		    'name':'epassword'})
		self.fields['month'].widget.attrs.update({
		    'id':'month',
		    'name':'month'})
		self.fields['status'].widget.attrs.update({
		    'id':'status',
		    'name':'status'})

	class Meta:
		model = ReturnInfo
		fields = (
			'name',
			'username',
			'upassword',
			'phone_number',
			'email',
			'epassword',
			'month',
			'status',			
		)