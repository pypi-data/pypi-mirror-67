from distutils import log
from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist as _sdist

import os
from glob import glob
import shutil


def remove(path):
    """ param <path> could either be relative or absolute. """
    log.info("removing " + path)
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


class SDist(_sdist):
    def run(self):
        self.run_command("build_ext")
        _sdist.run(self)


def find_files_with_extension(base, extension):
    return glob(os.path.join(base, "**", "*." + extension), recursive=True)


class Clean(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        remove("build")
        for folder in glob("*.egg-info"):
            remove(folder)
        for pyd_file in find_files_with_extension("algopack", "pyd"):
            remove(pyd_file)
        for so_file in find_files_with_extension("algopack", "so"):
            remove(so_file)

        c_files = find_files_with_extension("algopack", "c")
        pyx_files = find_files_with_extension("algopack", "pyx")
        for c_file in c_files:
            if c_file[:-2] + ".pyx" in pyx_files:
                remove(c_file)


try:
    from Cython.Distutils.extension import Extension
    from Cython.Distutils import build_ext
except ImportError:
    from setuptools import Extension

    USING_CYTHON = False
else:
    USING_CYTHON = True

extension_kwargs = (
    dict(cython_directives={"language_level": 3, "embedsignature": True})
    if USING_CYTHON
    else dict()
)

ext = "pyx" if USING_CYTHON else "c"

sources = find_files_with_extension("algopack", ext)
extensions = [
    Extension(
        source.split(".")[0].replace(os.path.sep, "."),
        sources=[source],
        **extension_kwargs,
    )
    for source in sources
]

cmdclass = {"build_ext": build_ext, "sdist": SDist} if USING_CYTHON else {}
cmdclass["clean"] = Clean

with open("requirements.txt") as fp:
    install_requires = [line.strip() for line in fp if line.strip()]

with open("requirements_dev.txt") as fp:
    dev_requires = [line.strip() for line in fp if line.strip()]

if __name__ == "__main__":
    setup(
        packages=find_packages(exclude=("tests")),
        ext_modules=extensions,
        cmdclass=cmdclass,
        install_requires=install_requires,
        extras_require={"dev": dev_requires},
    )
