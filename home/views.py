#encoding:utf-8
from home.models import Audio, FotoCategoria, Foto, Video, ArticuloCategoria, Articulo, Banner, Diario, DiarioCategoria, Principal, Publicidad, Noticia
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from home.forms import UserProfileForm, FotocatForm, AudioForm, FotoForm, VideoForm, ArticuloForm, NoticiaForm, UsuarioForm, UpdateUserForm, BannerForm, DiarioForm, PrincipalForm, PublicidadForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import datetime

def ver_audio(request, uni):
	if not request.user.is_authenticated():
		return redirect('/')

	audio = get_object_or_404(Audio, pk=uni)
	if request.method == 'POST':
		formulario = AudioForm(request.POST, request.FILES, instance=audio)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó el audio')
			return redirect('/art7admin/audio/')
	else:
		formulario = AudioForm(instance=audio)
	return render(request,'editar-audio.html', { 'formulario':formulario})

def eliminar_audio(request, uni):
	if not request.user.is_authenticated():
		return redirect('/')

	audio = get_object_or_404(Audio, pk=uni)
	audio.delete()
	return redirect('/art7admin/audio/')

def nuevo_audio(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = AudioForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/audio/')
	else:
		formulario = AudioForm()
	return render(request,'registro.html', { 'formulario':formulario})

def ver_foto(request, uni):
	if not request.user.is_authenticated():
		return redirect('/')

	foto = get_object_or_404(Foto, pk=uni)
	if request.method == 'POST':
		formulario = FotoForm(request.POST, request.FILES, instance=foto)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó la foto')
			return redirect('/art7admin/foto/')
	else:
		formulario = FotoForm(instance=foto)
	return render(request,'editar-foto.html', { 'formulario':formulario})

def eliminar_foto(request, uni):
	if not request.user.is_authenticated():
		return redirect('/')

	foto = get_object_or_404(Foto, pk=uni)
	video.delete()
	return redirect('/art7admin/foto/')

def nueva_fotocat(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = FotocatForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/foto/')
	else:
		formulario = FotocatForm()
	return render(request,'registro.html', { 'formulario':formulario})

def nueva_foto(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = FotoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/foto/')
	else:
		formulario = FotoForm()
	return render(request,'registro.html', { 'formulario':formulario})

def ver_video(request, uni):
	if not request.user.is_authenticated():
		return redirect('/')

	video = get_object_or_404(Video, pk=uni)
	if request.method == 'POST':
		formulario = VideoForm(request.POST, request.FILES, instance=video)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó el video')
			return redirect('/art7admin/video/')
	else:
		formulario = VideoForm(instance=video)
	return render(request,'registro.html', { 'formulario':formulario})

def eliminar_video(request, uni):
	if not request.user.is_authenticated():
		return redirect('/')

	video = get_object_or_404(Video, pk=uni)
	video.delete()
	return redirect('/art7admin/video/')

def nuevo_video(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = VideoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/video/')
	else:
		formulario = VideoForm()
	return render(request,'registro.html', { 'formulario':formulario})

def ver_articulo(request, arti):
	if not request.user.is_authenticated():
		return redirect('/')

	articulo = get_object_or_404(Articulo, pk=arti)
	if request.method == 'POST':
		formulario = ArticuloForm(request.POST, request.FILES, instance=articulo)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó el artículo')
			return redirect('/art7admin/articulos/')
	else:
		formulario = ArticuloForm(instance=articulo)
	return render(request,'registro-articulo.html', { 'formulario':formulario})

def eliminar_articulo(request, arti):
	if not request.user.is_authenticated():
		return redirect('/')

	articulo = get_object_or_404(Articulo, pk=arti)
	articulo.delete()
	return redirect('/art7admin/articulos/')

def nuevo_articulo(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = ArticuloForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/articulos/')
	else:
		formulario = ArticuloForm()
	return render(request,'registro-articulo.html', { 'formulario':formulario})

def ver_noticia(request, noti):
	if not request.user.is_authenticated():
		return redirect('/')

	noticia = get_object_or_404(Noticia, pk=noti)
	if request.method == 'POST':
		formulario = NoticiaForm(request.POST, request.FILES, instance=noticia)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó la noticia')
			return redirect('/art7admin/noticias/')
	else:
		formulario = NoticiaForm(instance=noticia)
	return render(request,'editar-noticia.html', { 'formulario':formulario})

def eliminar_noticia(request, noti):
	if not request.user.is_authenticated():
		return redirect('/')

	noticia = get_object_or_404(Noticia, pk=noti)
	noticia.delete()
	return redirect('/art7admin/noticias/')

def nueva_noticia(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = NoticiaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/noticias/')
	else:
		formulario = NoticiaForm()
	return render(request,'registro-noticia.html', { 'formulario':formulario})


def ver_publicidad(request, pub):
	if not request.user.is_authenticated():
		return redirect('/')

	publicidad = get_object_or_404(Publicidad, pk=pub)
	if request.method == 'POST':
		formulario = PublicidadForm(request.POST, request.FILES, instance=publicidad)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó la publicidad')
			return redirect('/art7admin/publicidad/')
	else:
		formulario = PublicidadForm(instance=publicidad)
	return render(request,'editar-publicidad.html', { 'formulario':formulario})


def eliminar_publicidad(request, pub):
	if not request.user.is_authenticated():
		return redirect('/')

	publicidad = get_object_or_404(Publicidad, pk=pub)
	publicidad.delete()
	return redirect('/art7admin/publicidad/')


def nuevo_publicidad(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = PublicidadForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/publicidad/')
	else:
		formulario = PublicidadForm()
	return render(request,'registro-publicidad.html', { 'formulario':formulario})

def ver_nprincipal(request, npr):
	if not request.user.is_authenticated():
		return redirect('/')

	principal = get_object_or_404(Principal, pk=npr)
	if request.method == 'POST':
		formulario = PrincipalForm(request.POST, request.FILES, instance=principal)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó una nota principal')
			return redirect('/art7admin/nota-principal/')
	else:
		formulario = PrincipalForm(instance=principal)
	return render(request,'editar-principal.html', { 'formulario':formulario})

def eliminar_nprincipal(request, npr):
	if not request.user.is_authenticated():
		return redirect('/')

	principal = get_object_or_404(Principal, pk=npr)
	principal.delete()
	return redirect('/art7admin/nota-principal/')


def nuevo_nprincipal(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = PrincipalForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró correctamente')
			return redirect('/art7admin/nota-principal/')
	else:
		formulario = PrincipalForm()
	return render(request,'registro-principal.html', { 'formulario':formulario})

def ver_diario(request, dia):
	if not request.user.is_authenticated():
		return redirect('/')

	diario = get_object_or_404(Diario, pk=dia)
	if request.method == 'POST':
		formulario = DiarioForm(request.POST, request.FILES, instance=diario)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó un diario')
			return redirect('/art7admin/diario/')
	else:
		formulario = DiarioForm(instance=diario)
	return render(request,'editar-diario.html', { 'formulario':formulario})


def eliminar_diario(request, dia):
	if not request.user.is_authenticated():
		return redirect('/')

	diario = get_object_or_404(Diario, pk=dia)
	diario.delete()
	return redirect('/art7admin/diario/')

def nuevo_diario(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = DiarioForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registro un nuevo diario')
			return redirect('/art7admin/diario/')
	else:
		formulario = DiarioForm()
	return render(request,'registro-diario.html', { 'formulario':formulario})

def ver_banner(request, bpr):
	if not request.user.is_authenticated():
		return redirect('/')

	banner = get_object_or_404(Banner, pk=bpr)
	if request.method == 'POST':
		formulario = BannerForm(request.POST, request.FILES, instance=banner)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó un banner principal')
			return redirect('/art7admin/banner-principal/')
	else:
		formulario = BannerForm(instance=banner)
	return render(request,'editar-banner.html', { 'formulario':formulario})


def eliminar_banner(request, bpr):
	if not request.user.is_authenticated():
		return redirect('/')

	banner = get_object_or_404(Banner, pk=bpr)
	banner.delete()
	return redirect('/art7admin/banner-principal/')


def nuevo_banner(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = BannerForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se registro un nuevo banner principal')
			return redirect('/art7admin/banner-principal/')
	else:
		formulario = BannerForm()
	return render(request,'registro-banner.html', { 'formulario':formulario})


def banner_principal(request):
	if not request.user.is_authenticated():
		return redirect('/')

	banners = Banner.objects.all()
	return render(request,'banner-principal.html',{ 'banners':banners })

def ver_usuario(request, usr):
	if not request.user.is_authenticated():
		return redirect('/')

	usuario = get_object_or_404(User, pk=usr)
	if request.method == 'POST':
		formulario = UpdateUserForm(request.POST, instance=usuario)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.SUCCESS, 'Se actualizó el usuario')
			return redirect('/art7admin/usuarios/')
	else:
		formulario = UpdateUserForm(instance=usuario)
	return render(request,'registro.html', { 'formulario':formulario})

def eliminar_usuario(request, usr):
	if not request.user.is_authenticated():
		return redirect('/')

	usuario = get_object_or_404(User, pk=usr)
	usuario.is_active = False
	usuario.save()
	return redirect('/art7admin/usuarios/') 

def usuarios(request):
	if not request.user.is_authenticated():
		return redirect('/')

	usuarios = User.objects.filter(is_active=True)
	return render(request,'usuarios.html',{ 'usuarios':usuarios })

def nuevo_usuario(request):
	if not request.user.is_authenticated():
		return redirect('/')

	if request.method == 'POST':
		formulario = UsuarioForm(request.POST)
		adicional = UserProfileForm(request.POST)
		if formulario.is_valid() and adicional.is_valid():
			f = formulario.save()
			adicional.user = f
			adicional.save()
			messages.add_message(request, messages.SUCCESS, 'Se registró un nuevo usuario')
			return redirect('/art7admin/usuarios/')
	else:
		formulario = UsuarioForm()
		adicional = UserProfileForm()
	return render(request,'registro-usuario.html', { 'formulario':formulario, 'adicional':adicional})

def diario(request):
	if not request.user.is_authenticated():
		return redirect('/')

	diario = Diario.objects.all()
	return render(request, 'diario.html', {'diario':diario})

def nota_principal(request):
	if not request.user.is_authenticated():
		return redirect('/')
	principales = Principal.objects.all()
	return render(request, 'nota-principal.html', {'principales':principales})

def publicidad(request):
	if not request.user.is_authenticated():
		return redirect('/')

	publicidades = Publicidad.objects.all()
	return render(request, 'publicidad.html', {'publicidades':publicidades})

def noticias(request):
	if not request.user.is_authenticated():
		return redirect('/')

	noticias = Noticia.objects.all()
	return render(request, 'noticias.html', {'noticias': noticias})

def articulos(request):
	if not request.user.is_authenticated():
		return redirect('/')

	articulos = Articulo.objects.all()
	return render(request, 'articulos.html', {'articulos':articulos})

def audio(request):
	if not request.user.is_authenticated():
		return redirect('/')

	audios = Audio.objects.all()
	return render(request, 'audio.html', {'audios':audios})

def video(request):
	if not request.user.is_authenticated():
		return redirect('/')

	videos = Video.objects.all()
	return render(request, 'video.html', {'videos':videos})

def foto(request):
	if not request.user.is_authenticated():
		return redirect('/')

	fotos = Foto.objects.all()
	return render(request, 'foto.html', {'fotos':fotos})

