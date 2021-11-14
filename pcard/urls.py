from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='first_view'),
    url(r'^home/$', views.home, name='home'),
    url(r'^base', views.Hbase, name='base'),
    url(r'^uimage/$', views.uimage, name='uimage'),  # image upload template!
    url(r'^pancard/$', views.ocr_core, name='PanCard'),  # PAN Card OCR template!
    url(r'^index', views.index, name='index'),
    url(r'^aadhar/$', views.aadhar, name='aadhar'),
    url(r'^voterid/$', views.voter_id, name='voterid'),
    url(r'^bank_id/$', views.bank_id, name='bank_id'),
    url(r'^driver/$', views.driver_id, name='driver_id'),
    url(r'^panverify', views.pandataverification, name='panverify'),
    url(r'^drverify', views.drivingdataverification, name='drivingverify'),
    url(r'^voterverify', views.voterdataverification, name='voterverify'),
    url(r'^aadharverify', views.aadhardataverification, name='aadharverify'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
