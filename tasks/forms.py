from django import forms


class TaskForm(forms.Form):
    text_input = forms.CharField()
    due_date = forms.DateField(
        widget=forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            required=False
        )
    is_complete = forms.BooleanField(
        required=False
    )