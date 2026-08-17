FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory on the host to the container's /app directory
COPY . .

# Install Python dependencies listed in requirements.txt
RUN pip3 install -r requirements.txt

# Define the command to run the Flask application on port 7860 and make it accessible externally
# - `-w 4`: Uses 4 workers
# - `-b 0.0.0.0:7860`: Binds the Flask app to all available network interfaces on port 7860
# - `app:app`: Specifies the name of the Flask app to run
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_predictor_api"]
