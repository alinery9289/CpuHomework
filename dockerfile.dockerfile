#cpu manege
#based ubuntu,python,django,psutil

FROM ubuntu

MAINTAINER zhangxusheng sdzhangxusheng@163.com

RUN apt-get update && apt-get install -y python=2.7.11
RUN pip install django
RUN pip install psutil

COPY /CPUManage /opt/CPUManage

CMD echo 'hello'
