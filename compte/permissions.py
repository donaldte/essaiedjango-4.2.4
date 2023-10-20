from django.contrib.auth.mixins import UserPassesTestMixin 
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied

from functools import wraps

def group_required(group:str):
    
    def decorator(view_func):
        
        @wraps(view_func)
        
        def _wrapped_vew(request, *args, **kwargs):
            
            if request.user.groups.filter(name=group).exists():
                
                return view_func(request, *args, **kwargs)
            
            else:
                raise PermissionDenied
            
        return _wrapped_vew
    
    return decorator


def role_required(required_roles:list):
    
    def decorator(view_func):
        
        @wraps(view_func)
        
        def _wrapped_vew(request, *args, **kwargs):
            if request.user.is_authenticated and all(getattr(request.user, role) for role in required_roles):
                    
                return view_func(request, *args, **kwargs)
            
            else:
                raise PermissionDenied
            
        return _wrapped_vew
    
    return decorator


# mixin for class based view

class GroupRequiredMixin(UserPassesTestMixin):
    group = None
    def test_func(self) -> bool | None:
        return self.request.user.groups.filter(name=self.group).exists()
    
    
class RoleRequiredMixin(UserPassesTestMixin):
    roles = []
    def test_func(self) -> bool | None:
        return self.request.user.is_authenticated and all(getattr(self.request.user, role) for role in self.roles)         