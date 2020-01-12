from django import forms
from .models import Im
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=Im
        fields=['Image']