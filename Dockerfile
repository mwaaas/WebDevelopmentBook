FROM gitpod/workspace-full 

WORKDIR /usr/src/app

COPY requirements.txt /tmp

RUN sudo apt-get update \
    && pip install -r /tmp/requirements.txt \
    && playwright install \
    && playwright install-deps 

COPY . .