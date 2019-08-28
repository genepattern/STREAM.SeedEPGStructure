FROM pinellolab/stream:0.3.8

RUN mkdir /stream
COPY structure_command_line.py /stream/structure_command_line.py

ENTRYPOINT []
