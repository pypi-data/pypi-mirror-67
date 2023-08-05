import setuptools
from distutils.core import setup

with open("README.md", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='ccy_dynamic_image',
    version='0.3',
    description='add dynamic effect to text or image',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chen Jiao',
    author_email='chenjiao@mail.ynu.edu.com',
    url='https://github.com/tenderzada/ccy_dynamic_images',
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=7.0.0', 'numpy==1.16.2'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'ccy_dynamic_image=ccy_dynamic_image:main'
        ],
    },
)
