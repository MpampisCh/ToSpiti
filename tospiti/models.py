from django.db import models
import os
from django.utils import timezone

def get_image_path(instance, filename):
    return os.path.join('tospiti/media/', str(instance.id), filename)

class Agent(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    id_ag = models.AutoField(primary_key = True)
    firstname = models.CharField(max_length=255, blank = True, null = True)
    lastname = models.CharField(max_length=255, blank = True, null = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank = True, null = True)
    phonenumber = models.CharField(max_length=255, blank = True, null = True)
    email = models.CharField(max_length=255, blank = True, null = True)
    picture = models.ImageField(upload_to="agentPicture", blank = True, null = True)

    class Meta:
        verbose_name = 'Μεσίτης'
        verbose_name_plural = 'Μεσίτες'

    def __str__(self):
        return self.lastname + " " + self.firstname

    def getFullName(self):
        title = ""
        if (self.gender == 'M'):
            title = 'κος '
        elif (self.gender == 'F'):
            title = "κα "

        return title + self.lastname + " " + self.firstname

class Property(models.Model):
    id_prop = models.AutoField(primary_key = True)
    prop_category = models.ForeignKey('Prop_Category', related_name='properties',verbose_name='Είδος κατοικίας')
    prop_genre = models.ForeignKey('Prop_Genre', related_name='properties', verbose_name='Προς')
    price = models.FloatField(blank=True, null=True, verbose_name='Τιμή')
    squaremeters = models.IntegerField(blank=True, null=True, verbose_name='Τετραγωνικά')
    rooms = models.IntegerField(blank=True, null=True, verbose_name='Δωμάτια')
    bedrooms = models.IntegerField(blank=True, null=True, verbose_name='Υπνοδωμάτια')
    bathrooms = models.IntegerField(blank=True, null=True, verbose_name='Μπάνια')
    area = models.FloatField(blank=True, null=True, verbose_name='Χώροι')
    description = models.TextField(blank=True, null=True, verbose_name='Σύντομη περιγραφή')

    country = models.CharField(max_length=255, blank=True, null=True, verbose_name='Χώρα')
    region = models.CharField(max_length=255, blank=True, null=True, verbose_name='Νομός')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='Πόλη')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Διεύθυνση')
    zipcode = models.CharField(max_length=255, blank=True, null=True, verbose_name='Τ.Κ.')

    agent = models.ForeignKey('Agent', related_name='properties', verbose_name='Μεσίτης')

    created_date = models.DateTimeField(default=timezone.now, verbose_name='Ημερομηνία Δημιουργίας')
    publised_date = models.DateTimeField(blank=True, null=True, verbose_name='Ημερομινία Δημοσίευσης')

    class Meta:
        verbose_name = 'Ακινήτο'
        verbose_name_plural = 'Ακίνητα'

    def publised(self):
        self.publised_date = timezone.now()
        self.save()

    def __str__(self):
        return self.country

class Prop_Category(models.Model):
    id_prop_cat = models.AutoField(primary_key = True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Κατηγορία Ακινήτου'
        verbose_name_plural = 'Κατηγορίες Ακινήτων'

    def __str__(self):
        return self.description

class Prop_Genre(models.Model):
    id_prop_gen = models.AutoField(primary_key = True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ακίνητο προς'
        verbose_name_plural = 'Ακίνητα προς'

    def __str__(self):
        return self.description

class Prop_Picture(models.Model):
    id_prop_pic = models.AutoField(primary_key = True)
    property = models.ForeignKey(Property, related_name='pictures')
    picture = models.ImageField(upload_to="Prop_Picture", blank = True, null = True)

    class Meta:
        verbose_name = 'Εικόνα'
        verbose_name_plural = 'Εικόνες'

class Facility(models.Model):
    id_fac = models.AutoField(primary_key = True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Επιπρόσθετο στοιχείο'
        verbose_name_plural = 'Επιπρόσθετα στοιχεία'

    def __str__(self):
        return self.description


class Prop_Facility(models.Model):
    id_prop_fac = models.AutoField(primary_key = True)
    property = models.ForeignKey('Property', related_name='prop_facilities')
    facility = models.ForeignKey('Facility', related_name='prop_facilities')

    class Meta:
        verbose_name = 'Property_Facility'
        verbose_name_plural = 'Property_Facilities'
