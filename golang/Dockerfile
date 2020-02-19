FROM golang:1.11

EXPOSE 8080

WORKDIR /app
ADD go.mod .
ADD go.sum .
RUN go mod download
COPY . .
CMD ["go", "run", "main.go"]
