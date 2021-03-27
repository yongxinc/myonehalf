from django.urls import include, path
from django.contrib import admin
from django.apps import apps
from django.conf.urls.static import static

from mainsite import views


from django.conf import settings
# from django.conf.urls.static import static
app_name = 'mainsite'
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),



    path('admin/', admin.site.urls),

    path('', include(apps.get_app_config('oscar').urls[0])),

    path('accounts/seller-apply',views.sellerApply),  # 賣家申請畫面
    path('accounts/seller-apply-process',views.sellerApplyProcess), #處理申請


    
    # path('love', ApplicationListView.as_view(), name='list'),
    path('collectinfo/', views.collectInfo),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)