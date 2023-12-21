# Import necessary modules for creating Django forms.
from django import forms

# Import the 'Video' model from the 'models' module of the 'video_app'.
from .models import Video

# Define a Django form named 'VideoUploadForm' for uploading video files.
class VideoUploadForm(forms.ModelForm):
    class Meta:
        # Associate the form with the 'Video' model and specify the fields to include.
        model = Video
        fields = ['video_file']

    def __init__(self, *args, **kwargs):
        super(VideoUploadForm, self).__init__(*args, **kwargs)
        # Customize form field attributes.
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if field_name == 'video_file':
                field.widget.attrs.update({'placeholder': 'Upload Video'})

    # Define a 'video_file' field as a FileField with specific attributes.
    video_file = forms.FileField(
        label='',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
