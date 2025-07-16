from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import File, TransferHistory
from .serializers import FileSerializer, TransferHistorySerializer

class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, original_owner=self.request.user)

class TransferFileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_id = request.data.get('file_id')
        to_user_id = request.data.get('to_user_id')
        file = get_object_or_404(File, id=file_id)
        to_user = get_object_or_404(User, id=to_user_id)
        if file.owner != request.user:
            return Response({'detail': 'Only the current owner can transfer this file.'}, status=status.HTTP_403_FORBIDDEN)
        file.owner = to_user
        file.save()
        TransferHistory.objects.create(file=file, from_user=request.user, to_user=to_user, action="TRANSFER")
        return Response({'detail': 'File ownership transferred.'}, status=status.HTTP_200_OK)

class RevokeTransferView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_id = request.data.get('file_id')
        file = get_object_or_404(File, id=file_id)
        if file.original_owner != request.user:
            return Response({'detail': 'Only the original owner can revoke this file.'}, status=status.HTTP_403_FORBIDDEN)
        if file.owner == file.original_owner:
            return Response({'detail': 'File is already owned by the original owner.'}, status=status.HTTP_400_BAD_REQUEST)
        prev_owner = file.owner
        file.owner = file.original_owner
        file.save()
        TransferHistory.objects.create(file=file, from_user=prev_owner, to_user=request.user, action="REVOKE")
        return Response({'detail': 'File ownership revoked and returned to original owner.'}, status=status.HTTP_200_OK)

class TransferHistoryListView(generics.ListAPIView):
    queryset = TransferHistory.objects.all().order_by('-timestamp')
    serializer_class = TransferHistorySerializer
    permission_classes = [IsAuthenticated]
