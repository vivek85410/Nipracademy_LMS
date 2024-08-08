from django.contrib import admin
from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Homepage,name="home"),
    path('logout',views.signout , name = 'logout'),
    path('signup', views.SignupView.as_view() , name = 'signup'),
    path('About_us', views.About_us , name = 'About_us'),
    path('Allcourses', views.Allcourses, name="Allcourses"),
    path('login', views.LoginView.as_view() , name = 'login'),
    path('my-courses',views.MyCoursesList.as_view() , name = 'my-courses'),
    path('course/<str:slug>', views.coursePage , name = 'coursepage'),
    path('check-out/<str:slug>',views.checkout , name = 'check-out'),
    path('verify_payment', views.verifyPayment , name = 'verify_payment'),
    path('contact/',views.details,name='details'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="Nipracademy/password_reset_form.html"),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="Nipracademy/password_reset_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="Nipracademy/password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="Nipracademy/password_reset_complete.html"),name="password_reset_complete"),
    path('comments/', views.comment_page, name='comment_page'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('address/',views.OfflineAdmission,name="address_page"),
    path('terms-and-conditions/',views.terms_and_conditions,name="terms-and-conditions"),
    path('privacy-policy/',views.privacy_policy,name="privacy-policy"),
    path('faculty/',views.faculty,name="faculty_page"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
