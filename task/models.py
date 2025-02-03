from django.db import models
from django.db.models import Count
from django.contrib.auth import get_user_model


User = get_user_model()     

WORK_TYPES = (
    ("Аварийно-восстановительные работы", "avr"),
    ("Монтаж спутниковой антенны", "antenna_mount"),
    ("Юстировка спутниковой антенны", "antenna_pointing"),
    ("Ремонт облучателя", "feed_repair"),
    ("Другие работы", "other"),
)

STATUS_CHOICES = (
    ("in_work", "В работе"),
    ("done", "Завершена"),
    ("invoiced", "Выставлены документы"),
    ("paid", "Оплачена"),
    ("canceled", "Отменена"),
)

class Customer(models.Model):
    name = models.CharField(
        max_length=255,
        help_text='Введите наименование заказчика (Оператор или обслуживающая компания)',
        verbose_name=u'Наименование'
    )
    is_operator = models.BooleanField(default=True, verbose_name=u'Оператор')
    contact_person_name = models.CharField(max_length=100, verbose_name=u'Контактное лицо')
    contact_person_phone = models.CharField(max_length=255, verbose_name=u'Контактный телефон')
    contact_person_email = models.EmailField(verbose_name=u'Контактный емейл')
    address = models.TextField(verbose_name=u'Адрес')

    class Meta:
        ordering = ['pk']

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField(
        max_length=255,
        help_text='Введите наименование клиента (Организация или ФИО если заказчик физ. лицо)',
        verbose_name=u'Наименование'
    )
    contact_person_name = models.CharField(max_length=100, verbose_name=u'Контактное лицо')
    contact_person_phone = models.CharField(max_length=255, verbose_name=u'Контактный телефон')
    contact_person_email = models.EmailField(verbose_name=u'Контактный емейл')
    address = models.TextField(verbose_name=u'Адрес')

    class Meta:
        ordering = ['pk']

    def __str__(self) -> str:
        return self.name


class WorkType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    base_price = models.IntegerField(blank=True)

    class Meta:
        ordering = ['pk']

    def __str__(self) -> str:
        return self.title
    

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Наименование работ')
    adding_date = models.DateField(auto_now_add=True, 
        verbose_name=u'Дата создания задачи')
    type = models.ForeignKey(
        WorkType,
        on_delete=models.CASCADE,
        related_name='work_types',
        verbose_name=u'Вид работ'
    )
    description = models.TextField(blank=True, verbose_name=u'Описание задачи')
    cost = models.IntegerField(blank=True, verbose_name=u'Стоимость работ (руб.)')
    address = models.TextField(verbose_name=u'Адрес объекта')
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE, 
        related_name='tasks', 
        verbose_name=u'Клиент'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE, 
        related_name='tasks', 
        verbose_name=u'Заказчик'
    )
    executor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        blank=False, null=False, 
        verbose_name=u'Исполнитель')
    status = models.CharField(
        u'Статус', 
        max_length=50, 
        choices=STATUS_CHOICES,
        default='in_work'
    )

    # is_done = models.BooleanField(default=False, verbose_name='Завершена')
    # is_canceled = models.BooleanField(default=False, verbose_name='Отменена')
    # is_invoiced = models.BooleanField(default=False, verbose_name='Выставлены документы')
    # is_paid = models.BooleanField(default=False, verbose_name='Оплачена')

    class Meta:
        ordering = ['pk']

    def __str__(self) -> str:
        return self.title