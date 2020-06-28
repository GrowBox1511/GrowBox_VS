"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from firebase import Firebase
import firebase

#config = {
#
#    'apiKey': "J2yYL1PfOZtAfRPNQExBjEEgjOPgF5HrUhftgVDz",
#    'authDomain': "rdsbase-4da2c.firebaseio.com",
#    'databaseURL': "https://rdsbase-4da2c.firebaseio.com/",
#    'projectId': "rdsbase-4da2c",
#    'storageBucket': "rdsbase-4da2c.appspot.com",
#    'messagingSenderId': "579985583952"
#    
#    }
#
#firebase = firebase_admin.App(name = '[https://rdsbase-4da2c.firebaseio.com/]', credential = "J2yYL1PfOZtAfRPNQExBjEEgjOPgF5HrUhftgVDz", options = "databaseURL")

#result = firebase.post('qqq')
#repub
config = {
  "apiKey" : "AIzaSyBdTHru5uwyqywTxsv-JWyQCFWIahegowQ",
  "authDomain" : "rdsbase-4da2c.firebaseapp.com",
  "databaseURL" : "https://rdsbase-4da2c.firebaseio.com",
  "projectId" : "rdsbase-4da2c",
  "storageBucket" : "rdsbase-4da2c.appspot.com",
  "messagingSenderId" : "526631168898",
  "appId" : "1:526631168898:web:a4c0b9ee28f3f29468fd9b",
  "measurementId" : "G-46388JY1TT"
}

firebase = Firebase(config)

db = firebase.database()

output = db.child("values").get()


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
