import os
from fastapi import FastAPI
import queues


#
#
# app = FastAPI()
#
#
# @app.get("/get_images_info/")
# async def get_images_info():
#     images = read_files(IMAGE_FOLDER_PATH)
#     queues.send_result(images)
#     return "Success"
#
#
# @app.get("/")
# async def root():
#     return {"message": "Platform is running"}
