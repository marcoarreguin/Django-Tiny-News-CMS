from home.models import FotoCategoria, Foto, Video, ArticuloCategoria, Articulo, NoticiaCategoria, UserProfile, Banner, DiarioCategoria, Diario, Principal, Noticia, Publicidad
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Banner)
admin.site.register(DiarioCategoria)
admin.site.register(Diario)
admin.site.register(Principal)
admin.site.register(Publicidad)
admin.site.register(Noticia)
admin.site.register(NoticiaCategoria)
admin.site.register(Articulo)
admin.site.register(ArticuloCategoria)
admin.site.register(Video)
admin.site.register(Foto)
admin.site.register(FotoCategoria)

