#
#     Kwola is an AI algorithm that learns how to use other programs
#     automatically so that it can find bugs in them.
#
#     Copyright (C) 2020  Kwola Software Testing Inc.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requirements = [
    "mitmproxy",
    "mongoengine",
    "numpy",
    "opencv-python",
    "pandas",
    "psutil",
    "questionary",
    "requests",
    "scikit-image",
    "scikit-learn",
    "scipy",
    "selenium",
    "torch"
]

setup(
    name='kwola',
    version='0.1.1',
    description='Kwola makes an AI powered tool for finding bugs in software',
    long_description=open("README.md", "rt").read(),
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
    ],
    author='Bradley Arsenault',
    author_email='brad@kwola.io',
    url='https://kwola.io/',
    keywords='torch pytorch artificial intelligence',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
    },
    package_data={
        'kwola': [
            'config/prebuilt_configs/*.json'
        ]
    },
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'kwola = kwola.bin.main:main',
            'kwola_init = kwola.bin.initialize:main',
            'kwola_train_agent = kwola.bin.train_agent:main',
            'kwola_run_train_step = kwola.bin.run_train_step:main',
            'kwola_run_test_step = kwola.bin.run_test_step:main',
            'kwola_rapid_local_test_suite = kwola.bin.rapid_local_test_suite:main',
            'kwola_full_internal_test_suite = kwola.bin.full_internal_test_suite:main',
            'kwola_test_chromedriver = kwola.bin.test_chromedriver:main',
            'kwola_test_javascript_rewriting = kwola.bin.test_javascript_rewriting:main',
            'kwola_test_ffmpeg = kwola.bin.test_ffmpeg:main',
            'kwola_test_neural_network = kwola.bin.test_neural_network:main',
            'kwola_test_installation = kwola.bin.test_installation:main',
            'kwola_install_proxy_cert = kwola.bin.install_proxy_cert:main'
        ]
    }
)
