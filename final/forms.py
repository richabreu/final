from django import forms
from final.models import User, SourceTag, SourceUrl

class TagMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name
		
class UserForm(forms.ModelForm):
	tags = TagMultipleChoiceField(SourceTag.objects.all())
	
	class Meta:
		model = User
		fields = ['name', 'tags']