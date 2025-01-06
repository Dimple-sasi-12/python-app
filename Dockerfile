FROM python
WORKDIR /app
COPY /target/medical-app-1.0-SNAPSHOT.jar /app
CMD ["app" ".py"]
