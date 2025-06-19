from setuptools import setup, find_packages

setup(
    name='taming-transformers',
    version='0.0.1',
    description='Taming Transformers for High-Resolution Image Synthesis',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'torchaudio',
        'numpy',
        'albumentations',
        'opencv-python',
        'pudb',
        'imageio',
        'imageio-ffmpeg',
        'pytorch-lightning',
        'omegaconf',
        'test-tube',
        'streamlit',
        'einops',
        'more-itertools',
        'transformers',
    ],
)
