FROM python:3.7.9-slim-buster
RUN apt-get update 
RUN apt-get -y install poppler-utils --fix-missing
RUN apt-get -y install tesseract-ocr

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
ENV HOME  /home/user
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> .bashrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> .bashrc
RUN echo 'eval "$(pyenv init -)"' >> .bashrc


RUN python -m pip install --upgrade pip && pip install pipenv
COPY Pipfile* ./
RUN pipenv install --deploy
COPY ./app ./app
EXPOSE 8000
CMD uvicorn app.main:app --host 0.0.0.0 
