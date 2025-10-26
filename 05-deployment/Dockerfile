FROM agrigorev/zoomcamp-model:2025

RUN pip install uv

WORKDIR /app

COPY ".python-version" "pyproject.toml" "uv.lock" "./"
RUN uv sync --locked

COPY "predict_fastapi.py" "pipeline_v1.bin" "./"

EXPOSE 9696

ENTRYPOINT ["uv","run", "uvicorn", "predict_fastapi:app", "--host", "0.0.0.0", "--port", "9696"]