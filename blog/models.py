from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)    #제목
    content = models.TextField()    #포스트내용
    create_date = models.DateTimeField() #날짜
    categories = models.ManyToManyField("Category", related_name="blogs") #카테고리
    # image = models.ImageField() #이미지
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

