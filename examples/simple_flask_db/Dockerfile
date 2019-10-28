FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --extra-index-url https://pypi.apple.com/simple --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

ENV FLASK_APP main.py

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]