from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition', 'quantity', 'rating', 'pubdate', 'publisher']
        labels = {'pubdate': 'Publication date'}
        widgets = {'pubdate': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')}

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError('Quantity cannot be negative.')
        return quantity

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating
