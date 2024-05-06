FROM python:3.10
WORKDIR /app/
COPY . /app/
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
CMD ["bash", "./run_app.sh"]
