#################################
Sluggard - auto packaging tool
#################################

*********
features
*********

+ archiving (tar)
+ compression (gzip, bzip2, xz)
+ ignore file

***********
how to use
***********

1. write ignore file
2. run sluggard command

ignore file
===============

example (`.packignore` file)

::

    .git/
    venv/
    dev/
    !.gitkeep


sluggard command
==================

::

    # only need -o option
    sluggard -o <output file>
    sluggard -o package.tar  # no compress
    sluggard -o package.tar.gz  # gz compress
    sluggard -o package.tar.xz  # xz compress
    sluggard -o package.tar.bz2  # bz2 compress

    # package specified directory (if not provided, use current directory)
    sluggard -o <output file> /path/to/directory

    # show help -h or --help
    sluggard -h
