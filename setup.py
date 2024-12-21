from setuptools import setup, find_packages

setup(
    name="CustomCLILang",  # Replace with a unique name
    version="1.0.0",
    description="A custom CLI programming language for handling Windows tasks.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="vinit",
    author_email="vineetp6@gmail.com",
    url="https://github.com/vineetp6/CustomCLILang.git",  
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "customcli=cli_interpreter:main",  # Exposed `customcli` as a CLI command
        ],
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    license="MIT",
)
