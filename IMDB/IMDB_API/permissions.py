from rest_framework import permissions

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user == obj.review_user)