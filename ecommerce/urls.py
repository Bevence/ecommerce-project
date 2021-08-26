from django.urls import path
from ecommerce.views import (
    EcommerceTemplateView, 
    ItemsListView, 
    SubCategoryListView, 
    CategoryListView, 
    ItemDetailView
)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", cache_page(10*60)(EcommerceTemplateView.as_view()), name="home"),
    path("products/", ItemsListView.as_view(), name="items"),
    path("products/<category>/", CategoryListView.as_view(), name="cat_view"),
    path("products/<category>/<sub_category>/", SubCategoryListView.as_view(), name="sub_cat_view"),
    path("products/<category>/<sub_category>/<slug>", ItemDetailView.as_view(), name="detail_view"),

]
