#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'articulo7.views.home', name='home'),
    # url(r'^articulo7/', include('articulo7.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^adminity/', include(admin.site.urls)),
    url(r'^art7admin/usuarios/$', 'home.views.usuarios'),
    url(r'^$', 'home.views.usuarios'),
    url(r'^art7admin/banner-principal/$', 'home.views.banner_principal'),
    url(r'^art7admin/diario/$', 'home.views.diario'),
    url(r'^art7admin/nota-principal/$', 'home.views.nota_principal'),
    url(r'^art7admin/publicidad/$', 'home.views.publicidad'),
    url(r'^art7admin/noticias/$', 'home.views.noticias'),
    url(r'^art7admin/articulos/$', 'home.views.articulos'),
    url(r'^art7admin/audio/$', 'home.views.audio'),
    url(r'^art7admin/video/$', 'home.views.video'),
    url(r'^art7admin/foto/$', 'home.views.foto'),
    url(r'^art7admin/usuarios/nuevo/$', 'home.views.nuevo_usuario'),
    url(r'^art7admin/usuarios/(?P<usr>[0-9]+)/eliminar/$', 'home.views.eliminar_usuario'),
    url(r'^art7admin/usuarios/(?P<usr>[0-9]+)/$', 'home.views.ver_usuario'),
    url(r'^art7admin/banner-principal/nuevo/$', 'home.views.nuevo_banner'),
    url(r'^art7admin/banner-principal/(?P<bpr>[0-9]+)/eliminar/$', 'home.views.eliminar_banner'),
    url(r'^art7admin/banner-principal/(?P<bpr>[0-9]+)/$', 'home.views.ver_banner'),

    url(r'^art7admin/diario/nuevo/$', 'home.views.nuevo_diario'),
    url(r'^art7admin/diario/(?P<dia>[0-9]+)/eliminar/$', 'home.views.eliminar_diario'),
    url(r'^art7admin/diario/(?P<dia>[0-9]+)/$', 'home.views.ver_diario'),

    url(r'^art7admin/nota-principal/nuevo/$', 'home.views.nuevo_nprincipal'),
    url(r'^art7admin/nota-principal/(?P<npr>[0-9]+)/eliminar/$', 'home.views.eliminar_nprincipal'),
    url(r'^art7admin/nota-principal/(?P<npr>[0-9]+)/$', 'home.views.ver_nprincipal'),

    url(r'^art7admin/publicidad/nuevo/$', 'home.views.nuevo_publicidad'),
    url(r'^art7admin/publicidad/(?P<pub>[0-9]+)/eliminar/$', 'home.views.eliminar_publicidad'),
    url(r'^art7admin/publicidad/(?P<pub>[0-9]+)/$', 'home.views.ver_publicidad'),

    url(r'^art7admin/noticias/nuevo/$', 'home.views.nueva_noticia'),
    url(r'^art7admin/noticias/(?P<noti>[0-9]+)/eliminar/$', 'home.views.eliminar_noticia'),
    url(r'^art7admin/noticias/(?P<noti>[0-9]+)/$', 'home.views.ver_noticia'),

    url(r'^art7admin/articulos/nuevo/$', 'home.views.nuevo_articulo'),
    url(r'^art7admin/articulos/(?P<arti>[0-9]+)/eliminar/$', 'home.views.eliminar_articulo'),
    url(r'^art7admin/articulos/(?P<arti>[0-9]+)/$', 'home.views.ver_articulo'),

    url(r'^art7admin/videos/nuevo/$', 'home.views.nuevo_video'),
    url(r'^art7admin/videos/(?P<uni>[0-9]+)/eliminar/$', 'home.views.eliminar_video'),
    url(r'^art7admin/videos/(?P<uni>[0-9]+)/$', 'home.views.ver_video'),

    url(r'^art7admin/foto/nuevo/$', 'home.views.nueva_foto'),
    url(r'^art7admin/foto-cat/nuevo/$', 'home.views.nueva_fotocat'),
    url(r'^art7admin/foto/(?P<uni>[0-9]+)/eliminar/$', 'home.views.eliminar_foto'),
    url(r'^art7admin/foto/(?P<uni>[0-9]+)/$', 'home.views.ver_foto'),

    url(r'^art7admin/audio/nuevo/$', 'home.views.nuevo_audio'),
    url(r'^art7admin/audio/(?P<uni>[0-9]+)/eliminar/$', 'home.views.eliminar_audio'),
    url(r'^art7admin/audio/(?P<uni>[0-9]+)/$', 'home.views.ver_audio'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve', 
        {'document_root':settings.MEDIA_ROOT,}),
    
)
