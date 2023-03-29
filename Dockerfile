FROM openjdk:17.0.2-jdk

RUN microdnf upgrade && \
    microdnf install libXext libXrender libXtst

RUN microdnf install python3

COPY ./xGTM_portal /xGTM_portal

RUN chmod -R +rx /xGTM_portal/