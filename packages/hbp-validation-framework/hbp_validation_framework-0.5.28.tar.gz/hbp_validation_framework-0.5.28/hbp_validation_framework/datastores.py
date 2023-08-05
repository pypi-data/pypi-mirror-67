"""
Defines classes for interacting with remote data stores.

Currently supported:
    - HBP Collaboratory storage
    - Swift CSCS storage
    - ModelDB

Other possibilities:
    - Fenix storage
    - Zenodo
    - Open Science Framework
    - Figshare
    - Dropbox
    - OwnCloud
    - ...
"""

import os
import json
try:
    input = raw_input  # Py2
    from urllib import urlretrieve
    from urlparse import urlparse
except (NameError, ImportError):
    from urllib.request import urlretrieve  # Py3
    from urllib.parse import urlparse
import mimetypes
import requests
from hbp_service_client.storage_service.api import ApiClient

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # Python 2 backport

try:
    raw_input
except NameError:  # Python 3
    raw_input = input

mimetypes.init()


class FileSystemDataStore(object):
    """
    A class for interacting with the local file system
    """

    def __init__(self, **kwargs):
        pass

    def load_data(self, local_path):
        with open(local_path) as fp:
            observation_data = json.load(fp)


class CollabDataStore(object):
    """
    A class for uploading and downloading data from HBP Collaboratory storage.
    """

    def __init__(self, collab_id=None, base_folder=None, auth=None, **kwargs):
        self.collab_id = collab_id
        self.base_folder = base_folder
        self._auth = auth  # we defer authorization until needed
        self._authorized = False

    @property
    def authorized(self):
        return self._authorized

    def authorize(self, auth=None):
        if auth is None:
            auth = self._auth
        self.doc_client = ApiClient.new(auth.token)
        self._authorized = True

    def _translate_URL_to_UUID(self, url):
        """
        Can take a path such as:
        `https://collab-storage-redirect.brainsimulation.eu/5165/hippoCircuit_20171027-142713`
        with 5165 being the Collab ID and the latter part being the collab path,
        and translate this to the UUID on the HBP Collaboratory storage.
        """
        if not self.authorized:
            self.authorize(self._auth)
        path = url.split("https://collab-storage-redirect.brainsimulation.eu")[1]
        entity = self.doc_client.get_entity_by_query(path=path)
        return entity["uuid"]

    def _translate_UUID_to_URL(self, uuid):
        """
        Can take a UUID on the HBP Collaboratory storage path and translate this
        to a path such as:
        `https://collab-storage-redirect.brainsimulation.eu/5165/hippoCircuit_20171027-142713`
        with 5165 being the Collab ID and the latter part being the collab storage path.
        """
        if not self.authorized:
            self.authorize(self._auth)
        path = self.doc_client.get_entity_path(uuid)
        return "https://collab-storage-redirect.brainsimulation.eu{}".format(path)

    def upload_data(self, file_paths):
        if not self.authorized:
            self.authorize(self._auth)
        projects_in_collab = self.doc_client.list_projects(collab_id=self.collab_id,
                                                           access='write')["results"]
        assert len(projects_in_collab) == 1
        project_id = projects_in_collab[0]["uuid"]
        base_folder_id = self._make_folders(self.base_folder, parent=project_id)

        # determine common sub-path to use as base directory
        # we retain directory structure below this common sub-path
        if len(file_paths) > 1:
            common_base_dir = os.path.commonpath(file_paths)
        else:
            common_base_dir = os.path.dirname(file_paths[0])

        relative_paths = [os.path.relpath(p, common_base_dir) for p in file_paths]

        uploaded_file_paths = []
        for local_path, relative_path in zip(file_paths, relative_paths):
            if os.path.dirname(relative_path):
                parent = self._make_folders(os.path.dirname(relative_path), parent=base_folder_id)
            else:
                parent = base_folder_id

            filename = os.path.basename(relative_path)
            content_type = mimetypes.guess_type(local_path)[0]
            file_entity = self.doc_client.create_file(filename, content_type, parent)
            etag = self.doc_client.upload_file_content(file_entity['uuid'],
                                                       source=local_path)
            uploaded_file_paths.append("https://collab-storage-redirect.brainsimulation.eu{}"
                                       .format(self.doc_client.get_entity_path(file_entity['uuid'])))
        return uploaded_file_paths

    def _make_folders(self, folder_path, parent):
        for i, folder_name in enumerate(folder_path.split(os.path.sep)):
            # might not retrieve all entries; increase page size further if required (unlikely)
            folders = self.doc_client.list_folder_content(parent, entity_type="folder", page_size=10000)["results"]
            folder_exists = False
            for f in folders:
                if folder_name in f["name"]:
                    child = f['uuid']
                    folder_exists = True
                    break
            if not folder_exists:
                child = self.doc_client.create_folder(folder_name, parent=parent)['uuid']
            parent = child
        return child

    def _download_data_content(self, remote_path):
        if not self.authorized:
            self.authorize(self._auth)
        # need to support other formats besides JSON
        if remote_path.startswith("https://collab-storage-redirect.brainsimulation.eu"):
            remote_path = remote_path[len("https://collab-storage-redirect.brainsimulation.eu"):]

        entity = self.doc_client.get_entity_by_query(path=remote_path)
        if entity["entity_type"] == 'file':
            etag, content = self.doc_client.download_file_content(entity["uuid"])
        else:
            raise IOError("Can only load data from individual files, not from {}".format(entity["entity_type"]))
        return content

    def download_data(self, remote_paths, local_directory="."):
        """
        Note: This can only download files (not directories)
        """
        if isinstance(remote_paths, str):
            remote_paths = [remote_paths]
        local_paths = []
        for remote_path in remote_paths:
            local_path = os.path.join(local_directory, os.path.basename(remote_path))
            Path(os.path.dirname(local_path)).mkdir(parents=True, exist_ok=True)
            with open(local_path, "wb") as fp:
                fp.write(self._download_data_content(remote_path))
            local_paths.append(local_path)
        return local_paths

    def download_data_using_uuid(self, uuid, local_directory="."):
        """
        Downloads the resource specified by the UUID on the HBP Collaboratory.
        Target can be a file or a folder. Returns a list containing absolute
        filepaths of all downloaded files.
        Note: This can recursively download files and sub-directories
              within a specified directory
        """
        file_uuids = []

        if not self.authorized:
            self.authorize(self._auth)
        entity = self.doc_client.get_entity_details(uuid)
        if entity["entity_type"] == 'file':
            file_uuids.append(uuid)
        elif entity["entity_type"] == 'folder':
            items = self.doc_client.list_folder_content(uuid)["results"]
            for item in items:
                file_uuids.extend(self.download_data_using_uuid(item["uuid"], local_directory=os.path.join(local_directory, entity["name"])))
            return file_uuids
        else:
            raise Exception("Downloading of resources currently supported only for files and folders!")

        remote_paths = []
        local_paths = []
        for uuid in file_uuids:
            remote_paths.append(self._translate_UUID_to_URL(uuid))
        local_paths.extend(self.download_data(remote_paths=remote_paths, local_directory=local_directory))
        return local_paths

    def load_data(self, remote_path):
        content = self._download_data_content(remote_path)
        content_type = mimetypes.guess_type(remote_path)[0]
        if content_type == "application/json":
            return json.loads(content)
        else:
            return content


