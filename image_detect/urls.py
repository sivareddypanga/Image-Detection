from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.model, name = 'model' ),
    url(r'^upload/', views.image_upload, name = 'upload' ),
    url(r'^results/', views.result, name = 'result' ),
    ]
