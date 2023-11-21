from django.urls import path, include
from product import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', views.CategoryAPI.as_view()),
    path('subcategory/', views.SubCategoryAPI.as_view()),
    path('product/', views.ProductAPI.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     path('product/', views.ProductAPI.as_view()),
#     path('category/', views.CategoryAPI.as_view()),
#     path('Subcategory/', views.SubCategoryAPI.as_view()),
# ]

