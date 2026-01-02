from django import forms 
from blogs.models import Blogs, Category, Comment, React


class Add_post_form(forms.ModelForm):
    class Meta:
        model = Blogs
        fields =('title', 'category', 'blog_image', 'short_description', 'blog_body', 'status', 'is_featured')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black',
                'placeholder': 'Enter blog title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black',
                'placeholder': 'Unique slug'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
            }),
            'author': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
            }),
            'blog_image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black',
                'rows': 3,
                'placeholder': 'Brief summary of the blog'
            }),
            'blog_body': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black',
                'rows': 6,
                'placeholder': 'Full blog content'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            }),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Write your comment...',
                    'class': 'w-full px-3 py-2 rounded-lg border border-gray-700 bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-blue-500'
                }
            )
        }
class ReactForm(forms.ModelForm):
    class Meta:
        model = React
        fields = [] 