class HTTPDataStore(object):
    """
    A class for downloading data from the web.
    """

    def __init__(self, **kwargs):
        pass

    def upload_data(self, file_paths):
        raise NotImplementedError("The HTTPDataStore does not support uploading data.")

    def download_data(self, remote_paths, local_directory="."):
        if isinstance(remote_paths, str):
            remote_paths = [remote_paths]
        local_paths = []
        for url in remote_paths:
            req = requests.head(url)
            if req.status_code == 200:
                if url.startswith("https://senselab.med.yale.edu/modeldb/") and url.endswith("&mime=application/zip"):
                    filename = req.headers["Content-Disposition"].split("filename=")[1]
                else:
                    filename = url.split('/')[-1]
            local_path = os.path.join(local_directory, filename)
            #local_path = os.path.join(local_directory, os.path.basename(urlparse(url).path))
            Path(os.path.dirname(local_path)).mkdir(parents=True, exist_ok=True)
            filename, headers = urlretrieve(url, local_path)
            local_paths.append(filename)
        return local_paths

    def load_data(self, remote_path):
        content_type, encoding = mimetypes.guess_type(remote_path)
        if content_type == "application/json":
            return requests.get(remote_path).json()
        else:
            local_paths = self.download_data([remote_path])
            return local_paths[0]


