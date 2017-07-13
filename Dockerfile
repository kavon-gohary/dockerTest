
FROM python:3.5.2

COPY doctest.py /doctest.py

RUN pip install --upgrade pip && \
    pip --version             && \
	pip install coverage      && \
    pip install mypy          && \
    pip install numpy         && \
    pip install pylint

CMD ["python", "/doctest.py"]
