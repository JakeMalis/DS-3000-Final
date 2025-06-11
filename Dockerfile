# Use NVIDIA's PyTorch container as base
FROM nvcr.io/nvidia/pytorch:25.05-py3

# Set working directory
WORKDIR /workspace

# Copy requirements.txt into the container
COPY requirements.txt .

# Install Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
