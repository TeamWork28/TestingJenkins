# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files from current directory to container
COPY . .

# Command to run when container starts
CMD ["python", "--version"]
