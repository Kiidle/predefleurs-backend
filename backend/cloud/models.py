from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

User = get_user_model()

class Folder(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name="created_folders")

    def __str__(self):
        return f"Folder: {self.title}"

class UserFolder(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    read = models.BooleanField(null=False, default=False)
    edit = models.BooleanField(null=False, default=False)
    delete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.group} linked {self.folder}"

class File(models.Model):
    title = models.CharField(max_length=50)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="files")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="created_files")

    def __str__(self):
        return f"File: {self.title}"

class UserFile(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    read = models.BooleanField(null=False, default=False)
    edit = models.BooleanField(null=False, default=False)
    delete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.group} linked {self.file}"

class TextSection(models.Model):
    title = models.CharField(null=True, max_length=50)
    content = models.TextField(max_length=1000)
    arrange = models.IntegerField()
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="created_textsection")

    def __str__(self):
        return f"Textabschitt: {self.title}"

class UserTextSection(models.Model):
    textSection = models.ForeignKey(TextSection, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    read = models.BooleanField(null=False, default=False)
    edit = models.BooleanField(null=False, default=False)
    delete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.group} linked {self.textSection}"