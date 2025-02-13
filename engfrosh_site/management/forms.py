from django import forms
from common_models.models import Puzzle
from schedule.models import Event, Calendar
from django.contrib.auth.models import User


class AnnouncementForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    body = forms.CharField(label='Body', widget=forms.Textarea)


class DiscordNickForm(forms.Form):
    nickname = forms.CharField(label="Nickname", max_length=60)
    # 979c9f is the default discord role color
    color = forms.CharField(initial="#979c9f", widget=forms.TextInput(attrs={'type': 'color'}))

    def __init__(self, *args, nick=None, col=None, **kwargs):
        super(DiscordNickForm, self).__init__(*args, **kwargs)

        if nick is not None:
            self.fields['nickname'].value = nick
        if col is not None:
            self.fields['color'].value = col


class LockForm(forms.Form):
    duration = forms.IntegerField(label="Durations (mins)")


class HintForm(forms.Form):
    free_hints = forms.IntegerField(label="Free Hints")


class PuzzleForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        exclude = ['id', 'secret_id', 'created_at']


class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['calendar'].queryset = Calendar.objects.exclude(name__in=User.objects.all().values('username'))

    class Meta:
        model = Event
        fields = ['start', 'end', 'title', 'description', 'calendar', 'color_event']
        widgets = {
            "start": forms.DateTimeInput(),
            "end": forms.DateTimeInput(),
        }
