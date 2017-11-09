import dropbox
import os
from django.db import models
from dropbox.files import WriteMode

# Create your models here.


class DropboxUpload(models.Model):
    name = models.CharField(max_length=255)
    metadata = models.TextField()

    @classmethod
    def upload(cls, file, name, metadata=""):
        dbx = dropbox.Dropbox(os.environ["DROPBOX_TOKEN"])
        dbx.files_upload(file.read(), "/%s" % name, mode=WriteMode('overwrite'))
        return DropboxUpload.objects.create(
            name=name,
            metadata=metadata
        )

    def get_link(self):
        dbx = dropbox.Dropbox(os.environ["DROPBOX_TOKEN"])
        return dbx.files_get_temporary_link("/%s" % self.name).link
