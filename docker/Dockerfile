# Dockerfile for Lorenz attractor simulation

FROM python:3.9
WORKDIR /lorenz
ADD lorenz.py .
RUN pip3 install numpy scipy pytomlpp pandas
CMD ["python3", "lorenz.py", "input.toml", "out.csv"]
