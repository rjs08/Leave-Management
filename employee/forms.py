from django import forms
from login.models import LeaveApplication

class leaveForm(forms.ModelForm):
    start_date = forms.DateField(error_messages={'required':'*'}, widget=forms.DateInput(attrs={'type':'date'}))
    end_date = forms.DateField(error_messages={'required':'*'}, widget=forms.DateInput(attrs={'type':'date'}))
    leave_description= forms.CharField(error_messages={'required':'*'})
    leave_type = forms.Select()

    class Meta:
        model = LeaveApplication
        fields = ['start_date','end_date','leave_description','leave_type']
        error_message={
            'leave_type' : {
                'required' : '*'
            }
        }
