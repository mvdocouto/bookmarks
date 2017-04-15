FROM ubuntu:14.04

# Forca a instalacao do pacote evitando divergencia de pacotes
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Ignorando as etapas de configuracao depois da instalacao
ENV DEBIAN_FRONTEND noninteractive


# Atualizando os pacotes
RUN apt-get update --fix-missing

# Instalando os pacotes basicos do python
RUN apt-get install -y build-essential git
RUN apt-get install -y python python-dev python-setuptools
RUN apt-get install -y python-pip python-virtualenv
RUN apt-get install -y nginx 


# Iniciando o virtualenv e instalando os requirements.txt
RUN virtualenv /opt/venv
ADD ./requirements.txt /opt/venv/requirements.txt
RUN /opt/venv/bin/pip install -r /opt/venv/requirements.txt

# Copiando as configuracoes do nginx
ADD ./nginx.conf /etc/nginx/nginx.conf

RUN service nginx stop

COPY . /opt/app

EXPOSE 5000

# Iniciando o APP
CMD ["python", "run.py"]