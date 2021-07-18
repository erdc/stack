FROM erdc/ubuntu_base:gcc9

MAINTAINER Proteus Project <proteus@googlegroups.com>

# Configure environment
ENV SHELL /bin/bash
ENV NB_USER jovyan
ENV NB_UID 1000
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Create jovyan user with UID=1000 and in the 'users' group
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

RUN chown -R $NB_USER:users /home/$NB_USER

WORKDIR /home/$NB_USER

#build proteus as $NBUSER
USER $NB_USER

RUN git clone https://github.com/erdc/stack && \
    cd stack && \
    git checkout ${SOURCE_COMMIT} && \
    echo ${SOURCE_COMMIT} && \
    git log | head -1 && \
    git submodule update --init --recursive && \
    ./hit/bin/hit init-home && \
    ./hit/bin/hit remote add https://proteus.cee.lsu.edu/hashdist_src --objects="source" && \
    ln -s examples/proteus.linux.yaml default.yaml && \
    ./hit/bin/hit build default.yaml -v && \
    cd /home/$NB_USER && \
    chmod u+rwX -R /home/$NB_USER/.hashdist/src && \
    rm -rf /home/$NB_USER/.hashdist/src && \
    rm -rf /home/$NB_USER/.cache && \
    chmod u+rwX -R /home/$NB_USER/.hashdist/bld/chrono/*/share/chrono/data && \
    rm -rf /home/$NB_USER/.hashdist/bld/chrono/*/share/chrono/data/* && \
    rm -rf /home/$NB_USER/stack
