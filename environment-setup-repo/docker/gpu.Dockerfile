FROM tensorflow/tensorflow:1.15.0-gpu-py3
#FROM tensorflow/tensorflow:1.15.0-py3

RUN apt-get update  && \
    apt-get install -y \
        wget \
        git


# Install Anaconda
#RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh
RUN bash Miniconda3-4.7.12.1-Linux-x86_64.sh -b
RUN rm Miniconda3-4.7.12.1-Linux-x86_64.sh

# Set path to conda
ENV PATH /root/miniconda3/bin:$PATH
RUN . /root/.bashrc