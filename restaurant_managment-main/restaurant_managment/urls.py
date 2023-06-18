from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from users.forms import LoginForm
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('configrate.urls')),
    path('', include('input.urls')),
    path('', include('purchases.urls')),
    path('', include('users.urls')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login',template_name='users/login.html'), name='logout'),
    re_path(r'^reset-password/$', ResetPasswordView.as_view(), name='reset_password'),
    re_path(r'^change-password/$', ChangePasswordView.as_view(), name='change_password'),
    #path('password-reset-confirm/<uidb64>/<token>/',
     #    auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
      #   name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    url('oauth/', include('social_django.urls', namespace='social')),

]  


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 