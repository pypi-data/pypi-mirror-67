import hashlib
import os
import time

import boto3 as boto3
from werkzeug.utils import secure_filename

from gwlib.config import config
from gwlib.base.base_service import BaseService


class BaseUploadService(BaseService):

    def __init__(self):
        super().__init__()

    def upload(self, file, path=None):
        host = "https://{}.s3.amazonaws.com".format(config.BUCKET_NAME)
        filename = file.filename
        filename_splited = filename.split(".")
        if len(filename_splited) <= 1:
            raise Exception("MALFORMED filename")

        extension = filename_splited[-1]
        mimetype = file.content_type
        filename = hashlib.sha256(str(secure_filename(file.filename) +
                                      str(time.time())).encode('utf-8')).hexdigest() + ".{}".format(extension)
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv('AWS_UPLOAD_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_UPLOAD_SECRET')
        )
        file_stream = file.stream.read()
        print("log", len(file_stream))
        filename = path.format(filename)
        s3.put_object(Key=filename, ACL='public-read',
                      ContentType=mimetype,
                      Bucket=config.BUCKET_NAME, Body=file_stream)
        file_url = "{}/{}".format(host, filename)
        return {'success': True,
                "file_url": file_url,
                "file_name": filename
                }


