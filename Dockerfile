FROM ubuntu:22.04

# Install Python 3 (needed for our server script)
RUN apt-get update && apt-get install -y python3

# Copy the download server script into the image
COPY serve_downloads.py /serve_downloads.py

# Expose port 8000 for the webserver
EXPOSE 8000

# Run the server on container start
CMD ["python3", "/serve_downloads.py", "8000"]
