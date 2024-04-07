FROM grafana/grafana

USER root
RUN apk update && apk add --no-cache curl gettext && rm -rf /var/cache/apk/*

WORKDIR /etc/grafana
COPY datasources ./datasources

WORKDIR /app
COPY entrypoint.sh ./
RUN chmod u+x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]