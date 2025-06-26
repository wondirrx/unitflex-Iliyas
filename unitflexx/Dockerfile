FROM python:3.11-slim as builder

WORKDIR /app
COPY . .

RUN pip install -e . && \
    python -m pip install --upgrade build && \
    python -m build && \
    pip install --no-cache-dir dist/*.whl

FROM python:3.11-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/unitflex /usr/local/bin/unitflex

# Verify CLI works
RUN unitflex --help > /dev/null

ENTRYPOINT ["unitflex"]