FROM postgres:13
COPY ./flask_db.sql /docker-entrypoint-initdb.d/
ENTRYPOINT ["docker-entrypoint.sh"]
#EXPOSE 5433
#CMD ["postgres"]
