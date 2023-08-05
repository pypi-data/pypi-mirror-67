import setuptools

def obtain_version():
    def version_scheme(version):
        return version.format_with("{tag}")

    def local_scheme(version):
        if version.exact:
            metadata = \
                version.format_choice(
                    clean_format="",
                    dirty_format="+dirty"
                )
        else:
            metadata = "+" + version.node[1:]
            metadata = \
                version.format_choice(
                    clean_format=metadata,
                    dirty_format=metadata + ".dirty"
                )
        return metadata

    return {
        "version_scheme": version_scheme,
        "local_scheme": local_scheme,
    }

setuptools.setup(
    name="rockart",
    use_scm_version=obtain_version,
    description="A tool for drawing in terminal using Braille characters",
    keywords="pseudographics semigraphics braille terminal console",
    license="MIT",
    author="van-kalsing",
    author_email="kalsin@inbox.ru",
    url="https://github.com/van-kalsing/rockart",
    project_urls={
        "Bug Tracker": "https://github.com/van-kalsing/rockart/issues",
        "Source Code": "https://github.com/van-kalsing/rockart",
    },
    zip_safe=True,
    packages=["rockart"],
    python_requires=">=3.6.9",
    setup_requires=["setuptools_scm==3.2.0"],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Terminals",
    ],
)
