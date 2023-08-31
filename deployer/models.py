from django.db import models

class EpubFile(models.Model):
    title = models.CharField(max_length=100)
    epub_file = models.FileField(upload_to='epub_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
