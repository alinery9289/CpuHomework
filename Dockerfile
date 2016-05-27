#cpu manege
#based ubuntu,python,django,psutil

FROM ubuntu

MAINTAINER zhangxusheng sdzhangxusheng@163.com

RUN apt-get update && apt-get install -y python-pip && apt-get install -y vim-gtk
RUN pip install --default-timeout=100 django
RUN pip install wheel

COPY psutil-4.2.0-cp27-cp27m-win_amd64.whl /opt/psutil-4.2.0-cp27-cp27m-win_amd64.whl
RUN pip install /opt/psutil-4.2.0-cp27-cp27m-win_amd64.whl

COPY /CPUManage /opt/CPUManage

EXPOSE 8000

WORKDIR /opt/CPUManage

CMD python manage.py runserver 0.0.0.0:8000 & python test.py
