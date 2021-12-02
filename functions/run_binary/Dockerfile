# Define function directory
ARG FUNCTION_DIR="/function/"

# Ubuntu with python.
# For some reason, Ubuntu doesn't include python so I need to install it.
# On this stage, python3 is installed on /usr/bin/python3
FROM ubuntu:20.04 AS with-python3
RUN apt update && apt install python3 python3-pip -y

# New stage. In this stage, we'll install AWS RIC.
FROM with-python3 AS ric

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Copy function code (May we are copying unnecessary files)
COPY . ${FUNCTION_DIR}

# Install the runtime interface client
RUN python3 -m pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric

# New stage. We'll install open CV and then
FROM with-python3

# Install OpenCV
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install libopencv-dev -y

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies
COPY --from=ric ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/bin/python3", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]
