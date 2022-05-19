from django import forms
from index.models import Audio

class SaveAudio(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['song_name','singer','category','song_image','song_file', 'song_lrc','upload_user','song_release']
    def __init__(self, *args, **kwargs):
        super(SaveAudio, self).__init__(*args, **kwargs)
        self.fields['song_name'].widget = forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '音乐名', 'id':'song_name'})
        self.fields['singer'].widget = forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '歌手','id':'singer'})
        self.fields['song_image'].widget = forms.widgets.FileInput(attrs={'id':'exampleInputFile1'})
        self.fields['song_file'].widget = forms.widgets.FileInput(attrs={'id':'exampleInputFile2'})
        self.fields['song_lrc'].widget = forms.widgets.FileInput(attrs={'id': 'exampleInputFile3'})