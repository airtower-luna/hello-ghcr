FROM alpine:latest

LABEL org.opencontainers.image.source="https://github.com/airtower-luna/hello-ghcr" \
      org.opencontainers.image.title="Container says Meow!"

COPY meow.sh /
ENTRYPOINT ["/meow.sh"]
