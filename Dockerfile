FROM python:3.12-slim
COPY ./ app
WORKDIR app
RUN pip install -r  requirement.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
