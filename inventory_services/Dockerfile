FROM python:3.9-slim

# Set environment variables.
ARG stage
ENV STAGE=$stage
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /inventory_services

COPY /requirements*.txt .
RUN if [ "${STAGE}" = "dev" ]; then pip install -r requirements-dev.txt; else pip install -r requirements.txt; fi

RUN apt-get update -y && apt-get install -y iputils-ping sudo telnet

EXPOSE 5000


COPY /app .
# Use the provided entrypoint script
COPY /entrypoint.sh .
RUN chmod +x /inventory_services/entrypoint.sh

# Run your application using the provided entrypoint script
ENTRYPOINT ["/inventory_services/entrypoint.sh"]
CMD ["start"]
