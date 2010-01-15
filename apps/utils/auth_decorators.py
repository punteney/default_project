from django.http import HttpResponseForbidden

def staff_required(fn):
    def decorator(request, *args, **kwargs):
        if request.user.is_staff:
            return fn(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorator

def user_match_only(instance_keyword, attribute_name='user', allow_anonymous=False):
    def user_match_decorator(original_fn):
        def check_user_match(request, **kwargs):
            if request.user.is_anonymous():
                if allow_anonymous:
                    return original_fn(request, **kwargs)
                else:
                    return HttpResponseForbidden("You must be logged in to access this page.")
            elif request.user.is_staff:
                return original_fn(request, **kwargs)
            else:
                attr = getattr(kwargs[instance_keyword], attribute_name, None)

                if isinstance(attr, int):
                    match = (request.user.id == attr)
                elif isinstance(attr, (str, unicode)):
                    match = (request.user.id == int(attr))
                else:
                    match = (request.user == attr)

                if match:
                    return original_fn(request, **kwargs)
                else:
                    return HttpResponseForbidden("This page is restricted to its owner.")
        return check_user_match
    return user_match_decorator

def only_if_user_in(approved_list=[], instance_keyword=None, attribute_name=None):
    def only_if_user_in_decorator(original_fn):
        def check_user_in(request, **kwargs):
            approved = False
            if approved_list:
                a_list = approved_list
            else:
                a_list = []
            if request.user.is_staff:
                approved = True 
            else:
                if not a_list:
                    if instance_keyword and attribute_name:
                        a_list = getattr(kwargs[instance_keyword], attribute_name).all()
                        print a_list
                if a_list:
                    if request.user.id in a_list:
                        approved = True
                    elif request.user in a_list:
                        approved = True

            if approved:
                return original_fn(request, **kwargs)
            else:
                return HttpResponseForbidden("Access to this page is restricted.")
        return check_user_in
    return only_if_user_in_decorator
