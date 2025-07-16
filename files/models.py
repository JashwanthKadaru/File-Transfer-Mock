from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_files')
    original_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='original_files')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TransferHistory(models.Model):
    ACTION_CHOICES = [
        ("TRANSFER", "Transfer"),
        ("REVOKE", "Revoke"),
    ]
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='transfer_histories')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_made')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_received')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name}: {self.action} from {self.from_user} to {self.to_user} at {self.timestamp}"
