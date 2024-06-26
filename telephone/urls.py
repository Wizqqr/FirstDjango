from django.urls import path
from . import views

urlpatterns = [
    path('phone_list/', views.PhoneListView.as_view(), name='phone_list'),
    path('phone_list/<int:id>/', views.PhoneDetailForm.as_view(), name='phone_detail'),
    path('phone_list/<int:id>/delete/', views.PhoneDeleteForm.as_view(), name='phone_detail_delete'),
    path('phone_list/<int:id>/update/', views.PhoneEditForm.as_view(), name='phone_update_view'),
    path('create_phone/', views.PhoneCreateForm.as_view(), name='create_phone'),
    path('phone_list/comment/', views.PhoneCreateComment.as_view(), name='create_comment'),
    path('search/', views.SearchPhoneView.as_view(), name='phone_search'),
    path('create_comment_ajax/', views.create_comment_ajax, name='create_comment_ajax'),
]
