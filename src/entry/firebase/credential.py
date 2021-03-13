import base64

from config import CREDENTIAL_B64, CREDENTIAL_FILE_NAME
from src.util.b64file import make_file_from_b64
from firebase_admin import credentials


def get_credential() -> credentials.Certificate:
    make_file_from_b64(CREDENTIAL_FILE_NAME, CREDENTIAL_B64)

    credential = credentials.Certificate(CREDENTIAL_FILE_NAME)

    return credential
