import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent
readme = (here / "README.rst").read_text(encoding="utf-8")
changelog = (here / "CHANGELOG.rst").read_text(encoding="utf-8")

setup(
    name="epiweeks-barc",
    version="0.0.1",
    description="Epidemiological weeks based on the CDC (MMWR) and ISO week "
    "numbering systems.",
    long_description="\n".join([readme, changelog]),
    long_description_content_type="text/x-rst",
    url="https://github.com/ankusharya/epiweeks",
    project_urls={"Documentation": "https://epiweeks.readthedocs.io/"},
    author="Ankush Singh",
    author_email="",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
        "Typing :: Typed"
    ],
    keywords="epidemiology weeks cdc mmwr iso calendar surveillance "
    "public-health",
    py_modules=[module.stem for module in here.glob("src/*.py")],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
)
