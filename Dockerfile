FROM python
WORKDIR /app
RUN mvn install
COPY /target/medical-app-1.0-SNAPSHOT.jar /app
CMD ["app" ".py"]
