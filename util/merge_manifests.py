import sys
import os
import glob
from os.path import join

#import manifest_xml
from manifest_xml import *
#from manifest_xml import GitcManifest
#from manifest_xml import XmlManifest, GitcManifest, GitcClient
#from manifest_xml import GitcManifest, RepoClient

ecto_dir = os.environ["_ECTO"]
repo_dir = os.environ["_REPO"]
template = join(repo_dir, "_remotes.xml")

remotes_xml_files = glob.glob("*/_remotes.xml")
repo_names = list(map(lambda p: p.split("/")[0], remotes_xml_files))
ecto_paths = list(map(lambda n: "/".join([ecto_dir,n]), repo_names))

#ecto_manifests = list(map(lambda i: GitcManifest(ecto_paths[i], remotes_xml_files[i]),
#                          range(len(remotes_xml_files))))
ecto_manifests = list(map(lambda i: RepoClient(ecto_paths[i], remotes_xml_files[i]),
                          range(len(remotes_xml_files))))

#print(ecto_manifests[0].remotes)
#repo_remote_xml = GitcManifest(".", "_remotes.xml")
#print(repo_remote_xml.remotes)
print(template)
