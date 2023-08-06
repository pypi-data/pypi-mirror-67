
# Copyright 2020 Erik Soma
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# python
import pathlib
import platform
import setuptools

README_FILE_PATH = pathlib.Path(__file__).parent.absolute().joinpath(
    'README.md'
)
with open(README_FILE_PATH) as f:
    long_description = f.read()
    
if platform.system() == "Windows":
    platform_install_requires = ["pywin32"]

setuptools.setup(
    name='jellybean-esoma',
    version='0.0.1',
    author='Erik Soma',
    author_email='stillusingirc@gmail.com',
    description='3D Game Engine',
    tests_require=["pytest"],
    install_requires=[] + platform_install_requires,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/esoma/jellybean',
    #packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment',
    ],
    python_requires='>=3.8',
)
