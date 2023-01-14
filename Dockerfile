FROM docker.io/library/alpine:3.17.1

LABEL org.opencontainers.image.source="https://github.com/airtower-luna/hello-ghcr" \
      org.opencontainers.image.title="Container says Meow!" \
      org.opencontainers.image.description="This container will meow at you."

COPY meow.sh /
ENTRYPOINT ["/meow.sh"]
