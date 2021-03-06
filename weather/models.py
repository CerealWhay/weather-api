from django.db import models

DESCRIPTIONS = (
    (0, "sunny"),
    (1, "rain"),
    (2, "cloudy"),
    (4, "snow"),
)


class Description(models.Model):
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    probOfPrecip = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    wet = models.IntegerField(default=0)
    time = models.TextField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.created_on)
