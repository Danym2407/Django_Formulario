from django import forms

class EmployeeForm(forms.Form):
    # charField
    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3'
        }),
        initial="Name",
        help_text="Please enter your full name (First Name Last Name)"
    )
    emp_salary = forms.IntegerField(
        min_value=0,
        max_value=105,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mb-3',
                'type': 'number',
                'id': "emp_salary"
            }),
        label="Employee Salary",
        initial=0,
        help_text="Please Enter the employee salary"
    )
    emp_score = forms.FloatField(
        min_value=0.0,
        max_value=105.0,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mb-3',
                'type': 'number',
                'id': "emp_salary"
            }),
        label="Employee Salary",
        initial=0.0,
        help_text="Please Enter the employee salary"
    )
    is_employed = forms.BooleanField(
    )
