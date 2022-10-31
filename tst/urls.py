from django.urls import path, re_path
from tst import views

urlpatterns = [
    path('', views.test, name='test'),
    path('starttest/', views.starttest, name='starttest'),
    path('getquestion/', views.getquestion, name='getquestion'),
    path('getquestionfetch/', views.getquestionfetch, name='getquestionfetch'),
    
    # path('details', views.test_begins, name='test-details'),
    # re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]