#!/usr/bin/env python
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See dcm2bidsphysio.py file for the copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

import os.path as op

from setuptools import findall, setup, find_packages


def main():

    thispath = op.dirname(__file__)
    ldict = locals()

    # Get version and release info, which is all stored in info.py
    info_file = op.join(thispath, 'bidsphysio', 'info.py')
    with open(info_file) as infofile:
        exec(infofile.read(), globals(), ldict)


    def findsome(subdir, extensions):
        """Find files under subdir having specified extensions

        Leading directory (datalad) gets stripped
        """
        return [
            f.split(op.sep, 1)[1] for f in findall(subdir)
            if op.splitext(f)[-1].lstrip('.') in extensions
        ]
    # Only recentish versions of find_packages support include
    # bidsphysio_pkgs = find_packages('.', include=['bidsphysio*'])
    # so we will filter manually for maximal compatibility
    bidsphysio_pkgs = [pkg for pkg in find_packages('.') if pkg.startswith('bidsphysio')]


    setup(
        name=ldict['__packagename__'],
        author=ldict['__author__'],
        author_email=ldict['__author_email__'],
        version=ldict['__version__'],
        description=ldict['__description__'],
        long_description=ldict['__longdesc__'],
        license=ldict['__license__'],
        classifiers=ldict['CLASSIFIERS'],
        packages=bidsphysio_pkgs,
        entry_points={'console_scripts': [
            'physio2bidsphysio=bidsphysio.physio2bidsphysio:main',
            'dcm2bidsphysio=bidsphysio.dcm2bidsphysio:main',
            'acq2bidsphysio=bidsphysio.acq2bidsphysio:main',
            'pmu2bidsphysio=bidsphysio.pmu2bidsphysio:main',
        ]},
        python_requires=ldict['PYTHON_REQUIRES'],
        install_requires=ldict['REQUIRES'],
        extras_require=ldict['EXTRA_REQUIRES'],
        package_data={
            'bidsphysio.tests': [
                        op.join('data', '*.acq'),
                        op.join('data', '*.dcm'),
                        op.join('data', '*.puls'),
                        op.join('data', '*.resp'),
                        op.join('data', '*.tsv')
            ],
        }
    )


if __name__ == '__main__':
    main()
