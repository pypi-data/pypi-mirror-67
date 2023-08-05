# File/Folder utilities
#
# Author: F. Mertens

import re
import os
import shutil


def reglob(path, exp, invert=False):
    m = re.compile(exp)

    if invert is False:
        res = [f for f in os.listdir(path) if m.search(f)]
    else:
        res = [f for f in os.listdir(path) if not m.search(f)]

    return map(lambda x: "%s/%s" % (path, x, ), res)


def rm_if_exist(directory, verbose=False):
    if os.path.exists(directory):
        if verbose:
            print('Remove ' + directory)
        shutil.rmtree(directory)


def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def abspath(p):
    return os.path.abspath(os.path.expanduser(p))


def is_file(f):
    return os.path.isfile(os.path.expanduser(f))


def zip_copy(dir_ins, dir_outs, filename, verbose=True):
    for dir_in, dir_out in zip(dir_ins, dir_outs):
        if verbose:
            print(f'Copy {dir_in}/{filename} -> {dir_out}/{filename}')
        shutil.copyfile(f'{dir_in}/{filename}', f'{dir_out}/{filename}')


def zip_copytree(dir_ins, dir_outs, dirname, verbose=True):
    for dir_in, dir_out in zip(dir_ins, dir_outs):
        if verbose:
            print(f'Copy {dir_in}/{dirname} -> {dir_out}/{dirname}')
        shutil.copytree(f'{dir_in}/{dirname}', f'{dir_out}/{dirname}')


def zip_rename(dir_ins, dir_outs, filename_or_dirname=None, verbose=True):
    for f_in, f_out in zip(dir_ins, dir_outs):
        if filename_or_dirname is not None:
            f_in = f'{f_in}/{filename_or_dirname}'
            f_out = f'{f_out}/{filename_or_dirname}'
        if verbose:
            print(f'Rename {f_in} -> {f_out}')
        os.rename(f_in, f_out)


def zip_rename_reg(dir_ins, dir_outs, regex, verbose=True, invert=False):
    for f_in, f_out in zip(dir_ins, dir_outs):
        for f_in2 in reglob(f_in, regex, invert=invert):
            f_out = f'{f_out}/{os.path.basename(f_in2)}'
            if verbose:
                print(f'Rename {f_in2} -> {f_out}')
            os.rename(f_in2, f_out)


def zip_rm(dirs, verbose=True):
    for directory in dirs:
        rm_if_exist(directory, verbose=verbose)
