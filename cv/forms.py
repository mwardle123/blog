from django import forms

from .models import Item, CV, CoreSkill

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('name', 'addresses', 'mobile_number', 'email', 'personal_profile', 'education_and_qualifications', 'relevant_experience', 'work_history', 'hobbies_and_interests',)

class CoreSkillForm(forms.ModelForm):

    class Meta:
        model = CoreSkill
        fields = ('text',)
