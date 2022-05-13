from pydoc import describe
from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from matplotlib.style import available
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UUIDMixin(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

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

class Wagon(UUIDMixin):
    name = models.CharField(_('wagon'), max_length=255)
    train  = models.ForeignKey(Train, verbose_name=_('train'), on_delete=models.CASCADE, related_name='train_wagon')
    class_wagon = models.CharField(_('class'), max_length=255)
    capacity = models.IntegerField(_('capacity'), blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"wagon"
        verbose_name = _('wagon')
        verbose_name_plural = _('wagons')

class Privilege(UUIDMixin):
    category = models.CharField(_('category'), max_length=255)
    discount = models.FloatField(_('discount'), blank=True, \
    validators=[MinValueValidator(0), MaxValueValidator(100)])
    description  = models.CharField(_('description'), max_length=255)
    tariff = models.CharField(_('tariff'), max_length=255)

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


    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"service"
        verbose_name = _('service')
        verbose_name_plural = _('services')

class Trip(UUIDMixin):
    train  = models.ForeignKey(Train, on_delete=models.CASCADE, related_name=_('train_trip+'))
    city_departure = models.ForeignKey(City, verbose_name=_('city_departure'), on_delete=models.CASCADE, related_name='city_departure')
    city_arrival = models.ForeignKey(City, verbose_name=_('city_arrival'), on_delete=models.CASCADE, related_name='city_arrival')
    way_departure = models.IntegerField(_('way_departure'), blank=True)
    way_arrival =  models.IntegerField(_('way_arrival'), blank=True)
    time_departure = models.DateTimeField(auto_now_add=True)
    time_arrival = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.train + " " + self.city_arrival + " " + self.city_departure

    class Meta:
        db_table = "content\".\"trip"
        verbose_name = _('trip')
        verbose_name_plural = _('trips')

class User(UUIDMixin):
    full_name = models.CharField(_('full_name'), max_length=255)
    docs = models.IntegerField(_('docs'), blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"user"
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Ticket(UUIDMixin):
    trip  = models.ForeignKey(Trip, verbose_name=_('trip'), on_delete=models.CASCADE, related_name='trip')
    wagon  = models.ForeignKey(Wagon, verbose_name=_('wagon'), on_delete=models.CASCADE, related_name='wagon')
    user  = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.CASCADE, related_name='user')
    priv  = models.ForeignKey(Privilege, verbose_name=_('privilege'), on_delete=models.CASCADE, related_name='privilege')

    price = models.FloatField(_('price'), blank=True)

    availability = models.BooleanField(_('availability'), blank=True)

    place = models.IntegerField(_('place'), blank=True)

    # def __str__(self):
    #     return self.price

    class Meta:
        db_table = "content\".\"ticket"
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')



class Service_to_Ticket(UUIDMixin):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)












