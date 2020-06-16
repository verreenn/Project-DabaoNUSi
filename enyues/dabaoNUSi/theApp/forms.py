from django import forms
from  .models import Comment, Rate

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('rating',)