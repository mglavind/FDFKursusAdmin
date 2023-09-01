from django import forms
from Butikken.models import ButikkenItemType, ButikkenItem, Day, Meal, Option, Recipe
from organization.models import Team, TeamMembership, Volunteer
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


class MealBookingForm(forms.ModelForm):
    class Meta:
        model = models.MealBooking
        fields = [
            "monday_breakfast",
            "monday_lunch",
            "monday_dinner",

            "tuesday_breakfast",
            "tuesday_lunch",
            "tuesday_dinner",

            "wednesday_breakfast",
            "wednesday_lunch",
            "wednesday_dinner",

            "thursday_breakfast",
            "thursday_lunch",
            "thursday_dinner",

            "friday_breakfast",
            "friday_lunch",
            "friday_dinner",

            "team_contact",
            "team",
        ]
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
            ('Vælg fra liste', 'Vælg fra liste'), 
            ('Spiser inde ', 'Spiser inde '),
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

        monday_breakfast = forms.ChoiceField(choices=MONDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        monday_lunch = forms.ChoiceField(choices=MONDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        monday_dinner = forms.ChoiceField(choices=MONDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

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

        tuesday_breakfast = forms.ChoiceField(choices=TUESDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        tuesday_lunch = forms.ChoiceField(choices=TUESDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        tuesday_dinner = forms.ChoiceField(choices=TUESDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



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

        wednesday_breakfast = forms.ChoiceField(choices=WEDNESDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        wednesday_lunch = forms.ChoiceField(choices=WEDNESDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        wednesday_dinner = forms.ChoiceField(choices=WEDNESDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



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

        thursday_breakfast = forms.ChoiceField(choices=THURSDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        thursday_lunch = forms.ChoiceField(choices=THURSDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        thursday_dinner = forms.ChoiceField(choices=THURSDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



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

        friday_breakfast = forms.ChoiceField(choices=FRIDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        friday_lunch = forms.ChoiceField(choices=FRIDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        friday_dinner = forms.ChoiceField(choices=FRIDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance
    
    def __init__(self, *args, user=None, **kwargs):
        super(MealBookingForm, self).__init__(*args, **kwargs)
        self.fields["team_contact"].queryset = Volunteer.objects.all().order_by("first_name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        
        if user:
            try:
                team_membership = TeamMembership.objects.get(member=user)
                self.fields["team"].initial = team_membership.team
                self.fields["team_contact"].queryset = Volunteer.objects.filter(
                    teammembership__team=team_membership.team
                )
            except TeamMembership.DoesNotExist:
                pass
            
            self.fields["team_contact"].initial = user
            


class MealForm(forms.ModelForm):
    class Meta:
        model = models.Meal
        fields = [
            "type",
            "day",
        ]

    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        self.fields["day"].queryset = Day.objects.all()

class OptionForm(forms.ModelForm):
    class Meta:
        model = models.Option
        fields = [
            "meal",
            "recipe",
        ]

    def __init__(self, *args, **kwargs):
        super(OptionForm, self).__init__(*args, **kwargs)
        self.fields["meal"].queryset = Meal.objects.all()
        self.fields["recipe"].queryset = Recipe.objects.all()



class DayForm(forms.ModelForm):
    class Meta:
        model = models.Day
        fields = [
            "name",
            "date",
        ]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = [
            "name",
            "description",
        ]

class ButikkenItemForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItem
        fields = [
            "description",
            "name",
            "type",
            "content_normal",
            "content_unit",
        ]

    def __init__(self, *args, **kwargs):
        super(ButikkenItemForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = ButikkenItemType.objects.all()



class ButikkenBookingForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenBooking
        fields = [
            "remarks",
            "quantity",
            "start",
            "item",
            "team_contact",
            "team",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        super(ButikkenBookingForm, self).__init__(*args, **kwargs)
        self.fields["item"].queryset = ButikkenItem.objects.all().order_by("name")
        self.fields["team_contact"].queryset = Volunteer.objects.all().order_by("first_name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")
        
        if user:
            try:
                team_membership = TeamMembership.objects.get(member=user)
                self.fields["team"].initial = team_membership.team
                self.fields["team_contact"].queryset = Volunteer.objects.filter(
                    teammembership__team=team_membership.team
                )
            except TeamMembership.DoesNotExist:
                pass
            
            self.fields["team_contact"].initial = user
            
            # Set initial values from instance
            instance = kwargs.get('instance')
            if instance:
                self.fields["quantity"].initial = instance.quantity
                self.fields["start"].initial = instance.start

                # Add other fields similarly



class ButikkenItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItemType
        fields = [
            "name",
            "description",
        ]
