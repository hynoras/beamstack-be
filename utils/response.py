from rest_framework import status
from rest_framework.response import Response

def make_success_response(message: str):
    return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
    