from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.conf import settings
from tinymce import models as tinymce_models
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', related_name = 'children',null=True, on_delete=models.CASCADE,)


    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Post(models.Model):
    # user =  models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    Title = models.CharField(max_length=120, null=False, blank=False)
    Description = models.TextField(max_length=255, blank = True, null=True)
    category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.CASCADE)
    content = tinymce_models.HTMLField('Content', null=True, blank=True)
    image = models.ImageField(upload_to='images', null=False,default=False, blank=False)
    pdf = models.FileField(upload_to='media', null=True, blank=True, validators=[validate_file_extension])
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False,)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Title

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

        
# Create your models here.
