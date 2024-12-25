# from setuptools import setup, find_packages  # Ensure this is imported

# setup(
#     name="CustomWindowsCLILang",  # New package name
#     version="2.0.1",
#     description="A custom CLI programming language for handling Windows tasks.",
#     long_description=open("README.md", "r", encoding="utf-8").read(),
#     long_description_content_type="text/markdown",
#     author="vinit",
#     author_email="vineetp6@gmail.com",
#     url="https://github.com/vineetp6/CustomWindowsCLILang",  # Update GitHub repo URL if applicable
#     packages=find_packages(),
#     entry_points={
#         "console_scripts": [
#             "customwincli=cli_interpreter:main",  # New CLI command
#         ],
#     },
#     install_requires=[],
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "Operating System :: Microsoft :: Windows",
#         "License :: OSI Approved :: MIT License",
#     ],
#     python_requires=">=3.7",
#     license="MIT",
# )


from setuptools import setup, find_packages

setup(
    name="CustomWindowsCLILang",
    version="2.0.3",  # Increment version number
    description="A custom CLI language for managing Windows tasks",
    author="vinit",
    author_email="vineetp6@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'open=core.cli_interpreter:main',  # Ensure 'main' exists in cli_interpreter.py
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)


