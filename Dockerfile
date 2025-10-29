FROM python:3.12-slim

# Copy application files into the container
COPY . /

# Install git and Python dependencies
RUN apt-get update && apt-get install -y git && \
    pip install --no-cache-dir -r requirements.txt

# Ensure the entrypoint script uses Unix line endings
COPY src/entrypoint.py /src/entrypoint.py
RUN sed -i 's/\r$//' /src/entrypoint.py

# Create and define a volume for external folder mounting
RUN mkdir -p /workspace
VOLUME /workspace

# Run a simple ls -al command to list files and directories
RUN ls -al /

# Set the entrypoint to the Python script
ENTRYPOINT ["python", "/src/entrypoint.py"]