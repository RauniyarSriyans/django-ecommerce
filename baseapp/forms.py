from django import forms 
from baseapp.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Please add your review here."}))
    
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']