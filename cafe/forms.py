from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'file']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : '글 제목을 입력하세요.'
        })
        self.fields['file'].required=False
# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     photo = models.ImageField(blank=True)
#     text = models.TextField()
#     # create_date = models.DateTimeField(default=timezone.now)
#     published_date