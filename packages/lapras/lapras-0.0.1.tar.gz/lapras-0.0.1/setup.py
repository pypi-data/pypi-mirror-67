from setuptools import setup
from codecs import open


setup(
    name='lapras',
    version='0.0.1',
    author='Badtom',
    author_email='yhangang@gmail.com',
    description='An automatic scorecard package.',
    url='https://gitlab.com/badtom/scorecardlapras',
    license='MIT',
    keywords='scorecard',
    packages=[],
    entry_points = {'console_scripts': [
       'MSE-Manager = MSE.Worker.Manager:main',
   ]},
    install_requires=[],


)
