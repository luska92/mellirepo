from django.conf.urls import url
from melliapp import views

app_name = 'melliapp'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$',views.ProduktDetailView.as_view(),name='detail'),
    url(r'^about/$',views.OmnieView.as_view(),name='omnie'),
    url(r'^contact/$',views.ContactView,name='contact'),
]
