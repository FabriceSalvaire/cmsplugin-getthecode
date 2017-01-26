####################################################################################################

from django.conf import settings

####################################################################################################

LANGUAGE_CHOICES = getattr(settings, 'PYGMENTS_LANGUAGE_CHOICES', [
    ('python', 'Python'),
    ('python3', 'Python 3'),
])
LANGUAGE_CHOICES.sort(key=lambda x: x[0])
