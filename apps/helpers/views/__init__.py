from django.utils.decorators import method_decorator

class ProtectedViewMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedViewMixin, self).dispatch(*args, **kwargs)

def static_view(request, path):
    if not path or path.endswith('/'):
        template_name = path + 'index.html'
    else:
        template_name = path
    
    return render_to_response(template_name, 
        context_instance=RequestContext(request))