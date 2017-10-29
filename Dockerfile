FROM python:2.7-slim
LABEL maintainer "Peter Benjamin <petermbenjamin@gmail.com>"
WORKDIR /src/BasicAuth-Brute/
COPY BasicAuth-Brute.py .
RUN pip install colorama requests
ENTRYPOINT [ "python", "BasicAuth-Brute.py" ]
