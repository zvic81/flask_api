FROM postgres:13
USER postgres
RUN whoami
ADD ./flask_db.sql /docker-entrypoint-initdb.d/
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]