from .models import Project
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import ProjectServiceImpl
from .serializers import ProjectSerializer, UpdateProjectSerializer
from utils.pagination import CustomPagination
from utils.response import make_success_response

project_service = ProjectServiceImpl()

@api_view(['GET', 'POST'])
def get_all_and_create_project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = project_service.create_project(serializer.validated_data)
            result_serializer = ProjectSerializer(project)
            return Response(result_serializer.data, status=http_status.HTTP_201_CREATED)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

    status = request.query_params.get('status')
    projects = project_service.get_all_projects(status=status)
    paginator = CustomPagination()
    paginated = paginator.paginate_queryset(projects, request)
    serializer = ProjectSerializer(paginated, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def get_project_by_id(request, id: int):
    try:
        project = project_service.get_project_by_id(id)
    except Project.DoesNotExist:
        return Response(
            {'error': 'Project not found'},
            status=http_status.HTTP_404_NOT_FOUND
        )
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=http_status.HTTP_200_OK)

@api_view(['PUT'])
def update_project(request, id: int):
    serializer = UpdateProjectSerializer(data=request.data)
    if serializer.is_valid():
        project = project_service.update_project(id, serializer.validated_data)
        _ = UpdateProjectSerializer(project)
        return make_success_response("Updated project successfully")
    return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)
