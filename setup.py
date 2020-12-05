"""
    PyIDM
    multi-connections internet download manager, based on "LibCurl", and "youtube_dl".
    :copyright: (c) 2019-2020 by Mahmoud Elshahat.
    :license: GNU LGPLv3, see LICENSE for more details.
"""

import os
import setuptools

# get current directory
path = os.path.realpath(os.path.abspath(__file__))
current_directory = os.path.dirname(path)

# get version
version = {}
with open(f"{current_directory}/pyidm/version.py") as f:
    exec(f.read(), version)  # then we can use it as: version['__version__']

# get long description from readme
with open(f"{current_directory}/README.md", "r") as fh:
    long_description = fh.read()

try:
    with open(f"{current_directory}/requirements.txt", "r") as fh:
        requirements = fh.readlines()
except:
    requirements = ['plyer', 'certifi', 'youtube_dl', 'youtube_dlc', 'pycurl', 'pillow', 'pystray',
                    'awesometkinter >= 2020.9.22']

setuptools.setup(
    name="PyIDM",
    version=version['__version__'],
    scripts=[],  # ['PyIDM.py'], no need since added an entry_points
    author="Mahmoud Elshahat",
    author_email="info.pyidm@gmail.com",
    description="download manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pyIDM/PyIDM ",
    packages=setuptools.find_packages(),
    keywords="internet download manager youtube downloader pycurl curl youtube-dl",
    project_urls={
        'Source': 'https://github.com/pyIDM/PyIDM',
        'Tracker': 'https://github.com/pyIDM/PyIDM/issues',
        'Releases': 'https://github.com/pyIDM/PyIDM/releases',
        'Screenshots': 'https://github.com/pyIDM/PyIDM/issues/13#issuecomment-689337428'
    },
    install_requires=requirements,
    entry_points={
        # our executable: "exe file on windows for example"
        'console_scripts': [
            'pyidm = pyidm.PyIDM:main',
        ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
