# Use lambci/lambda base image.
ARG TAG=aws-python3.8
FROM ylathouris/cuta:$TAG

# Install build-time requirements.
ARG BUILD_REQUIRES
RUN if [ "x$BUILD_REQUIRES" = "x" ] ; then echo "No Build Arguments" ; else yum update -y && yum install -y "$BUILD_REQUIRES" && yum clean al; fi

RUN echo `pwd`
COPY ./pyproject.toml pyproject.toml
COPY ./poetry.lock poetry.lock

# Install runtime requirements.
RUN poetry export --format requirements.txt --without-hashes --output requirements.txt
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
