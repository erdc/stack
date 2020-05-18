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

EXPOSE 8888

#build proteus as $NBUSER
USER $NB_USER

WORKDIR /home/$NB_USER

RUN ./hit/bin/hit init-home && \
    ./hit/bin/hit remote add http://levant.hrwallingford.com/hashdist_src --objects="source" && \
    ln -s examples/proteus.linux.yaml default.yaml && \
    ./hit/bin/hit -j 1 build default.yaml -v && \
    chmod u+rwX -R /home/$NB_USER/.hashdist/src && \
    rm -rf rm -rf /home/$NB_USER/.hashdist/src && \
    rm -rf /home/$NB_USER/.cache && \
    chmod u+rwX -R /home/$NB_USER/.hashdist/bld/chrono/*/share/chrono/data && \
    rm -rf /home/$NB_USER/.hashdist/bld/chrono/*/share/chrono/data/* && \
    rm -rf /home/$NB_USER/proteus/.git && \
    rm -rf /home/$NB_USER/stack/.git && \
    rm -rf /home/$NB_USER/air-water-vv/.git && \
    rm -rf /home/$NB_USER/proteus/air-water-vv && \
    rm -rf /home/$NB_USER/proteus/build && \
    rm -rf /home/$NB_USER/proteus/stack/default

WORKDIR /home/$NB_USER
