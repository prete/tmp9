import setuptools

def get_readme():
    with open("README.md", "rt", encoding="utf-8") as fh:
        return fh.read()

def get_requirements():
    with open("requirements.txt", "rt", encoding="utf-8") as fh:
        return [line.strip() for line in fh.readlines()]

setuptools.setup(
    name="cellphonedb",
    version="5.0.0,
    packages=setuptools.find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.6'
)
