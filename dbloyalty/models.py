import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Project(models.Model):
    """
    Проект, к которому относится программа лояльности (DB, Tkano, и т.п.)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название проекта', max_length=100)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ('name',)

    def __str__(self):
        return self.name


####################################
# Настройки программы лояльности
####################################
class Status(models.Model):
    """
    Статусы программы лояльности
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название статуса', max_length=250)
    points_to_receive = models.PositiveIntegerField(verbose_name='Баллы для получения')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.project})'


class Rule(models.Model):
    """
    Правила начисления баллов
    """
    class RuleType(models.TextChoices):
        HELLO_POINTS = 'HP', _('Приветственные баллы')
        PURCHASE_POINTS = 'PP', _('Баллы за покупку')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название правила', max_length=250)
    rule_type = models.CharField(verbose_name='Тип правила', max_length=2, choices=RuleType.choices,
                                 default=RuleType.PURCHASE_POINTS)
    points_to_add = models.IntegerField(verbose_name='Баллы для начисления', default=0)
    purchase_percentage = models.IntegerField(verbose_name='Процент от покупки', default=0)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE, related_name='rules')

    class Meta:
        verbose_name = 'Правило начисления баллов'
        verbose_name_plural = 'Правила начисления баллов'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    Участник программы лояльности
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # phone = models.CharField(verbose_name='Телефон', max_length=20, unique=True,
    #                         validators=[RegexValidator(regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
    #                                                    message='Формат номера телефона неправильный'),])
    phone = PhoneNumberField(verbose_name='Телефон', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, blank=True)
    birth_date = models.DateField(verbose_name='День рождения', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    # status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='members', verbose_name='Статус')
    statuses = models.ManyToManyField(Status, related_name='members', verbose_name='Статусы')
    total_points = models.IntegerField(verbose_name='Накопленные баллы', default=0)
    points_for_payment = models.IntegerField(verbose_name='Количество баллов для оплаты', default=0)

    class Meta:
        verbose_name = 'Участник программы лояльности'
        verbose_name_plural = 'Участники программы лояльности'
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return f'{self.phone} {self.first_name} {self.last_name}'.rstrip()


class Transaction(models.Model):
    """
    Транзакция, начисляющая или списывающая баллы члену программы лояльности
    """
    class TransactionType(models.IntegerChoices):
        EARN_POINTS = 1, _('Начисление баллов')
        SPEND_POINTS = 2, _('Списание баллов')
        SET_STATUS = 3, _('Установка статуса')

    class TransactionStatus(models.IntegerChoices):
        OPEN = 1, _('Открытая')
        CLOSE = 2, _('Закрытая')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='transactions')
    order_id = models.TextField(verbose_name='Номер заказа', blank=True, max_length=11)
    points = models.IntegerField(verbose_name="Количество баллов", default=0)
    transaction_type = models.IntegerField(verbose_name='Тип транзакции', choices=TransactionType.choices,
                                           default=TransactionType.EARN_POINTS)
    transaction_status = models.IntegerField(verbose_name='Статус транзакции', choices=TransactionStatus.choices,
                                             default=TransactionStatus.OPEN)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ('order_id', 'points')

    def __str__(self):
        return f'{self.transaction_type} - {self.member} - {self.points} баллов'
