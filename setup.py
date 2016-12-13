from setuptools import setup, find_packages
setup(
    name="HelloWorld",
    version="0.1",
    packages=["foobar"],
    entry_points={
        "console_script":[
    "foobard=foobar.sever.main",
    "foobar=foobar.client.main",
    ]
    },
)