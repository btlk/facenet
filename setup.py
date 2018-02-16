from setuptools import setup
import os

setup(
    name='facenet',

    version='1.0.0',

    description='Facenet',

    author='Alex Serikov & David Sandberg',
    author_email='ivanmitrafanych@gmail.com',

    license='MIT',

    packages=['facenet', 'facenet.align'],

    package_dir={'facenet': 'facenet', 'facenet.align': os.path.join('facenet', 'align')},
    package_data={'facenet.align': ['det1.npy', 'det2.npy', 'det3.npy']},

    python_requires='>=3.6, <3.7',
)
