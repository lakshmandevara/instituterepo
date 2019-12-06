from django import forms
from multiselectfield import MultiSelectFormField
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )

    )
    feedback=forms.CharField(
            label='Enter Your Feedback',
            widget=forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'your feedback'

                }
            )
    )



class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )

    )
    mobile = forms.IntegerField(
        label='Your Number:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your number'
            }
        )

    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )
    courses = MultiSelectFormField(max_length=200,choices=COURSES_CHOICES)
    SHIFT_CHOICES = (
        ('mrg', 'Morning'),
        ('aftn', 'Afternoon'),
        ('eveng', 'Evening'),
        ('night', 'Night'),
    )
    shifts = MultiSelectFormField(max_length=200,choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('che', 'Chennai'),
        ('pune', 'Pune'),
    )
    locations = MultiSelectFormField(max_length=200,choices=LOCATION_CHOICES)

    GENDER_CHOICES =(
        ('M','Male'),
        ('F','Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICES
    )
    start_date = forms.DateTimeField(
        widget=forms.SelectDateWidget()
    )







