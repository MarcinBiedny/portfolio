# Use an official Python image as base.
# This will use `python:3.x` latest image.
FROM python:3

ARG USER_NAME
ARG LOG_DIR

# Set the working directory in the container to /app
WORKDIR /app

# Create a new user with UID 1000
# Necessary step to preserve the file permissions (docker host vs. container)
RUN useradd -u 1000 -m ${USER_NAME}

# Create application log dir with proper user permissions
RUN mkdir -p ${LOG_DIR}
RUN chown ${USER_NAME}:${USER_NAME} ${LOG_DIR}

# Necessary for all binaries installed with pip
ENV PATH="/home/${USER_NAME}/.local/bin:${PATH}"

# Switch user to newly created one
USER ${USER_NAME}

# Make port 5000 available to the world outside this container
EXPOSE 5000
