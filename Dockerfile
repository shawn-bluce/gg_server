FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && apt update && apt -y install supervisor fabric vim
RUN pip install --upgrade pip -i https://pypi.mirrors.ustc.edu.cn/simple && pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
