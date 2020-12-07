class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['lastname'] 
        labels = {'lastname':'Last name'}