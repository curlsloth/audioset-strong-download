from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='audioset-strong-download',
    version='2.0.5',
    description='This package aims at simplifying the download of the strong version of AudioSet dataset. This is a revised version of audioset-download (https://github.com/MorenoLaQuatra/audioset-download).',
    py_modules=["Downloader"],
    packages=find_packages(include=['audioset_strong_download', 'audioset_strong_download.*']),
    classifiers={
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    },
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [
        "ffmpeg==1.4",
        "joblib",
        "pandas",
        "yt-dlp>=2024.12.6",
        "numpy", 
    ],
    extras_require = {
        "dev" : [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/curlsloth/audioset-strong-download",
    author="Andrew Chang & Moreno La Quatra",
    author_email="c.andrew123@gmail.com",
)
