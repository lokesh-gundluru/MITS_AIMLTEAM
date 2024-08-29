from setuptools import setup,find_packages


setup(
    name='MITS_AIMLTEAM',
    version='0.1',
    author='Lokesh Gundluru, M C Bhargav, Yaseer Ahammad',
    author_email='lokesh.gundluru@example.com',
    description='A Python package for similarity measures such as Hamming, Jaccard, and Overlap coefficients.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/lokesh-gundluru/MITS_AIMLTEAM',
    license='GPLv3',

    classifiers=[
        'Development Status :: 4 - Beta',  # Update according to your package status
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
