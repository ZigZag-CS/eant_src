from django.dispatch import Signal

# signal pentru view
object_viewed_signal = Signal(providing_args=['instance', 'request'])