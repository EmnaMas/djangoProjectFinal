from .views import *
from django.urls import path
urlpatterns = [
     path('homepage/<int:id>',HomePage,name='HomePage'),
     path('liststatic/',eventStatic,name='eventStatic'),
     path('listevntes/',EventList,name='EventList'),
          path('listevntes/',EventList,name='EventList'),

       path('listevntesview/',EventListClass.as_view(),name='EventListClass')
           path('eventDetailCalss/<int:pk>',EventDetailClass.as_view(),name='EventDetailClass')

]


