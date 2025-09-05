from django.contrib import admin
from django.urls import path, include
from recipes.views import HomeView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password reset (templates provided below)
    path('', HomeView.as_view(), name='home'),
    path('recipes/', include('recipes.urls')),
]
