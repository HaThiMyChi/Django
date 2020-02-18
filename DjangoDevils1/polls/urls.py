from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'polls'
urlpatterns = [
		path('detail/<int:question_id>', views.detailView, name="detail"),
		path('list/', views.viewlist, name="view_list"),
    path('', views.index, name="index"),
		path('abc/', views.ham1, name="ham"),
		path('<int:question_id>', views.vote, name="vote"),
]

# note đường dẫn sẽ chạy vào polls trước vì trong file DjangoDevils1 -> urls có gọi urls con
# có đường dẫn là polls rồi mới tới /list tiếp
#path('detail/<int:question_id>') boi  vì nó truyền theo id
