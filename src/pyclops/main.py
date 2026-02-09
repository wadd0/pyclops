import time

import cv2
import dropbox
from dropbox import Dropbox
import logging

from pyclops.settings import settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def read_webcam() -> bytes:
    cap = cv2.VideoCapture(0)
    # Warm up the camera by discarding initial frames
    for _ in range(5):
        cap.read()

    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise Exception("Could not read from webcam")
    _, buffer = cv2.imencode(".jpg", frame)
    return buffer.tobytes()


def watch() -> None:
    dbx = Dropbox(
        app_key=settings.app_key,
        app_secret=settings.app_secret,
        oauth2_refresh_token=settings.refresh_token,
    )
    while True:
        logger.info("Reading image from webcam...")
        image = read_webcam()
        logger.info("Uploading image to Dropbox...")
        dbx.files_upload(
            f=image,
            path=f"{settings.app_root}/{settings.image}",
            mode=dropbox.files.WriteMode("overwrite"),  # ty:ignore[possibly-missing-attribute]
            autorename=False,
        )
        logger.info("Upload complete.")
        logger.info(f"Waiting for {settings.interval} seconds before next upload...")
        time.sleep(settings.interval)


if __name__ == "__main__":
    watch()
