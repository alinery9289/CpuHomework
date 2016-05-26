#cpu manege
#based ubuntu,python,django,psutil

FROM ubuntu

MAINTAINER zhangxusheng sdzhangxusheng@163.com

RUN apt-get update && apt-get install -y python
RUN pip install django
RUN pip install psutil

COPY /CPUManage /opt/CPUManage

CMD echo 'hello'
