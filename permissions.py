from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = 'permission denied: you are not the owner'

    def has_permission(self, request, view):
        return request.user == request.user.is_authenticated

    def has_object_permission(self,request,obj,view):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user