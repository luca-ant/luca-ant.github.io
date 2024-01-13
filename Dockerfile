FROM ubuntu:22.04

RUN apt update
RUN apt install -y bash curl
RUN apt install -y ruby-full build-essential zlib1g-dev

RUN mkdir -p /site

RUN DOCKER_USER=jekyll && \
    groupadd -g 5000 $DOCKER_USER && \
    useradd -m -u 5000 -g $DOCKER_USER -s $(which nologin) $DOCKER_USER && \
    usermod -L $DOCKER_USER && \
    chown -R $DOCKER_USER:$DOCKER_USER /home/$DOCKER_USER && \
    chown -R $DOCKER_USER:$DOCKER_USER /site

# USER jekyll
# ENV PATH="$PATH:/home/jekyll/.local/share/gem/ruby/3.0.0/bin"

RUN gem install jekyll bundler && gem cleanup

COPY entrypoint.sh /usr/local/bin

#COPY ./site /site

WORKDIR /site

EXPOSE 1409

# USER jekyll

# ENTRYPOINT [ "entrypoint.sh" ]
CMD [ "jekyll", "--help" ]
