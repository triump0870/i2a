from django import forms

from app.models import Application, Owner, Questionnaire, Tag, Rule, TagType
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder, Fieldset, Hidden, HTML


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'description', 'primary_owner', 'secondary_owner', 'logo', 'review_cycle', 'next_review_date']

        # def __init__(self, *args, **kwargs):
        #     super(ApplicationForm, self).__init__(*args, )
        #     self.helper = FormHelper()
        #     self.helper.form_tag = False
        #     self.helper.form_class = 'form-horizontal'
        #     self.helper.layout = Layout(
        #         Field('name'),
        #         Field('description'),
        #         Field('primary_owner'),
        #         Field('secondary_owner'),
        #         Field('logo'),
        #         Field('review_cycle'),
        #         Field('next_review_date', css_class='input-small dateinput'),
        #         Submit('submit', 'Submit', css_class="btn-success"),
        #     )


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email']


class QuestionnaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            Field('application_name')
        )
    class Meta:
        model = Questionnaire
        fields = ['application_name']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'type', 'description']


class TagTypeForm(forms.ModelForm):
    class Meta:
        model = TagType
        fields = ['name', 'description']


class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = '__all__'
