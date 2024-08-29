from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    message = "You are blocklisted..."
    def has_permission(self, request, view):
        print("Checking blocklist permission", request.query_params, request.parser_context['kwargs'])
        return request.method == 'GET'

    def has_object_permission(self, request, view, obj):
        print("Checking single object permissions")
        if obj.country.name == 'india':
            return True
        return False