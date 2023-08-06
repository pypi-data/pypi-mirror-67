import setuptools  # type: ignore
from pathlib import Path

DEV_REQUIREMENTS = ["tox==3.14.5"]
TEST_REQUIREMENTS = ["black==19.10b0", "flake8==3.7.*", "flake8-bugbear==19.8.0", "mypy==0.770", "pytest==5.4.1"]
DOCS_REQUIREMENTS = ["Sphinx==2.2.*", "sphinx-argparse==0.2.*", "sphinx-autodoc-typehints==1.8.*"]
EXTRAS_REQUIRE = {
    "dev": DEV_REQUIREMENTS + TEST_REQUIREMENTS,
    "testing": TEST_REQUIREMENTS,
    "docs": DOCS_REQUIREMENTS,
}

setuptools.setup(
    name="openvpn-server",
    use_scm_version=True,
    author="Piotr Szczepaniak",
    author_email="szczep.piotr+openvpn-server@gmail.com",
    description="Python package for managing OpenVPN instances through their entire life cycle",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/D0han/openvpn-server",
    project_urls={
        "Bug Tracker": "https://gitlab.com/D0han/openvpn-server/-/issues",
        "Source": "https://gitlab.com/D0han/openvpn-server/-/tree/master",
        "Documentation": "https://openvpn-server.readthedocs.io/en/stable/",
    },
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    keywords=["openvpn", "management"],
    setup_requires=["setuptools_scm"],
    install_requires=["openvpn_api==0.2.0"],
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.6.0",
)
