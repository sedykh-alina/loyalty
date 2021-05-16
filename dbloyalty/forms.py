from django.forms import ModelForm

from .models import Member
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class MemberAdminForm(ModelForm):
    """
    Форма, представляющая участника программы лояльности в админке
    """

    class Meta:
        """Метаинформация"""
        model = Member
        fields = ('phone', 'first_name', 'last_name', 'birth_date',
                  'email', 'total_points', 'points_for_payment', 'statuses')
        widgets = {
            'phone': PhoneNumberInternationalFallbackWidget(),
        }