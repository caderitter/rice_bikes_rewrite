from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^repair/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^merch/(?P<pk>[0-9]+)/$', views.MerchDetailView.as_view(), name='merch_detail'),
    url(r'^new_repair_transaction$', views.add_transaction, name='new_repair_transaction'),
    url(r'^new_merch_transaction$', views.add_merch_transaction, name='new_merch_transaction'),
    url(r'^repair/(?P<pk>\d+)/delete$', views.TransactionDelete.as_view(), name='delete_transaction'),
    url(r'^merch/(?P<pk>\d+)/delete$', views.MerchTransactionDelete.as_view(), name='delete_merch_transaction'),
    url(r'^(?P<pk>\d+)/add_bike$', views.add_bike, name='add_bike'),
    url(r'^(?P<pk>\d+)/bike_edit$', views.edit_bike, name='bike_edit'),
    url(r'repair/^(?P<pk>\d+)/transaction_edit$', views.TransactionUpdate.as_view(), name='transaction_edit'),
]