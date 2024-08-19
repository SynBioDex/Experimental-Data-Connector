# This docker file coppies the src folder and installs the dependencies
# we use python:3.12 as the base image
# we also mount the output folder to the WORKDIR/output folder

FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Create a folder to store the output
RUN mkdir output

# Expose the port the app runs on
EXPOSE 4269

# Run main.py when the container launches
CMD ["python", "main.py"]
