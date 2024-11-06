# setup.py
from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",                          # Name of your project
    version="0.1.0",                            # Version
    description="Math game + tests",
    long_description=open("README.md").read(),  # Full description (usually from README)
    long_description_content_type="text/markdown",
    author="Joana Joanidopoulos",
    author_email="joana.joanidopoulos@fau.de",
    url="https://github.com/Josie-fau/dsss_homework_2",
    packages=find_packages(),                   # Automatically finds packages in your project
    install_requires=[
        # Add dependencies here, e.g., "requests", "numpy>=1.18.0"
    ],
    python_requires=">=3.6",                    # Python version requirement
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
