FROM ubuntu:16.04
MAINTAINER Aditya mandil
RUN apt-get update && apt-get install -y openssh-server && apt install python3 -y && apt install python3-pip -y && pip3 install flask
RUN apt install figlet -y
RUN mkdir /var/run/sshd
RUN echo 'root:THEPASSWORDYOUCREATED' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "figlet -f big Play With VM">>/root/.bashrc
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

