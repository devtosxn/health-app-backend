from django.urls import path, include


urlpatterns = [
	path('', include('api.urls')),
    path('blogs/', include('blog.urls')),
]