import base64
import json
import logging
import os
import sys
from uuid import uuid4

import pika
from db.database import get_session
from db.models import ImageClassification
from logger import setup_logger

logger = logging.getLogger("platform")

USER = str(os.getenv('RABBITMQ_USER'))
PASSWORD = str(os.getenv('RABBITMQ_PASSWORD'))
HOST = str(os.getenv('RABBITMQ_HOST'))
PORT = int(os.getenv('RABBITMQ_PORT'))
CONSUME_QUEUE = str(os.getenv('RABBITMQ_CONSUME_QUEUE'))
PRODUCE_QUEUE = str(os.getenv('RABBITMQ_PRODUCE_QUEUE'))
IMAGE_FOLDER_PATH = str(os.getenv('IMAGE_FOLDER_PATH'))


def read_files(image_path):
    files = os.listdir(image_path)
    image_files = filter(lambda file: file.split('.')[-1] in ("jpg", "jpeg", "png"), files)
    images = []
    for image_file in image_files:
        with open(f'images_files/{image_file}', mode='rb') as image:
            images.append(image.read())
    return images


credentials = pika.PlainCredentials(USER, PASSWORD)
conn_params = pika.ConnectionParameters(host=HOST, port=PORT, credentials=credentials)


def send_result(images):
    logger.info('Start send images to queue')
    connection = pika.BlockingConnection(conn_params)
    ch = connection.channel()

    for image in images:
        bytes_image = base64.b64encode(image)
        bytes_image_str = bytes_image.decode('utf-8')
        data = {
            "image": bytes_image_str,
            "photo_id": str(uuid4())
        }
        logger.info(f'Send image with id: {data["photo_id"]}')
        message = json.dumps(data)
        ch.basic_publish(exchange='',
                         routing_key=CONSUME_QUEUE,
                         body=message,
                         properties=pika.BasicProperties(
                             delivery_mode=2,  # make message persistent
                         ))
    connection.close()
    logger.info('End send images to queue')


def main():
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()

    def callback(ch, method, properties, body):
        try:
            data = json.loads(body)
            logger.info(f'Get image info: {data}')
            with get_session() as session:
                image_classification = ImageClassification(id=data['photo_id'], label=data['label'])
                session.add(image_classification)
                session.commit()
                session.refresh(image_classification)


        except Exception as e:
            logger.exception('Error', e)
            # https://stackoverflow.com/questions/24333840/rejecting-and-requeueing-a-rabbitmq-task-when-prefetch-count-1
            ch.basic_reject(delivery_tag=method.delivery_tag, requeue=True)

    channel.basic_consume(queue=PRODUCE_QUEUE, on_message_callback=callback)

    logger.info('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        setup_logger()
        images = read_files(IMAGE_FOLDER_PATH)
        send_result(images)
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
