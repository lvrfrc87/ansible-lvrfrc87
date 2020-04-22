FROM centos:8
COPY ./requirements.txt .
RUN yum -y update --security 2>/dev/null && \
    yum -y install git 2>/dev/null && \
    yum clean packages && \
    dnf install python36 -y 2>/dev/null && \
    dnf clean packages && \
    mkdir /git && \
    mkdir /etc/ansible &&\
    pip3 --no-cache-dir  \
    install -r requirements.txt 2>/dev/null
WORKDIR /git
COPY ./ansible.cfg /etc/ansible
COPY filters/ /usr/local/lib/python3.6/site-packages/ansible/plugins/filter/

