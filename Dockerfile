FROM glotzerlab/software
USER root
RUN python3 -m pip install signac-dashboard
COPY dashboard.py /
ENTRYPOINT python3 dashboard.py run --port=9000
