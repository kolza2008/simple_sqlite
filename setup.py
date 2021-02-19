import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_sqlite-kolza2008", # Replace with your own username
    version="0.5",
    author="Nikolay Nikushin",
    author_email="kolza2008@bk.ru",
    description="Library for simplify work with sqlite3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kolza2008/simple_sqlite",
    packages=setuptools.find_packages(),
    python_requires='>=3.1',
)