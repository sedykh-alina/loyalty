from django.contrib import admin

from .models import Project, Status, Rule, Member, Transaction
from .forms import MemberAdminForm


admin.site.site_header = "Администрирование программы лояльности"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели Project
    """
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели Status
    """
    list_display = ('name', 'points_to_receive', 'project')
    list_filter = ('project',)
    search_fields = ('name',)
    ordering = ('points_to_receive', 'project')


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели Rule
    """
    list_display = ('name', 'rule_type', 'status',
                    'points_to_add', 'purchase_percentage')
    list_filter = ('rule_type', 'status')
    search_fields = ('name',)
    ordering = ('points_to_add', 'purchase_percentage')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели Member
    """
    form = MemberAdminForm
    readonly_fields = ('total_points', 'points_for_payment')
    list_display = ('phone', 'first_name', 'last_name', 'birth_date',
                    'email', 'total_points', 'points_for_payment', 'show_statuses')
    list_filter = ('statuses',)
    search_fields = ('phone', 'first_name', 'last_name', 'birth_date', 'email')
    ordering = ('phone', 'last_name', 'first_name', 'email', 'birth_date')

    def show_statuses(self, obj):
        return ', '.join(map(lambda x: str(x), list(obj.statuses.all())))
    show_statuses.short_description = 'Статусы'


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели Transaction
    """
    list_display = ('member', 'order_id', 'points',
                    'transaction_type', 'transaction_status', )
    list_filter = ('member', 'order_id', 'transaction_type', 'transaction_status', )
    search_fields = ('member', 'order_id', )
    ordering = ('points', 'order_id', )
