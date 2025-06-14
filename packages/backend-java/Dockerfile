# packages/backend-java/Dockerfile

# 1. 빌드 환경 (Builder Stage)
FROM eclipse-temurin:21-jdk
WORKDIR /app
COPY . .
RUN chmod +x ./gradlew
RUN ./gradlew build --no-daemon -x test && cp build/libs/demo-0.0.1-SNAPSHOT.jar app.jar

# 실제 실행은 빌드된 jar로
WORKDIR /app
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]