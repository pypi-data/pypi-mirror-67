from setuptools import setup

setup(
    name="NoseHTML",
    version="0.4.6",
    description="""HTML Output plugin for Nose / Nosetests""",
    url='https://github.com/galaxyproject/nosehtml',
    author='James Taylor, Nate Coraor, Dave Bouvier',
    author_email='james@taylorlab.org',
    license='MIT',
    install_requires=['nose'],
    packages=['nosehtml'],
    entry_points={
        'nose.plugins.0.10': ['nosehtml = nosehtml.plugin:NoseHTML']
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
    ]
)
