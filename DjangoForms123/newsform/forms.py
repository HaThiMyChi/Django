from django import forms
from . models import Post
from django.forms import ModelForm
from .models import PostLogin


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'time_created',)
		widgets = {
			'title': forms.TextInput(attrs={'class': 'tieude123'}),
			'content': forms.Textarea(attrs={'class': 'noidung123456'})
		}


class SendEmail(forms.Form):
	title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'tieude'}))
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'sonnguyen', 'id': 'noidung'}))
	cc = forms.BooleanField(required=False)
	
	
class PostFormLogin(ModelForm):
	class  Meta:
		model = PostLogin
		fields = ['title', 'content']