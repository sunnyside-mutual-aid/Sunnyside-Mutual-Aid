FROM postgres:alpine

# create a db user
RUN addgroup -S dbuser && adduser -S dbuser -G dbuser

RUN touch /var/lib/postgresql/data/pgdata && \
  chown -R dbuser:dbuser /var/lib/postgresql/data/pgdata

USER dbuser
