from django.conf import settings

# Slide photo size in pixels
PHOTO_SIZE = getattr(settings, 'SLIDESHOW_PHOTO_SIZE', (950, 263))
