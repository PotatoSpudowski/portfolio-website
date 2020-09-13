from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import index, contact, about, post, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('contact', contact),
    path('about', about),
    path('post/<id>/', post, name="post-detail"),
    path('signup',signup, name='signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

