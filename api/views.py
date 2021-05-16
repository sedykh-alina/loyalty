from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from dbloyalty.models import Project, Status, Rule, Member, Transaction
from .serializers import ProjectSerializer, StatusSerializer, RuleSerializer, MemberSerializer, TransactionSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class RuleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
