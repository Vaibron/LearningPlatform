from django.db import models


# Курс
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)  # Добавлено поле image_url

    def __str__(self):
        return f'{self.title}'


# Тема
class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.course} - {self.title}'


# Урок
class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_code = models.CharField(blank=True)  # Для кода видео на YouTube

    def __str__(self):
        return f'{self.topic} - {self.title}'
