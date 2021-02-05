from django.urls import path,re_path,include
from .views import ManufacturerViewset,ManufacturerDetailView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'manufacturer', ManufacturerViewset)

urlpatterns =[

    # re_path(r'^manufacturer',MfgView.as_view()),
    path('',include(router.urls)),
    re_path(r'^detail/$',ManufacturerDetailView.as_view(), name='detail')
]
# urlpatterns = format_suffix_patterns(urlpatterns,allowed=['json','html'])