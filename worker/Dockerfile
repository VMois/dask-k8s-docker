FROM python:3.5.6

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
ADD ./requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install OpenCV
RUN pip install opencv-python==3.4.3.18