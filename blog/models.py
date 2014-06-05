from django.db import models

class Tag(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'

class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text[:10] if len(self.text) > 11 else self.text

    class Meta:
        ordering = ['created']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
