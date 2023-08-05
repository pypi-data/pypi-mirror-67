### Introduction

genre, a simple and concise `requirements.txt` generator.

When using `pip freeze > requirements.txt`, many indirect dependencies are listed, which is not elegant. This simple tool aims to provide a concise `requirements.txt`, which means it only export direct third-party dependencies or imports in your project.

> usage: genre [-h] [-p PACKAGE_DIR] [-v {0,1}]
>
> optional arguments:
>   -h, --help            show this help message and exit
>   -p PACKAGE_DIR, --package_dir PACKAGE_DIR
>                         your package path
>   -v {0,1}, --add_version {0,1}
>                         add version (1) or not (0)

### FAQ

Q: What does "Below are unsure project names (manual check needed)" mean?

A: Normally, this message should not appear in generated `requirements.txt`. If you see it unluckily, it means one third-party import in your project is mapped to multiple packages. Manual check is needed to verify which package(s) is/are real dependency(ies).