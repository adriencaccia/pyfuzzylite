"""
 pyfuzzylite (TM), a fuzzy logic control library in Python.
 Copyright (C) 2010-2017 FuzzyLite Limited. All rights reserved.
 Author: Juan Rada-Vilela, Ph.D. <jcrada@fuzzylite.com>

 This file is part of pyfuzzylite.

 pyfuzzylite is free software: you can redistribute it and/or modify it under
 the terms of the FuzzyLite License included with the software.

 You should have received a copy of the FuzzyLite License along with
 pyfuzzylite. If not, see <http://www.fuzzylite.com/license/>.

 pyfuzzylite is a trademark of FuzzyLite Limited
 fuzzylite is a registered trademark of FuzzyLite Limited.
"""
import io


def setup_package() -> None:
    with io.open('README.md', encoding='utf-8') as file:
        long_description = file.read()

    from distutils.core import setup
    setup(
        name="pyfuzzylite",
        version="7.0",
        description="a fuzzy logic control library in Python",
        long_description=long_description,
        # long_description_content_type='text/markdown',
        keywords=['fuzzy logic control', 'artificial intelligence'],
        url='https://www.fuzzylite.com/python/',
        download_url='https://www.fuzzylite.com/downloads/',
        # project_urls={
        #     'Home': 'https://www.fuzzylite.com/',
        #     'Documentation': 'https://www.fuzzylite.com/documentation',
        #     'Bug Tracker': 'https://github.com/fuzzylite/pyfuzzylite/issues',
        #     'Source Code': 'https://github.com/fuzzylite/pyfuzzylite',
        # },
        author="Juan Rada-Vilela, Ph.D.",
        author_email="jcrada@fuzzylite.com",
        maintainer="Juan Rada-Vilela, Ph.D.",
        maintainer_email="jcrada@fuzzylite.com",
        license="GNU General Public License v3.0",
        packages=['fuzzylite'],
        package_dir={'fuzzylite': '.'},
        # entry_points={
        #     'console_scripts': ['fuzzylite=fuzzylite:console']
        # },
        platforms=['OS Independent'],
        provides=['pyfuzzylite'],
        # python_requires='>=3.6',
        # setup_requires=['pytest-runner'],

        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'License :: Other/Proprietary License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Software Development :: Libraries',
        ],
        # zip_safe=True
    )


if __name__ == '__main__':
    setup_package()
