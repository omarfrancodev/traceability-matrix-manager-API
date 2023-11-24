from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from matrix.serializers import MatrixSerializer


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            projectId = response.data["id"]

            matrixSerializer = MatrixSerializer(data={"associated_project": projectId})
            matrixSerializer.is_valid(raise_exception=True)
            matrixSerializer.save()

            return Response(
                data={
                    "message": "Project created successfully",
                    "projectData": response.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                data={"message": f"Error creating project: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return Response(
                data={
                    "message": "Projects retrieved successfully",
                    "projectsData": response.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                data={"message": f"Error retrieving projects: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response(
                data={
                    "message": "Project retrieved successfully",
                    "projectData": response.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                data={"message": f"Error retrieving project: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                data={
                    "message": "Project updated successfully",
                    "projectData": response.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                data={"message": f"Error updating project: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response(
                data={"message": "Project deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            return Response(
                data={"message": f"Error deleting project: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

class ProjectUsersView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        project = self.get_object()
        users = project.assignedUsers.all()
        user_data = [{'id': user.id, 'fullName': user.full_name} for user in users]

        return Response(
            data={'message': 'Users retrieved successfully', 'projectUsers': user_data},
            status=status.HTTP_200_OK
        )