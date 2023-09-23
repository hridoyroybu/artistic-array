from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('filter-color/<int:id>', views.searchByColor, name='filter-color'),
    path('filter-size/<int:id>', views.searchBySize, name='filter-size'),
    path('sortby/<int:id>', views.sortBy, name='sortby'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]