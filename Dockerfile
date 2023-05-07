# Dockerfile for Lorenz attractor simulation

#FROM python:3.9
FROM opensciencegrid/osgvo-ubuntu-xenial
WORKDIR /lorenz
ADD lorenz.py .
RUN pip install --upgrade pip
RUN pip install numpy scipy pytomlpp pandas
CMD ["python3", "lorenz.py", "input.toml", "out.csv"]
