from setuptools import setup, find_packages

setup(
    name="mkdocs-docker-tags",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'docker-tags = docker_tags.plugin:DockerTagsPlugin'
        ]
    },
)
