# Build stage
FROM golang:1.22 AS builder
WORKDIR /app
COPY go.mod .
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o temperature-api

# Final stage
FROM gcr.io/distroless/base-debian11
WORKDIR /app
COPY --from=builder /app/temperature-api .
EXPOSE 8081
ENTRYPOINT ["/app/temperature-api"]
