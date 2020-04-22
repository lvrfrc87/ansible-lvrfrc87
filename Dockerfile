FROM centos:8
COPY ./requirements.txt .
RUN yum -y update --security && \
    yum -y install git && \
    dnf install python36 -y && \
    mkdir /git && \
    mkdir /etc/ansible &&\
    pip3 install -r requirements.txt
WORKDIR /git
COPY ./ansible.cfg /etc/ansible
COPY filters/ /usr/local/lib/python3.6/site-packages/ansible/plugins/filter/

