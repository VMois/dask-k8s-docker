FROM python:3.5.6

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
ADD ./requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
# ADD . .
