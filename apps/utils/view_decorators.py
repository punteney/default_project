from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.http import Http404, HttpResponseServerError, HttpResponseForbidden

def accepts_instance(qs, lookup_keywords, output_name='instance', remove_keywords=True):
    def instance_view(original_fn):
        def get_instance(request, **kwargs):
            try:
                lookup = dict((k, kwargs[k]) for k in lookup_keywords)
            except KeyError:
                if settings.DEBUG:
                    return HttpResponseServerError("Incorrect arguments (%s) for instance lookup (options were: %s)" % (lookup_keywords, kwargs.keys()))
                else:
                    return HttpResponseServerError("Incorrect arguments for instance lookup.")
            try:
                instance = qs.get(**lookup)
            except ObjectDoesNotExist:
                raise Http404("The requested resource could not be found.")
            except FieldError:
                if settings.DEBUG:
                    return HttpResponseServerError("Invalid fields specified for instance lookup (%s)." % lookup.keys())
                else:
                    return HttpResponseServerError("Unable to retrieve the requested resource.")

            new_kwargs = dict(kwargs)

            new_kwargs[output_name] = instance

            if remove_keywords:
                for k in lookup_keywords:
                    new_kwargs.pop(k)

            return original_fn(request, **new_kwargs)

        return get_instance

    return instance_view

