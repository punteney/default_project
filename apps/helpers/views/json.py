from django import http
from django.shortcuts import redirect
from django.utils import simplejson as json

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


from settings import MEDIA_URL

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        if 'jsoncallback' in self.request.REQUEST and \
                self.request.REQUEST['jsoncallback']:
            content = "".join([self.request.REQUEST['jsoncallback'], '(', 
                content, ')'])
            return http.HttpResponse(content,
                                 content_type='text/javascript',
                                 **httpresponse_kwargs)
        else:
            return http.HttpResponse(content,
                                 content_type='application/javascript',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is a naive approach; we may need to do more complex method
        # for handing models and such
        return json.dumps(context)


class BaseJSONView(JSONResponseMixin, TemplateView):
    redirect = None

    def get(self, *args, **kwargs):
        page_format = self.request.REQUEST.get('format', 'html')
        c = self.get_context_data(**kwargs)
        if self.redirect:
            return self.redirect
        else:
            return self.render_to_response(c)

    def render_to_response(self, context):
        # If it's an ajax request or if it has a 'format=json' GET argument
        # then return as json otherwise spit out the template.
        page_format = self.request.REQUEST.get('format', 'html')
        if self.return_json:
            return JSONResponseMixin.render_to_response(self, context)
        else:
            if 'popup' in self.request.REQUEST:
                context['base_template'] = "popup_base.html"
            else:
                context['base_template'] = "base.html"
        
        return TemplateView.render_to_response(self, context)

    @property
    def return_json(self):
        if (self.request.is_ajax() or 
                self.request.REQUEST.get('format') == 'json'):
            return True
        else:
            return False
    
        
class JSONOnlyMixinView():
    def render_to_response(self, context):
        # If it's an ajax request or if it has a 'format=json' GET argument
        # then return as json otherwise try to redirect where they came from
        if self.return_json:
            return JSONResponseMixin.render_to_response(self, context)
        else:
            ref_page = self.request.META.get('HTTP_REFERER', None)
            if ref_page:
                return redirect(ref_page)
            else:
                return redirect('dashboard')

class AjaxSubmitView(JSONOnlyMixinView, BaseView):
    template_name = "coredisplay/blank_ajax.html"
