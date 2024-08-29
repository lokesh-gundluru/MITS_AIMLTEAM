import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='MITS_AIMLTEAM',
    version='2024.08.29',
    author='Lokesh Gundluru, M C Bhargav, Yaseer Ahammad',
    author_email='lokesh.gundluru@example.com',
    description='A Python package for similarity measures such as Hamming, Jaccard, and Overlap coefficients.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/lokesh-gundluru/MITS_AIMLTEAM.git',
    license='MIT',
    install_requires=[

         'numpy',
         'scipy',

    ],
    extras_require={
        # Optional dependencies for additional features
        'dev': ['pytest', 'twine', 'setuptools', 'wheel'],
        'docs': ['sphinx', 'sphinx_rtd_theme'],
        'all': ['pytest', 'twine', 'setuptools', 'wheel', 'sphinx', 'sphinx_rtd_theme']
    },
    classifiers=[
        'Development Status :: 4 - Beta',  # Update according to your package status
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
