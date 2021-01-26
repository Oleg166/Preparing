from django.forms import ModelForm


from homepage.models import Good_Item


class AddForm(ModelForm):
    class Meta:
        model = Good_Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
