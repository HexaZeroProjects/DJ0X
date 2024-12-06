from django import forms
from .models import Lows_post

class NewsForm(forms.ModelForm):
    class Meta:
        model = Lows_post
        fields = ['title', 'short_description', 'text']  # Убираем pub_date, так как оно автоматически заполняется

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['short_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)

        if user:
            instance.user = user  # Устанавливаем текущего пользователя
        # pub_date устанавливается автоматически, так как у нас auto_now_add=True

        if commit:
            instance.save()

        return instance
