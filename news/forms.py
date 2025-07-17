from django import forms

from news.models import Category, New


class AddNewsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      queryset=Category.objects.all())

    class Meta:
        model = New
        fields = ['title', 'image', 'content', 'category']


class NewsFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Qidiruv',
        widget=forms.TextInput(attrs={
            'placeholder': 'Sarlavha yoki matndan izlash...',
            'class': 'form-control'
        })
    )
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Kategoriya',
        empty_label='Barcha kategoriyalar',
        widget=forms.Select(attrs={'class': 'form-control'})
    )