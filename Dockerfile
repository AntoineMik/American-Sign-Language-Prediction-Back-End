FROM maiv/sign-language-detection:latest

LABEL Antoine Vignon <vignonantoinem@gmail.com>

WORKDIR /project
RUN mkdir ./datasets/user_test_data
RUN mkdir ./datasets/user_processed_test_dataset
RUN pip install flask transformers torch mediapipe streamlit

COPY . .

CMD ["python3", "server.py"]

