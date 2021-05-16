from rest_framework import serializers
from dbloyalty.models import Project, Rule, Status, Transaction, Member


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', )


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name', 'points_to_receive', 'project', )


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ('id', 'name', 'rule_type', 'points_to_add', 'purchase_percentage', 'status', )


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'phone', 'first_name', 'last_name', 'birth_date',
                  'email', 'statuses', 'total_points', 'points_for_payment', )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'member', 'order_id', 'points', 'transaction_type', 'transaction_status', )
