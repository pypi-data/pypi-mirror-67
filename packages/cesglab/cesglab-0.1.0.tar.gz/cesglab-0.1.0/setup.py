"cesglab setup module."

def main():

    from setuptools import setup
    from cesglab.main import CESGlab as clab

    console_scripts = ["cesglab=cesglab.__main__:main"]
    install_requires = ["microapp>=0.1.12", "xrcalc>=0.1.5"]

    setup(
        name=clab._name_,
        version=clab._version_,
        description=clab._description_,
        long_description=clab._long_description_,
        author=clab._author_,
        author_email=clab._author_email_,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        keywords="cesglab",
        packages=[ "cesglab" ],
        include_package_data=True,
        install_requires=install_requires,
        entry_points={ "console_scripts": console_scripts,
            "microapp.projects": "cesglab = cesglab"},
        project_urls={
            "Bug Reports": "https://github.com/grnydawn/cesglab/issues",
            "Source": "https://github.com/grnydawn/cesglab",
        }
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
