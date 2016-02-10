#!/usr/bin/python

import sys
import os.path
import utils
from fileDownloader import getFiles

if len(sys.argv) not in (2, 3):
    print('Usage: %s <path> [extensions]' %sys.argv[0])
    sys.exit(1)

path = os.path.abspath(sys.argv[1])
if len(sys.argv) > 2:
    # pipe sign is reserved in bash, so replace it
    extensions = sys.argv[2].replace(',','|')
else:
    extensions = utils.DEFAULT_EXTENSIONS_REGEX

extCompile = utils.regexCompile(utils.extensionify(extensions))

getFiles(url=path, extCompile=extCompile, recursionDepth=1, httpDomain='file://')

