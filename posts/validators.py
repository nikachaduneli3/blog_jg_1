from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_for_restricted_symbols(value):
    restricted_symbols = '#@^%&*='
    for symbol in restricted_symbols:
        if symbol in value:
            raise ValidationError(f'value must not contain any of these symbols {restricted_symbols}')

def validate_for_restricted_words(value):
    restricted_words = ['mliqvneli', 'tutuci', 'masxara', 'warmarti',
                        'medrove', 'mwvalebeli', 'mavne', 'rasisti', 'avi',
                        'grdzneuli', 'fashisti', 'hitleri', 'nacisti',
                        'komunisti', 'stalini', 'lenini', 'trocki',
                        'agviraxsnili']
    for word in restricted_words:
        if word in value.lower():
            raise ValidationError(f'value must not contain this word {word}')


def validate_future_time(value):
    if value > timezone.now():
        raise  ValidationError('date must not be in future')
