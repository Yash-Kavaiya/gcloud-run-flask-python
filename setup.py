from setuptools import setup, find_packages

setup(
    name='gcloud-run-flask-python',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.3',
        'gunicorn==22.0.0',
        'Werkzeug==3.0.3'
    ],
    entry_points={
        'console_scripts': [
            'gcloud-run-flask-python = gcloud_run_flask_python.cli:main'
        ]
    }
)
