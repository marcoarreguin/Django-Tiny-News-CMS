#encoding:utf-8
from django.forms import ModelForm
from django import forms
from home.models import UserProfile, Audio, FotoCategoria, Foto, Video, ArticuloCategoria, Articulo, Banner, Diario, DiarioCategoria, Principal, Publicidad, Noticia
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.html import escape

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user')

class FotocatForm(ModelForm):
	class Meta:
		model = FotoCategoria

class AudioForm(ModelForm):
	mp3 = forms.FileField(label="Selecciona audio",widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	class Meta:
		model = Audio

class FotoForm(ModelForm):
	foto = forms.FileField(widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	class Meta:
		model = Foto

class VideoForm(ModelForm):
	class Meta:
		model = Video

class ArticuloForm(ModelForm):
	texto = forms.CharField(widget=forms.Textarea(attrs={'cols':'58', 'rows':'17'}))
	class Meta:
		model = Articulo

class NoticiaForm(ModelForm):
	texto = forms.CharField(widget=forms.Textarea(attrs={'cols':'58', 'rows':'17'}))
	imagen = forms.FileField(widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	link = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	class Meta:
		model = Noticia
		exclude = ('visitas')
    
class PublicidadForm(ModelForm):
	imagen = forms.FileField(widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	class Meta:
		model = Publicidad

class PrincipalForm(ModelForm):
	texto = forms.CharField(widget=forms.Textarea(attrs={'cols':'58', 'rows':'17'}))
	imagen = forms.FileField(widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	link = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	class Meta:
		model = Principal

class DiarioForm(ModelForm):
	texto = forms.CharField(widget=forms.Textarea(attrs={'cols':'58', 'rows':'17'}))
	imagen = forms.FileField(widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	link = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	class Meta:
		model = Diario
    

class BannerForm(ModelForm):
	titulo = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	imagen = forms.FileField(widget=forms.FileInput(attrs={'style':"width:280px; border: 0;"}))
	link = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	class Meta:
		model = Banner


class UpdateUserForm(ModelForm):
	first_name = forms.CharField(max_length=30, label='Nombre(s)', required=True, error_messages={'required': 'Este campo es obligatorio'})
	last_name = forms.CharField(max_length=30, label='Apellidos', required=False)
	email = forms.EmailField(label='Correo electrónico', required=True, error_messages={'required': 'Este campo es obligatorio', 'invalid':'Escriba un correo electrónico válido'})

	class Meta:
		model = User
		fields = ("first_name","last_name","email")

	def save(self, commit=True):
		user = super(UpdateUserForm, self).save(commit=False)
		user.first_name = escape(self.cleaned_data["first_name"])
		user.last_name = escape(self.cleaned_data["last_name"])
		user.email = escape(self.cleaned_data["email"])
		if commit:
			user.save()
		return user


class UsuarioForm(ModelForm):
	first_name = forms.CharField(max_length=30, label='Nombre(s)', required=True, error_messages={'required': 'Este campo es obligatorio'}, widget=forms.TextInput(attrs={'size':'35'}))
	last_name = forms.CharField(max_length=30, label='Apellidos', required=False, widget=forms.TextInput(attrs={'size':'35'}))
	username = forms.CharField(max_length=30, label='Usuario', required=True, error_messages={'required': 'Este campo es obligatorio', 'unique':'Este usuario ya existe'}, widget=forms.TextInput(attrs={'size':'35'}))
	email = forms.EmailField(label='Correo electrónico', required=True, error_messages={'required': 'Este campo es obligatorio', 'invalid':'Escriba un correo electrónico válido'}, widget=forms.TextInput(attrs={'size':'35'}))
	password1 = forms.CharField(max_length=16, min_length=6 ,label='Contraseña', widget=forms.PasswordInput(render_value=False, attrs={'size':'35'}),error_messages={'required': 'Este campo es obligatorio', 'min_length':'Debe ser de mínimo 6 caracteres'})
	password2 = forms.CharField(max_length=16, min_length=6, label='Confirma contraseña', widget=forms.PasswordInput(render_value=False, attrs={'size':'35'}), error_messages={'required': 'Este campo es obligatorio', 'min_length':'Debe ser de mínimo 6 caracteres'})
	class Meta:
		model = User
		fields = ("first_name", "last_name", "email" , "username", "password1", "password2")

	def save(self, commit=True):
		user = super(UsuarioForm, self).save(commit=False)
		user.first_name = escape(self.cleaned_data["first_name"])
		user.last_name = escape(self.cleaned_data["last_name"])
		user.email = escape(self.cleaned_data["email"])
		user.username = escape(self.cleaned_data["username"])
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


