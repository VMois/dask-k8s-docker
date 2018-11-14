FROM vmois/dask-k8s-base:0.1.0


ADD ./requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . .

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]