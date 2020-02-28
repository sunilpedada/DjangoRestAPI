from django import forms
from.models import emp
class employeesforms(forms.ModelForm):
    def clean_esalary(self):
        inputsal=self.cleaned_data["esalary"]
        if inputsal<5000:
            raise forms.ValidationError("it should be grater than 5000")
        return inputsal
    class Meta:
        model=emp
        fields="__all__"