# base image
FROM python:3.10-buster
 
# options
ENV PYTHONUNBUFFERED 1
 
# Set working directory
RUN mkdir core
# set the working directory
COPY . /core/
# coppy commands 
WORKDIR /core
 
# update docker-iamage packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean
 
# update pip 
RUN pip install --upgrade pip
# install python packages 
RUN pip install -r requirements.txt
# create static directory
RUN mkdir static
RUN python manage.py collectstatic --no-input
EXPOSE 8000
CMD ["python","manage.py", "runserver"]