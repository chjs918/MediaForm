from django.db import models

# Create your models here.

class Blog(models.Model):   
    blog_title = models.CharField(max_length=200)
    blog_writer = models.CharField(max_length=100)
    blog_date = models.DateTimeField()
    blog_body = models.TextField()
    blog_img = models.ImageField(upload_to="blog/", blank = True, null = True)
     #원본이 아니라 경로 URL

#모델테이블을 변경하면 initial파일과 dbsqlite3파일을 삭제하고 다시 마이그레이션한다.
    def __str__(self):
          return self.blog_title

    def blog_summary(self):
        return self.blog_body[:100]