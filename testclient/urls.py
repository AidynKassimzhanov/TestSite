from django.urls import path, re_path
from testclient import views

urlpatterns = [
    path('', views.test, name='test'),
    path('', views.test, name='test1'),
    path('starttest/', views.starttest, name='starttest'),
    path('fetch/', views.fetch, name='fetch'),
    path('end/', views.end, name='end'),
    # path('details', views.test_begins, name='test-details'),
    # re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]