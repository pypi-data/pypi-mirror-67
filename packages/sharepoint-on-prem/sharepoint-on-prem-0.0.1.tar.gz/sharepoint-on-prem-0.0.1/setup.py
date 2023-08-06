from setuptools import setup

setup(
    name="sharepoint-on-prem",
    version="0.0.1",
    author="Shimeng Zhao",
    author_email="zhaoshimeng2015@gmail.com",
    packages=["sp_on_prem"],
    install_requires=["requests_ntlm2"],
)
