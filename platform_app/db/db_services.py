from .database import get_session
from .models import ImageClassification


def save_image_classification(data):
    with get_session() as session:
        image_classification = ImageClassification(id=data['photo_id'], label=data['label'])
        session.add(image_classification)
        session.commit()
        session.refresh(image_classification)