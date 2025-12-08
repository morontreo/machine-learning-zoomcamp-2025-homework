import os

from io import BytesIO
import numpy as np
import onnxruntime as ort
from PIL import Image
from torchvision import transforms
from urllib import request

model_name = os.getenv("MODEL_NAME", "hair_classifier_v1.onnx")

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

preprocess = transforms.Compose([
    transforms.Resize((200, 200)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ) # ImageNet normalization
])


session = ort.InferenceSession(
    model_name, providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


def predict(url):
    img = download_image(url)
    img = prepare_image(img, (200, 200))

    x = preprocess(img)
    result = session.run([output_name], {input_name: x.unsqueeze(0).numpy()})
    return result[0][0].tolist()

def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result