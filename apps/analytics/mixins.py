from .signals import object_viewed_signal


class ObjectViewedMixin(object):

    # def get_context_data(self, *args, **kwargs):
    def get_context_data(self, **kwargs):
        context = super(ObjectViewedMixin, self).get_context_data(**kwargs)
        # context = super(ObjectViewedMixin, self).get_context_data(*args, **kwargs)
        # print(f'analytics/mixin: {self.request}')
        # print(f'context: {context}')

        request = self.request
        instance = context.get('object')
        # print(f'instance: {instance}')
        if request.user.is_authenticated and instance:
            # print(f'instance: TRUE')
            object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return context