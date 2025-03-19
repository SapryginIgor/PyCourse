FROM python:3.10

WORKDIR /app

RUN apt-get update && apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended

COPY test_tex_maker.py frog.jpeg pyproject.toml script.sh /app/

ENV PATH="/root/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

RUN chmod +x script.sh

CMD [ "./script.sh" ]

