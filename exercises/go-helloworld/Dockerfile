FROM golang:alpine

WORKDIR /go/src/app

COPY . .

RUN go env -w GO111MODULE=off
RUN go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]