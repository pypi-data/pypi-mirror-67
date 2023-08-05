import pathlib
import setuptools
setuptools.setup(
    name="txtoJson",
    version="1.1",
    long_description=pathlib.Path("d:\\vcode\\HOLA!\\Insp_Json\\README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests","data"])
) 
