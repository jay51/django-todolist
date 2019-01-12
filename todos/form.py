# We need the form class
from django import forms
import datetime

from .models import Todos

# Form class describes a form and determines how it works and appears same way that.
# Django model describes the logical structure of an object, its behavior, and the way its parts are represented to us


class AddTodo(forms.ModelForm):

    class Meta:
        model = Todos
        fields = [
            "Todo",
            "summery",
            "done"
        ]

    # if label omitted Django would use the name of filed as label
    # todo = forms.CharField(label="Todo", max_length=180)
    # day = forms.DateField(initial=datetime.date.today)
    # summery = forms.CharField(
    #     max_length=2000,
    #     widget=forms.Textarea(),
    #     help_text='Write here your message!'
    # )
    # done = forms.BooleanField(required=False)
