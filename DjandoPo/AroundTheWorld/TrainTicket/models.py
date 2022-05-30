from secrets import choice
from pydoc import describe
from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from matplotlib.style import available
from django.utils.translation import gettext_lazy as _


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Train(UUIDMixin):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"train"
        verbose_name = _('train')
        verbose_name_plural = _('trains')


class WagonChoices(models.TextChoices):

    RESERVED_SEAT = _('RESERVED SEAT'), _('reserved seat')
    COUPE = _('COUPE'), _('coupe')
    SW = _('SW'), _('SW')


class Wagon(UUIDMixin):
    name = models.IntegerField(_('wagon'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(20)])
    train = models.ForeignKey(Train, verbose_name=_('train'), on_delete=models.CASCADE, related_name='train_wagon')
    class_wagon = models.CharField(_('class'), choices=WagonChoices.choices, max_length=255)
    capacity = models.IntegerField(_('capacity'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(54)])

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "content\".\"wagon"
        verbose_name = _('wagon')
        verbose_name_plural = _('wagons')

class TariffChoices(models.TextChoices):

    SCHOOL = _('SCHOOL'), _('school')
    STUDENTS = _('STUDENTS'), _('students')
    CHILDREN = _('CHILDREN'), _('children')
    VETERANS = _('VETERANS'), _('veterans')
    PENSIONERS = _('PENSIONERS'), _('pensioners')
    PERSONS_WITH_DISABILITIES = _('PERSONS WITH DISABILITIES'), _('persons with disabilities')


class Privilege(UUIDMixin):
    DISCOUNT = (
    ('50', '50%'),
    ('25', '25%')
)
    category = models.CharField(_('category'), choices=TariffChoices.choices, max_length=255)
    discount = models.IntegerField(blank=True, default=0)

    description = models.CharField(_('description'), max_length=255, choices=DISCOUNT)
    # tariff = models.CharField(_('tariff'), max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        db_table = "content\".\"privilege"
        verbose_name = _('privilege')
        verbose_name_plural = _('privileges')


class City(UUIDMixin):
    name_city = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name_city

    class Meta:
        db_table = "content\".\"city"
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class Service(UUIDMixin):
    name = models.CharField(_('name'), max_length=255)
    price = models.FloatField(_('price'), blank=True)
    is_optional = models.BooleanField(_('optional'), blank=True)


    class Meta:
        db_table = "content\".\"service"
        verbose_name = _('service')
        verbose_name_plural = _('services')


class Trip(UUIDMixin):
    train = models.ForeignKey(Train, verbose_name=_('train'), on_delete=models.CASCADE, related_name='train')
    city_departure = models.ForeignKey(City, verbose_name=_('city_departure'), on_delete=models.CASCADE, related_name='city_departure')
    city_arrival = models.ForeignKey(City, verbose_name=_('city_arrival'), on_delete=models.CASCADE, related_name='city_arrival')
    way_departure = models.IntegerField(_('way_departure'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    way_arrival = models.IntegerField(_('way_arrival'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    time_departure = models.DateTimeField(auto_now_add=True)
    time_arrival = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([str(self.train), str(self.city_arrival), '-', str(self.city_departure)])

    class Meta:
        db_table = "content\".\"trip"
        verbose_name = _('trip')
        verbose_name_plural = _('trips')


class User(UUIDMixin):
    full_name = models.CharField(_('full_name'), max_length=255)
    docs = models.CharField(_('docs'), max_length=11)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"user"
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Ticket(UUIDMixin):
       
    trip = models.ForeignKey(Trip, verbose_name=_('trip'), on_delete=models.CASCADE, related_name='trip')
    wagon = models.ForeignKey(Wagon, verbose_name=_('wagon'), on_delete=models.CASCADE, related_name='wagon')
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.CASCADE, related_name='user')
    priv = models.ForeignKey(Privilege, verbose_name=_('privilege'), on_delete=models.CASCADE, related_name='privilege')
    price = models.FloatField(_('price'), blank=True)
    place = models.IntegerField(_('place'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(54)])

    def __str__(self):
        return ' '.join([str(self.trip), str(self.user), str(_('place')), str(self.place), str(_('price')), str(self.price)])

    class Meta:
        db_table = "content\".\"ticket"
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')


class Service_to_Ticket(UUIDMixin):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
