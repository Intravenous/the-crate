from django.contrib import admin
# from .models import Recording
from .models import Artist, Label, Genre, Style, Country, Recording, Track, Crate, Video


# Register your models here.
admin.site.register(Artist)
admin.site.register(Label)
admin.site.register(Genre)
admin.site.register(Style)
admin.site.register(Country)
admin.site.register(Recording)
admin.site.register(Track)
admin.site.register(Crate)
admin.site.register(Video)
