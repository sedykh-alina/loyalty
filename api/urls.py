from django.urls import path, include
from rest_framework.routers import DefaultRouter, APIRootView
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProjectViewSet, StatusViewSet, RuleViewSet, MemberViewSet, TransactionViewSet


class LoyaltyAPIRootView(APIRootView):
    """
    API программы лояльности
    """
    pass


class LoyaltyRouter(DefaultRouter):
    APIRootView = LoyaltyAPIRootView


router = LoyaltyRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('statuses', StatusViewSet, basename='statuses')
router.register('rules', RuleViewSet, basename='rules')
router.register('members', MemberViewSet, basename='members')
router.register('transactions', TransactionViewSet, basename='transactions')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]