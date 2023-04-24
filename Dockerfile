FROM python:3.10.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate a virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN apt-get update && apt-get install -y libnss3
# Install the required packages inside the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Start a bash shell inside the virtual environment
CMD ["/bin/bash", "-c", "source /app/venv/bin/activate && exec bash"]
