
FROM python:3.10-slim

ENV PYTHONUNBUFFERED Truepy 

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install pip update
RUN pip install --no-cache-dir -r req.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
ENV FLASK_ENV "development"
ENV PORT 8080
CMD [ "python", "app.py" ]

# [END run_helloworld_dockerfile]
# [END cloudrun_helloworld_dockerfile]