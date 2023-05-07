# Dockerfile for Lorenz attractor simulation

#FROM python:3.9
FROM opensciencegrid/osgvo-ubuntu-20.04:latest
WORKDIR /lorenz
ADD lorenz.py .
RUN apt-get update && apt-get -y install python3-pip python3-setuptools \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install setuptools
RUN pip3 install scipy pandas numpy && pip3 install --upgrade scipy
CMD ["python3", "lorenz.py", "input.toml", "out.csv"]
