from setuptools import setup, find_packages

setup(
    name='AIChat',
    version='0.1.0',
    description='A chat framwork to let user create a character and chat with it via openai models',
    author='Elon Ezra',
    author_email='elon-kadatz@outlook.com',
    packages=find_packages(),
    install_requires=["openai"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)