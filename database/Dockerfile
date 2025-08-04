FROM public.ecr.aws/docker/library/postgres:13

ENV POSTGRES_DB=hello_db
ENV POSTGRES_USER=hello_user
ENV POSTGRES_PASSWORD=hello_pass

# init.sql will be run on first container start
COPY init.sql /docker-entrypoint-initdb.d/
