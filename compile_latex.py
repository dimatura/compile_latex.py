#!/usr/bin/env python

import time
import argparse
import subprocess

parser = argparse.ArgumentParser('compile_latex.py')
parser.add_argument('tex_files', nargs='+')
args = parser.parse_args()

# for now use rubber. funny thing is that rubber is already a
# python script.
cmd = ['rubber', '--pdf'] + args.tex_files

while True:
    subprocess.call(cmd)
    time.sleep(1)
