from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='scrapy-post2wp',
    version='1.0.0',
    description='',
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/maximiliancw/scrapy-post2wp',  # Optional
    author='Maximilian Wolf',
    author_email='maximilian.wolf@innovinati.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='scrapy, wordpress, content-aggregation',
    packages=['scrapy_post2wp'],
    python_requires='>=3.8, <4',
    install_requires=['requests', 'scrapy']
)
