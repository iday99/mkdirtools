from setuptools import setup, find_packages

setup(
    name="mkdirtools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mkdirtools=mkdirtools.main:main",
        ],
    },
    
    # 元数据
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for generating directory structures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="directory, structure, generator",
    url="https://github.com/yourusername/mkdirtools",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)