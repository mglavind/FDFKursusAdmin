# Nyt bookingsystem til kurserne i FDF
Dette er et forsøg på at lave et nyt booking system til kurserne indenfor FDF. Det er work-in-progress, så bær over med os!


## Framework
Web appen er bygget som en Django web app. Det er et framework hvor du som udvikler primært arbejder i python, og dermed ikke skal tage så meget stilling til HTML, php eller javascript. Det gør at det programmeringssprog du skal sætte dig ind i primært er python, hvilket er meget udbredt inden for en række grene af programmering, og ikke blot web-udvikling. Dette skulle gøre "bar of entry" lavere for flere. 

Vil du læse mere om Django?: 
https://docs.djangoproject.com/en/4.2/


Skal du bare have installeret Django og komme igang?: 
https://docs.djangoproject.com/en/4.2/intro/install/


Der er også fine tutorials her:
https://www.w3schools.com/django/index.php


## Bootstrap
For at gøre det let at få ting til at se nogenlunde pæne ud, har vi koblet bootstrap på, så du i alt HTML og laypout kan referere til bootstrap elementerne som du finder på dette link:
 hello fra morten

https://getbootstrap.com/docs/5.3/getting-started/introduction/


Det kan dog være at du skal installere det i dit django environment først:


´´´ pip install django-bootstrap-v5 ´´´


## Model access

### Event
You can now create instances of Event and EventMembership to represent events and the membership of users in events. For example:

```
user = CustomUser.objects.get(id=1)
event = Event(name='Scout Camp', start_date='2023-07-01', end_date='2023-07-07')
event.save()
membership = EventMembership(user=user, event=event)
membership.save()
```
This creates an event with the name "Scout Camp" and dates from July 1st to July 7th. It also creates an EventMembership linking the user and the event.
With the Event and EventMembership models in place, you can create, edit, and manage events and their memberships in a similar manner as with the Team and TeamMembership models.



### Teams
With the TeamMembership model in place, you can create instances of TeamMembership to represent the membership of a user in a team. For example:
```
user = CustomUser.objects.get(id=1)
team = Team.objects.get(id=1)
membership = TeamMembership(user=user, team=team, role='Member')
membership.save()
````


You can also access the members of a team and the teams a user belongs to through the TeamMembership model.
To access the members of a team:
```
team = Team.objects.get(id=1)
members = team.teammembership_set.all()
```

To access the teams a user belongs to:
```
user = CustomUser.objects.get(id=1)
teams = user.teammembership_set.all()
```
The teammembership_set is the reverse relation from TeamMembership to Team and CustomUser.
By introducing the TeamMembership model, you have the flexibility to store additional information related to the membership, such as the date joined and the role. You can also easily extend the functionality in the future as needed.