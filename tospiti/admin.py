from django.contrib import admin
from .models import Agent, Property, Prop_Genre, Prop_Picture, Prop_Category, Prop_Facility, Facility


class Prop_PictureInline(admin.TabularInline,):
    model = Prop_Picture
    verbose_name = "Εικόνα"
    verbose_name_plural = "Εικόνες"
    max_num = 10
    extra = 3

class FacilityInline(admin.TabularInline,):
    model = Facility


class Prop_FacilityInline(admin.TabularInline,):
    model = Prop_Facility
    verbose_name = "Χαρακτηριστικο"
    verbose_name_plural = "Χαρακτηριστικα"
    extra = 5

    inlines = [FacilityInline]

class PropAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'address', 'prop_genre', 'prop_category', 'price', 'agent')
    list_filter = ('country', 'prop_genre','prop_category', 'agent')
    search_fields = ('city', 'address')
    list_display_links = ('country', 'city', 'address', 'prop_genre', 'prop_category', 'price', 'agent')

    list_per_page = 30

    fieldsets = [
        ('Ημερομινία Δημιουργίας/Δημοσίευσης', {'fields': [('created_date','publised_date')]}),
        ('Βασικά',{'fields':[('prop_category') , ('prop_genre'), ('agent') ,('price', 'squaremeters')]}),
        ('Περιοχή', {'fields': [('country'), ('region', 'city'), ('address', 'zipcode')]}),
        ('Χώροι', {'fields':[('rooms', 'bedrooms'), ('bathrooms', 'area')]}),
        ('Σύντομη Περιγραφή', {
            'classes': ('collapse',),
            'fields':('description',)
                              }),
    ]
    inlines = [Prop_PictureInline, Prop_FacilityInline]
    save_on_top = True

admin.site.register(Property, PropAdmin)

admin.site.register(Agent)
admin.site.register(Prop_Genre)
admin.site.register(Prop_Category)
admin.site.register(Facility)

