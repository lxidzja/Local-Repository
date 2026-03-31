FROM gcc:13 AS builder 
WORKDIR /src 
COPY . . 
RUN make 
FROM debian:stable-slim 
WORKDIR /app 
COPY --from=builder /src/app ./app 
CMD ["./app"]