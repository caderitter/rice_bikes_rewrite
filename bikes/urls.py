from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new_transaction$', views.add_transaction, name='new_transaction'),
    url(r'^(?P<pk>\d+)/delete$', views.TransactionDelete.as_view(), name="delete_transaction"),
]