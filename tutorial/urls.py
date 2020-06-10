from django.conf.urls import url
from tutorial import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url(r'^api/tutorial$',views.tutorial_list ),
    url(r'^api/tutorial/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorial/published$', views.tutorial_list_published),
    url(r'api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]