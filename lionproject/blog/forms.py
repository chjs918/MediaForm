from django import forms
from .models import Blog

class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title','blog_writer', 'blog_body', 'blog_img']
        #blog_date는 현재 시각을 받아서 넣어야하니까 form에서 뺀다