# from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dedebug',  # How you named your package folder (MyLib)
    packages=['dedebug'],  # Chose the same as "name"
    version='0.7',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Telegram debuger',  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mark',  # Type in your name
    author_email='markolofsen@gmail.com',  # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/user/markolofsen',
    # download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    keywords=['telegram'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'requests',
    ],
    setup_requires=["wheel"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
