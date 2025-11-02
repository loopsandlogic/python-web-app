# Dockerfile

# 1. BASE IMAGE: Use an official lightweight Python image
FROM python:3.11-slim

# 2. WORKING DIRECTORY: Set the working directory inside the container
WORKDIR /app

# 3. COPY DEPENDENCIES: Copy the requirements file and install packages
# This is a key step for Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. COPY SOURCE CODE: Copy the rest of the application code
COPY . .

# 5. EXPOSE PORT: Inform Docker that the container listens on port 5000
# (Flask's default port)
EXPOSE 5000

# 6. START COMMAND: Define the command to run your Flask application
# Use 0.0.0.0 as the host to make the server accessible outside the container
CMD [ "flask", "run", "--host=0.0.0.0" ]