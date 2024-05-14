from setuptools import setup, find_packages

setup(
    name='gcloud-run-flask-python',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.0.3',
        'gunicorn==22.0.0',
        'Werkzeug==3.0.3',
    ],
    entry_points={
        'console_scripts': [
            'gcloud-run-flask-python=your_package.main:main',
        ],
    },
)