class SwiftDataStore(object):
    """
    A class for downloading data from CSCS Swift storage.
    Note: data from public containers can also be downloaded via `HTTPDataStore`
    """
    def __init__(self, **kwargs):
        pass

    def upload_data(self, file_paths, username="", container="", project=None, remote_directory="", overwrite=False):
        try:
            from hbp_archive import Container
        except ImportError:
            print("Please install the following package: hbp_archive")
            return

        print("----------------------------------------------------")
        print("NOTE: The target location is inside a CSCS container")
        print("----------------------------------------------------")
        if not username:
            username = raw_input("Please enter your CSCS username: ")
        if not container:
            container = raw_input("Please enter target container name: ")
        container_obj = Container(container, username, project=project)
        remote_paths = container_obj.upload(file_paths, remote_directory=remote_directory, overwrite=overwrite)
        return remote_paths

    def get_container(self, remote_path, username=""):
        try:
            from hbp_archive import Container
        except ImportError:
            print("Please install the following package: hbp_archive")
            return

        name_parts = remote_path.split("swift://cscs.ch/")[1].split("/")
        if name_parts[0].startswith("bp00sp"):  # presuming all project names start like this
            prj_name = name_parts[0]
            ind = 1
        else:
            prj_name = None
            ind = 0
        cont_name = name_parts[ind]
        entity_path = "/".join(name_parts[ind+1:])
        pre_path = None
        if not "." in name_parts[-1]:
            dirname = name_parts[-1]
            pre_path = entity_path.replace(dirname, "", 1)

        print("----------------------------------------------------")
        print("NOTE: The target location is inside a CSCS container")
        print("----------------------------------------------------")
        if not username:
            username = raw_input("Please enter your CSCS username: ")
        container = Container(cont_name, username, project=prj_name)
        if prj_name:
            container.project._get_container_info()
        return container, entity_path, pre_path

    def download_data(self, remote_paths, local_directory=".", username=""):
        if isinstance(remote_paths, str):
            remote_paths = [remote_paths]
        local_paths = []
        for remote_path in remote_paths:
            container, entity_path, pre_path = self.get_container(remote_path, username=username)
            contents = container.list()
            contents_match = [x for x in contents if x.name.startswith(entity_path)]
            for item in contents_match:
                if pre_path:
                    localdir = os.path.join(local_directory, entity_path.replace(pre_path,"",1))
                else:
                    localdir = local_directory
                if not "directory" in item.content_type: # download files
                    outpath = container.download(item.name, local_directory=localdir, with_tree=False, overwrite=False)
                    if outpath:
                        local_paths.append(outpath)
        return local_paths

    def load_data(self, remote_path, username=""):
        container, entity_path, pre_path = self.get_container(remote_path, username=username)
        content = container.read(entity_path)
        content_type = mimetypes.guess_type(remote_path)[0]
        if content_type == "application/json":
            return json.loads(content)
        else:
            return content


URI_SCHEME_MAP = {
    "collab": CollabDataStore,
    "http": HTTPDataStore,
    "https": HTTPDataStore,
    "swift": SwiftDataStore
}
