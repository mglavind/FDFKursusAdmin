from django.db import models
from django.urls import reverse
from django.utils import timezone
from organization.models import Team, Volunteer

class ButikkenItem(models.Model):

    # Relationships
    type = models.CharField(max_length=100)

    # Fields
    description = models.TextField(max_length=500, blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=100)
    content_normal = models.CharField(max_length=100, blank=True)
    content_unit = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Butikken_ButikkenItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_ButikkenItem_update", args=(self.pk,))
    
class ButikkenBooking(models.Model):
    

    # Relationships
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)
    item = models.ForeignKey("Butikken.ButikkenItem", on_delete=models.CASCADE)
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)


    # Fields
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Udleveret', 'Udleveret'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    start = models.DateTimeField(verbose_name='Start')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    remarks = models.TextField(blank=True)  # Blank allows for an empty value

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Butikken_ButikkenBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_ButikkenBooking_update", args=(self.pk,))



class ButikkenItemType(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Butikken_ButikkenItemType_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_ButikkenItemType_update", args=(self.pk,))



class Day(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    date = models.DateField()

    created = models.DateTimeField(default=timezone.now, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Butikken_Day_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_Day_update", args=(self.pk,))

class Meal(models.Model):
    DAY_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    # Relationships
    day = models.ForeignKey("Butikken.Day", on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=DAY_CHOICES)

    created = models.DateTimeField(default=timezone.now, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Butikken_Meal_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_Meal_update", args=(self.pk,))

class Recipe(models.Model):
    
    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(default=timezone.now, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Butikken_Recipe_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_Recipe_update", args=(self.pk,))

class Option(models.Model):

    # Relationships
    meal = models.ForeignKey("Butikken.Meal", on_delete=models.CASCADE)
    recipe = models.ForeignKey("Butikken.Recipe", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(default=timezone.now, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Butikken_Option_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_Option_update", args=(self.pk,))

class MealBooking(models.Model):

    # Relationships
    team_contact = models.ForeignKey("organization.Volunteer", on_delete=models.CASCADE)
    team = models.ForeignKey("organization.Team", on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    # Fields
    MONDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), 
        ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    MONDAY_LUNCH_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), 
        ('Spiser inde ', 'Spiser inde '),
        ('Frokostpakke', 'Frokostpakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    MONDAY_DINNER_CHOICES   = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'),
        ('Dinner trans', 'Dinner trans'),
        ('DYI - Chili Con Carne med ris / Råkost', 'DYI - Chili Con Carne med ris / Råkost'),
        ('DYI - Ciabatta med kylling og bacon', 'DYI - Ciabatta med kylling og bacon'),
        ('DYI - Indisk Kartoffelcurry / Råkost', 'DYI - Indisk Kartoffelcurry / Råkost'),
        ('DYI - Jambalaya / Spidskålssalat', 'DYI - Jambalaya / Spidskålssalat'),
        ('DYI - Pasta kødsovs / Spidskålssalat', 'DYI - Pasta kødsovs / Spidskålssalat'),
        ('DYI - Svensk pølseret / Spidskålssalat', 'DYI - Svensk pølseret / Spidskålssalat'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    monday_breakfast = models.CharField(max_length=200, choices=MONDAY_BREAKFAST_CHOICES, default="none")
    monday_lunch = models.CharField(max_length=200, choices=MONDAY_LUNCH_CHOICES, default="none")
    monday_dinner = models.CharField(max_length=200, choices=MONDAY_DINNER_CHOICES, default="none")

    # Fields
    TUESDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    TUESDAY_LUNCH_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Frokostpakke', 'Frokostpakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    TUESDAY_DINNER_CHOICES   = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'),
        ('Dinner trans', 'Dinner trans'),
        ('DYI - Chili Con Carne med ris / Råkost', 'DYI - Chili Con Carne med ris / Råkost'),
        ('DYI - Ciabatta med kylling og bacon', 'DYI - Ciabatta med kylling og bacon'),
        ('DYI - Indisk Kartoffelcurry / Råkost', 'DYI - Indisk Kartoffelcurry / Råkost'),
        ('DYI - Jambalaya / Spidskålssalat', 'DYI - Jambalaya / Spidskålssalat'),
        ('DYI - Pasta kødsovs / Spidskålssalat', 'DYI - Pasta kødsovs / Spidskålssalat'),
        ('DYI - Svensk pølseret / Spidskålssalat', 'DYI - Svensk pølseret / Spidskålssalat'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    tuesday_breakfast = models.CharField(max_length=200, choices=TUESDAY_BREAKFAST_CHOICES, default="none")
    tuesday_lunch = models.CharField(max_length=200, choices=TUESDAY_LUNCH_CHOICES, default="none")
    tuesday_dinner = models.CharField(max_length=200, choices=TUESDAY_DINNER_CHOICES, default="none")

    # Fields
    WEDNESDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    WEDNESDAY_LUNCH_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Frokostpakke', 'Frokostpakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    WEDNESDAY_DINNER_CHOICES   = (
        ('Vælg fra liste', 'Vælg fra liste'),
        ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'),
        ('DYI - Chili Con Carne med ris / Råkost', 'DYI - Chili Con Carne med ris / Råkost'),
        ('DYI - Ciabatta med kylling og bacon', 'DYI - Ciabatta med kylling og bacon'),
        ('DYI - Indisk Kartoffelcurry / Råkost', 'DYI - Indisk Kartoffelcurry / Råkost'),
        ('DYI - Jambalaya / Spidskålssalat', 'DYI - Jambalaya / Spidskålssalat'),
        ('DYI - Pasta kødsovs / Spidskålssalat', 'DYI - Pasta kødsovs / Spidskålssalat'),
        ('DYI - Svensk pølseret / Spidskålssalat', 'DYI - Svensk pølseret / Spidskålssalat'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    wednesday_breakfast = models.CharField(max_length=200, choices=WEDNESDAY_BREAKFAST_CHOICES, default="none")
    wednesday_lunch = models.CharField(max_length=200, choices=WEDNESDAY_LUNCH_CHOICES, default="none")
    wednesday_dinner = models.CharField(max_length=200, choices=WEDNESDAY_DINNER_CHOICES, default="none")

     # Fields
    THURSDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    THURSDAY_LUNCH_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Frokostpakke', 'Frokostpakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    THURSDAY_DINNER_CHOICES   = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'),
        ('Dinner trans', 'Dinner trans'),
        ('DYI - Chili Con Carne med ris / Råkost', 'DYI - Chili Con Carne med ris / Råkost'),
        ('DYI - Ciabatta med kylling og bacon', 'DYI - Ciabatta med kylling og bacon'),
        ('DYI - Indisk Kartoffelcurry / Råkost', 'DYI - Indisk Kartoffelcurry / Råkost'),
        ('DYI - Jambalaya / Spidskålssalat', 'DYI - Jambalaya / Spidskålssalat'),
        ('DYI - Pasta kødsovs / Spidskålssalat', 'DYI - Pasta kødsovs / Spidskålssalat'),
        ('DYI - Svensk pølseret / Spidskålssalat', 'DYI - Svensk pølseret / Spidskålssalat'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    thursday_breakfast = models.CharField(max_length=200, choices=THURSDAY_BREAKFAST_CHOICES, default="none")
    thursday_lunch = models.CharField(max_length=200, choices=THURSDAY_LUNCH_CHOICES, default="none")
    thursday_dinner = models.CharField(max_length=200, choices=THURSDAY_DINNER_CHOICES, default="none")
    
    # Fields
    FRIDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    FRIDAY_LUNCH_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Frokostpakke', 'Frokostpakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
    )
    FRIDAY_DINNER_CHOICES   = (
        ('Fællesforplejning', 'Fællesforplejning'), 
    )
    friday_breakfast = models.CharField(max_length=200, choices=FRIDAY_BREAKFAST_CHOICES, default="none")
    friday_lunch = models.CharField(max_length=200, choices=FRIDAY_LUNCH_CHOICES, default="none")
    friday_dinner = models.CharField(max_length=200, choices=FRIDAY_DINNER_CHOICES, default="none")

    last_updated = models.DateTimeField(auto_now=True, editable=False) 
    created = models.DateTimeField(auto_now_add=True, editable=False)
    

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Butikken_MealBooking_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Butikken_MealBooking_update", args=(self.pk,))