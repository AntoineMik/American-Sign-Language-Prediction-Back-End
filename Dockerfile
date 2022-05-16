FROM maiv/sign-language-detection:latest

LABEL Antoine Vignon <vignonantoinem@gmail.com>

WORKDIR /project

RUN pip install flask transformers torch mediapipe streamlit

COPY . .

CMD ["python3", "server.py"]

