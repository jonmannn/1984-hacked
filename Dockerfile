FROM python:3.8

# Copy only the requirements file first to leverage Docker caching
COPY /apps/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-traditional iputils-ping && apt-get install -y vim

# Copy the entire application code
COPY . .

# Expose the port your application will run on
EXPOSE 8888

# Specify the command to run on container start
ENTRYPOINT ["python", "apps/webapp.py"]