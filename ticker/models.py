from django.db import models
import cv2


fonts = ((str(cv2.FONT_HERSHEY_COMPLEX), 'COMPLEX'), (str(cv2.FONT_HERSHEY_SIMPLEX), 'SIMPLEX'))
colors = (('0 0 255', 'Red'), ('0 255 0', 'Green'), ('255 0 0', 'Blue'), ('255 255 255', 'White'), ('0 0 0', 'Black'))
align = (('center', 'CENTER'), ('down', 'DOWN'))

class Font(models.Model):
    name = models.CharField(max_length=10)
    font = models.CharField(max_length=50, choices=fonts, default=cv2.FONT_HERSHEY_COMPLEX)
    scale = models.PositiveIntegerField()
    thickness = models.PositiveIntegerField()
    color = models.CharField(max_length=20, choices=colors, default='White')
    align = models.CharField(max_length=20, choices=align, default='CENTER')

    def __str__(self):
        return f'{self.name}'

class Ticker(models.Model):
    text = models.CharField(max_length=250)
    font = models.ForeignKey(Font, on_delete=models.CASCADE)
    video_width = models.PositiveIntegerField()
    video_height = models.PositiveIntegerField() 
    seconds = models.PositiveIntegerField()
    video = models.FileField(blank = True)

    def __str__(self):
        return f'{self.text[:20]}'
    
