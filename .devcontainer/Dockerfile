FROM python:3.12

# https://python-poetry.org/docs/#ci-recommendations
RUN mkdir /root/.poetry && \
  python -m venv /root/.poetry && \
  /root/.poetry/bin/pip install poetry && \
  echo 'PATH=$PATH:/root/.poetry/bin' >> /root/.bashrc

RUN /root/.poetry/bin/poetry config virtualenvs.in-project true
RUN git config --global init.defaultBranch main