FROM ubuntu:18.04

ADD main /
ADD docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]
