from django import forms

import cv2
import numpy

from .models import Ticker


class TickerCreateForm(forms.ModelForm):
    class Meta:
        model = Ticker
        fields = ('text', 'font', 'video_width', 'video_height', 'seconds')

    def create_ticker(self) -> int:
        ''' Создаёт видео с бегущей строкой и сохраняет в media '''
        instance = self.save() #Сохраняем в БД результат формы

        data = self.cleaned_data
        width, height = data['video_width'], data['video_height']
        font = data['font']

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        ticker = cv2.VideoWriter(f"media/ticker_{instance.pk}.mp4", 
                                 fourcc, 30, (width, height))
        frame = numpy.zeros((height, width, 3), dtype=numpy.uint8)

        x, y = width, height // 2
        speed = width // (data['seconds']*25) + round(len(data['text']) * 3.5) * (font.scale // 5) // data['seconds']

        for _ in range(data['seconds']*30):
            frame.fill(0)
            x -= speed
            cv2.putText(frame, data['text'], (x, y), 
                        int(font.font), font.scale, tuple(map(int, font.color.split())), font.thickness)
            ticker.write(frame)

        ticker.release()

        return instance.pk
