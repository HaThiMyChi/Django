
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # cach viet nay goi function ben view xem trong file views.py co chu thich
    # path('', views.index, name="index" ),
    #
    
    # Cach goi nay cua class view xem trong file views.py co chu thich
    path('', views.IndexClass.as_view(), name="index"),
    #
    # path('add/', views.PostClass.as_view(), name="add"),
    path('save/', views.ClassSaveNew.as_view(), name="save"),
    path('email/', views.email_view, name="email"),
    path('process/', views.process, name="pro"),
    
    path('loginIndex/', views.LoginClassIndex.as_view(), name="loginindex"),
    path('login/', views.LoginClass.as_view(), name="login"),
    path('user-view/', views.ViewUser.as_view(), name="user_view"),
    path('view-pro/', views.view_product, name="view-product"),
    path('add-post/', views.AddPost.as_view(), name="add_post"),
    
    
    
    
]
