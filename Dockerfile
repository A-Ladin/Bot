FROM python:slim
ENV TOKEN='Your token here'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py
