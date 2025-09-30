import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverCreateForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = [
            "username",
            "first_name",
            "last_name",
            "license_number",
            "password1",
        ]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must be exactly 8 characters long."
            )
        pattern = r"^[A-Z]{3}[0-9]{5}$"
        if not re.match(pattern, license_number):
            raise forms.ValidationError(
                "License number must start with 3 "
                "uppercase letters followed by 5 digits."
            )
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"].strip()
        print(f"'{license_number}'", len(license_number))

        if len(license_number) != 8:
            raise ValidationError(
                "License number must be exactly 8 characters long."
            )

        pattern = r"^[A-Z]{3}[0-9]{5}$"
        if not re.match(pattern, license_number):
            raise ValidationError(
                "License number must start with 3 "
                "uppercase letters followed by 5 digits."
            )
        return license_number
