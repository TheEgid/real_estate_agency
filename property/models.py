from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    created_at = models.DateTimeField("Когда создано объявление",
                                      default=timezone.now,
                                      db_index=True)

    description = models.TextField("Текст объявления",
                                   blank=True)
    price = models.IntegerField("Цена квартиры",
                                db_index=True)

    town = models.CharField("Город, где находится квартира",
                            max_length=50,
                            db_index=True)

    town_district = models.CharField("Район города, где находится квартира",
                                     max_length=50,
                                     blank=True,
                                     help_text='Чертаново Южное')

    address = models.TextField("Адрес квартиры",
                               help_text='ул. Подольских курсантов д.5 кв.4')

    floor = models.CharField("Этаж",
                             max_length=3,
                             null=True,
                             blank=True,
                             help_text=
                             'Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField("Количество комнат в квартире",
                                       db_index=True)

    living_area = models.IntegerField("количество жилых кв.метров",
                                      null=True,
                                      blank=True,
                                      db_index=True)

    has_balcony = models.NullBooleanField("Наличие балкона",
                                          db_index=True)

    active = models.BooleanField("Активно-ли объявление",
                                 db_index=True)

    construction_year = models.IntegerField("Год постройки здания",
                                            null=True,
                                            blank=True,
                                            db_index=True)

    new_building = models.NullBooleanField("Дом является новостройкой",
                                           db_index=True)

    liked_by = models.ManyToManyField(User,
                                      related_name="liked_flat",
                                      db_index=True,
                                      blank=True,
                                      verbose_name='Кто лайкнул')

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Claim(models.Model):
    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"

    created_at = models.DateTimeField("Когда созданa жалоба",
                                      default=timezone.now,
                                      db_index=True)

    user = models.ForeignKey(User, blank=False, null=False,
                             related_name='user_claims',
                             verbose_name='Кто жаловался',
                             on_delete=models.CASCADE)

    flat = models.ForeignKey(Flat, blank=False, null=False,
                             verbose_name='Квартира, на которую пожаловались',
                             related_name='flat_claims',
                             db_index=True,
                             on_delete=models.CASCADE)

    claim_text = models.TextField("Текст жалобы",
                                  blank=True,
                                  null=True)




    def __str__(self):
        return f'Жалоба на квартиру: {self.flat} от {self.user}'


class Owner(models.Model):
    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

    owner_name = models.CharField("ФИО владельца",
                                  max_length=200,
                                  db_index=True)

    owners_phonenumber = models.CharField("Номер владельца",
                                          max_length=20,
                                          null=True,
                                          blank=True,
                                          db_index=True)

    owner_phone_pure = PhoneNumberField("Нормализированный номер владельца",
                                        max_length=20,
                                        null=True,
                                        blank=True,
                                        db_index=True)

    flats = models.ManyToManyField(Flat,
                                   related_name="flats_owners",
                                   db_index=True,
                                   blank=True,
                                   verbose_name='Квартиры в собственности')

    def __str__(self):
        return f' {self.owner_name} {self.owner_phone_pure}'

