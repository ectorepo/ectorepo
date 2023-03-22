import sys
import os
import glob
from os.path import join
import manifest_xml

ecto_dir = os.environ("_ECTO")
repo_dir = os.environ("_REPO")
template = os.join(repo_dir, "_remotes.xml")

remotes_xml_files = glob.glob("*/_remotes.xml")
repo_paths = map(lambda p: split(p, "/")[0], remotes_xml_files)

print(template)
