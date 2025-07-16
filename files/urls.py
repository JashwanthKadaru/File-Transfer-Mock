from django.urls import path
from .views import FileListCreateView, TransferFileView, RevokeTransferView, TransferHistoryListView

urlpatterns = [
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('transfer/', TransferFileView.as_view(), name='file-transfer'),
    path('revoke/', RevokeTransferView.as_view(), name='file-revoke'),
    path('history/', TransferHistoryListView.as_view(), name='transfer-history'),
]
