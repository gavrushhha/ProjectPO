from django.db import models
import uuid
import os
from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.translation import gettext_lazy as _

# from django.contrib.auth.models import User


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Train(UUIDMixin):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name"], name="unique_train")]
        db_table = "content\".\"train"
        verbose_name = _('train')
        verbose_name_plural = _('trains')


class WagonChoices(models.TextChoices):
    RESERVED_SEAT = _('reserved seat')
    COUPE = _('coupe')
    SW = _('SW')


class Wagon(UUIDMixin):
    name = models.IntegerField(_('wagon'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(
        int(os.environ.get('MAX_VALUE_WAGON')))])
    train = models.ForeignKey(Train, verbose_name=_('train'), on_delete=models.CASCADE, related_name='train_wagon')
    class_wagon = models.CharField(_('class'), choices=WagonChoices.choices, max_length=255)
    capacity = models.IntegerField(_('capacity'), blank=True,
                                   validators=[MinValueValidator(int(os.environ.get('MIN_VALUE_CAPACITY'))),
                                               MaxValueValidator(int(os.environ.get('MAX_VALUE_CAPACITY')))])

    def __str__(self):
        return ' '.join([str(self.name), '-', str(self.class_wagon)])

    class Meta:
        constraints = [models.UniqueConstraint(fields=["train_id", "name"], name="unique_wagon")]
        db_table = "content\".\"wagon"
        verbose_name = _('wagon')
        verbose_name_plural = _('wagons')


class TariffChoices(models.TextChoices):
    SCHOOL = _('school')
    STUDENTS = _('students')
    CHILDREN = _('children')
    VETERANS = _('veterans')
    PENSIONERS = _('pensioners')
    PERSONS_WITH_DISABILITIES = _('persons with disabilities')


class DiscountChoices(models.IntegerChoices):
    SCHOOL = 50
    STUDENTS = 30
    CHILDREN = 45
    VETERANS = 60
    PENSIONERS = 20
    PERSONS_WITH_DISABILITIES = 15


class DescriptionsChoices(models.TextChoices):
    SCHOOL = _('Pupils of general educational institutions from 10 years and older')
    STUDENTS = _('Students of higher and secondary educational institutions')
    CHILDREN = _('The passenger has the right to carry free* 1 child under the age of 5 years, if he does not occupy '
                 'a separate seat in the carriages')
    VETERANS = _('Combat veterans')
    PENSIONERS = _('Passengers aged 60 and over will be able to travel in a coupe at a discount')
    PERSONS_WITH_DISABILITIES = _('Passengers with disabilities can issue tickets to specialized compartments and '
                                  'carriages with seats')


class Privilege(UUIDMixin):
    category = models.CharField(_('category'), choices=TariffChoices.choices, max_length=255)
    discount = models.FloatField(_('discount'), blank=True, validators=[MinValueValidator(0), MaxValueValidator(
        int(os.environ.get('MAX_VALUE_DISCOUNT')))])
    description = models.CharField(_('description'), blank=True, max_length=255)

    # tariff = models.CharField(_('tariff'), max_length=255)

    def save(self):
        if self.category == TariffChoices.SCHOOL:
            self.discount = DiscountChoices.SCHOOL
            self.description = DescriptionsChoices.SCHOOL
            super().save(self)
            return self.discount

        if self.category == TariffChoices.STUDENTS:
            self.discount = DiscountChoices.STUDENTS
            self.description = DescriptionsChoices.STUDENTS
            super().save(self)
            return self.discount

        if self.category == TariffChoices.CHILDREN:
            self.discount = DiscountChoices.CHILDREN
            self.description = DescriptionsChoices.CHILDREN
            super().save(self)
            return self.discount

        if self.category == TariffChoices.VETERANS:
            self.discount = DiscountChoices.VETERANS
            self.description = DescriptionsChoices.VETERANS
            super().save(self)
            return self.discount

        if self.category == TariffChoices.PENSIONERS:
            self.discount = DiscountChoices.PENSIONERS
            self.description = DescriptionsChoices.PENSIONERS
            super().save(self)
            return self.discount

        if self.category == TariffChoices.PERSONS_WITH_DISABILITIES:
            self.discount = DiscountChoices.PERSONS_WITH_DISABILITIES
            self.description = DescriptionsChoices.PERSONS_WITH_DISABILITIES
            super().save(self)
            return self.discount

    def __str__(self):
        return self.category

    class Meta:
        constraints = [models.UniqueConstraint(fields=["category", "discount"], name="unique_privilege")]
        db_table = "content\".\"privilege"
        verbose_name = _('privilege')
        verbose_name_plural = _('privileges')


class City(UUIDMixin):
    name_city = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name_city

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name_city"], name="unique_city")]
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
        constraints = [models.UniqueConstraint(fields=["name", "price"], name="unique_service")]
        db_table = "content\".\"service"
        verbose_name = _('service')
        verbose_name_plural = _('services')


class Trip(UUIDMixin):
    train = models.ForeignKey(Train, verbose_name=_('train'), on_delete=models.CASCADE, related_name='train')
    city_departure = models.ForeignKey(City, blank=True, verbose_name=_('city_departure'), on_delete=models.CASCADE,
                                       related_name='city_departure')
    city_arrival = models.ForeignKey(City, blank=True, verbose_name=_('city_arrival'), on_delete=models.CASCADE,
                                     related_name='city_arrival')
    way_departure = models.IntegerField(_('way_departure'), blank=True, validators=[MinValueValidator(1),
                                                                                    MaxValueValidator(
                                                                                        int(os.environ.get(
                                                                                            'MAX_VALUE_WAY')))])
    way_arrival = models.IntegerField(_('way_arrival'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(
        int(os.environ.get('MAX_VALUE_WAY')))])
    time_departure = models.DateTimeField()
    time_arrival = models.DateTimeField()

    def __str__(self):
        return ' '.join([str(self.train), str(self.city_departure), '-', str(self.city_arrival)])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["train_id", "city_departure", "city_arrival"], name="unique_trip")]
        db_table = "content\".\"trip"
        verbose_name = _('trip')
        verbose_name_plural = _('trips')


class Person(UUIDMixin):
    username = models.CharField(_('username'), max_length=255)
    docs = models.CharField(_('docs'), max_length=11)
    email = models.EmailField(_('email'), max_length=255)

    def __str__(self):
        return ' '.join([str(self.username), str(self.email)])

    class Meta:
        constraints = [models.UniqueConstraint(fields=["username", "docs"], name="unique_user")]
        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('person')


class Ticket(UUIDMixin):
    trip = models.ForeignKey(Trip, verbose_name=_('trip'), on_delete=models.CASCADE, related_name='trip')
    wagon = models.ForeignKey(Wagon, verbose_name=_('wagon'), on_delete=models.CASCADE, related_name='wagon')
    user = models.ForeignKey(Person, verbose_name=_('person'), on_delete=models.CASCADE, related_name='person')
    priv = models.ForeignKey(Privilege, verbose_name=_('privilege'), on_delete=models.CASCADE, related_name='privilege')
    price = models.FloatField(_('price'), blank=True)
    place = models.IntegerField(_('place'), blank=True, validators=[MinValueValidator(1), MaxValueValidator(
        int(os.environ.get('MAX_VALUE_PLACE')))])

    def __str__(self):
        return ' '.join([str(self.trip), str(self.user)])

    class Meta:
        constraints = [models.UniqueConstraint(fields=["wagon", "trip", "place"], name="unique_ticket")]
        db_table = "content\".\"ticket"
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')


class Service_to_Ticket(UUIDMixin):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
