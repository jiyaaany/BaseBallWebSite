from django.urls import path
from cafe import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

app_name : 'cafe'
urlpatterns = [
    path('', views.index, name="index"),
    path('form/', views.form, name='form'),
    path('detail/', views.detail, name='detail'),
    path('photo/', views.photo, name="baseball_photo"),
    path('movie/', views.movie, name="baseball_movie"),
    path('photo_form/', views.photo_form, name="photo_form"),
    path('create_photo/', views.create_photo, name="create_photo"),
    path('create_post/', views.create_post, name="create_post"),
    path('photo/photo_detail/<int:post_id>/', views.photo_detail, name="photo_detail"),
    path('howto/', views.howto, name="howto")
    # static(settinjgs.MEDIA_URL, document_root=settings.MEDIA_ROOT),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)