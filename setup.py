from setuptools import find_packages, setup

with open('README.md', 'r', encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name='flaskr',
    version='0.0.1',
    author='mnichangxin',
    author_email='mnichangxin@163.com',
    url='https://github.com/mnichangxin/vue-blog-server',
    description='Flask server',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
