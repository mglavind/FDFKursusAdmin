from django import forms
from Butikken.models import ButikkenItemType, ButikkenItem, Day, Meal, Option, Recipe
from organization.models import Team, TeamMembership, Volunteer, Event
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import BaseFormSet, TextInput, formset_factory
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class MealBookingForm(forms.ModelForm):
    class Meta:
        model = models.MealBooking
        fields = [


            "thursday_breakfast",
            "thursday_lunch",
            "thursday_dinner",

            "friday_breakfast",
            "friday_lunch",
            "friday_dinner",

            "saturday_breakfast",
            "saturday_lunch",
            "saturday_dinner",

            "sunday_breakfast",
            "sunday_lunch",
            "sunday_dinner",

            "team_contact",
            "team",
        ]
        THURSDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), 
        ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        THURSDAY_LUNCH_CHOICES = (
            ('Vælg fra liste', 'Vælg fra liste'),
            ('Spiser inde ', 'Spiser inde '),
            ('Frokostpakke', 'Frokostpakke'),
            ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        THURSDAY_DINNER_CHOICES   = (
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

        thursday_breakfast = forms.ChoiceField(choices=THURSDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        thursday_lunch = forms.ChoiceField(choices=THURSDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        thursday_dinner = forms.ChoiceField(choices=THURSDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

        FRIDAY_BREAKFAST_CHOICES = (
            ('Vælg fra liste', 'Vælg fra liste'), 
            ('Spiser inde ', 'Spiser inde '),
            ('Morgenmadspakke', 'Morgenmadspakke'),
            ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        FRIDAY_LUNCH_CHOICES = (
            ('Vælg fra liste', 'Vælg fra liste'), 
            #('Spiser inde ', 'Spiser inde '),
            ('Frokostpakke', 'Frokostpakke'),
            ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        FRIDAY_DINNER_CHOICES   = (
            ('Vælg fra liste', 'Vælg fra liste'), 
            #('Spiser inde ', 'Spiser inde '),
            ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'),
            #('Dinner trans', 'Dinner trans'),
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


        SATURDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        SATURDAY_LUNCH_CHOICES = (
            ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
            ('Frokostpakke', 'Frokostpakke'),
            ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        SATURDAY_DINNER_CHOICES   = (
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

        saturday_breakfast = forms.ChoiceField(choices=SATURDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        saturday_lunch = forms.ChoiceField(choices=SATURDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        saturday_dinner = forms.ChoiceField(choices=SATURDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


        SUNDAY_BREAKFAST_CHOICES = (
        ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
        ('Morgenmadspakke', 'Morgenmadspakke'),
        ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        SUNDAY_LUNCH_CHOICES = (
            ('Vælg fra liste', 'Vælg fra liste'), ('Spiser inde ', 'Spiser inde '),
            ('Frokostpakke', 'Frokostpakke'),
            ('Står selv for forplejning', 'Står selv for forplejning'),
        )
        SUNDAY_DINNER_CHOICES   = (
            ('Fællesforplejning', 'Fællesforplejning'),
        )

        sunday_breakfast = forms.ChoiceField(choices=SUNDAY_BREAKFAST_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        sunday_lunch = forms.ChoiceField(choices=SUNDAY_LUNCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        sunday_dinner = forms.ChoiceField(choices=SUNDAY_DINNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
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
    start = forms.DateField(
        widget=TextInput(attrs={"type": "date"}),
        initial=Event.objects.filter(is_active=True).first().start_date
    )
    class Meta:
        model = models.ButikkenBooking
        fields = fields = '__all__' 

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"

        if commit:
            instance.save()

        return instance
    
    def __init__(self, *args, user=None, **kwargs):
        print("Initializing ButikkenBookingForm")  # Print to terminal when the method is called
        print("Current user: 0", user) 
        #user = kwargs.pop('user', None)
        self.user = user  # Assign the user argument to the form's user attribute
        print("Current user: 1", user)  # Print to terminal the current user

        super(ButikkenBookingForm, self).__init__(*args, **kwargs)

        if self.user is not None:
            print("Current user: 2", self.user)  # Print to terminal the current user
            team = Team.objects.filter(teammembership__member=self.user).first()
            print("Teams:", team)  # Print to terminal the current user

            self.fields['team_contact'].queryset = Volunteer.objects.filter(teammembership__team=team)
            self.fields['team_contact'].initial = self.user  # Set the default value to be the user object

            self.fields["team"].queryset = Team.objects.filter(teammembership__member=self.user)
            self.fields["team"].initial = team
            
        self.fields["start"].initial = Event.objects.filter(is_active=True).first()
        self.fields["item"].queryset = ButikkenItem.objects.all().order_by("name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")


class OldButikkenBookingForm(forms.ModelForm):
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

        widgets = {
            "item": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "start": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "remarks": forms.Textarea(attrs={"class": "form-control h-25"}),
            "team_contact": forms.Select(attrs={"class": "form-control"}),
            "team": forms.Select(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = "Pending"
        instance.team_contact = self.user
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, user=None, **kwargs):
        print("Initializing ButikkenBookingForm")  # Print to terminal when the method is called
        print("Current user: 0", user) 
        #user = kwargs.pop('user', None)
        self.user = user  # Assign the user argument to the form's user attribute
        print("Current user: 1", user)  # Print to terminal the current user

        super(ButikkenBookingForm, self).__init__(*args, **kwargs)

        if self.user is not None:
            print("Current user: 2", self.user)  # Print to terminal the current user
            team = Team.objects.filter(teammembership__member=self.user).first()
            print("Teams:", team)  # Print to terminal the current user

            self.fields['team_contact'].queryset = Volunteer.objects.filter(teammembership__team=team)
            self.fields['team_contact'].initial = self.user  # Set the default value to be the user object

            self.fields["team"].queryset = Team.objects.filter(teammembership__member=self.user)
            self.fields["team"].initial = team
            
        self.fields["start"].initial = Event.objects.filter(is_active=True).first()
        self.fields["item"].queryset = ButikkenItem.objects.all().order_by("name")
        self.fields["team"].queryset = Team.objects.all().order_by("name")



class ButikkenItemTypeForm(forms.ModelForm):
    class Meta:
        model = models.ButikkenItemType
        fields = [
            "name",
            "description",
        ]
