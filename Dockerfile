#cpu manege
#based ubuntu,python,django,psutil

FROM ubuntu

MAINTAINER zhangxusheng sdzhangxusheng@163.com

RUN apt-get update && apt-get install -y python-pip && apt-get install -y vim-gtk 
RUN pip install django
RUN pip install setuptools
RUN apt-get install -y python-dev
COPY psutil-4.2.0.tar.gz /opt/psutil-4.2.0.tar.gz
RUN pip install /opt/psutil-4.2.0.tar.gz

COPY /CPUManage /opt/CPUManage

EXPOSE 8000

WORKDIR /opt/CPUManage

CMD python manage.py runserver 0.0.0.0:8000 & python test.py
