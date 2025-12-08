FROM agrigorev/model-2024-hairstyle:v3

RUN pip install onnxruntime torchvision

COPY lambda_function.py ./

CMD ["lambda_function.lambda_handler"]