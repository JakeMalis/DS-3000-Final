FROM nvcr.io/nvidia/pytorch:25.03-py3

# Install requirements.txt
RUN pip install --no-deps --requirement requirements.txt --ignore-installed
