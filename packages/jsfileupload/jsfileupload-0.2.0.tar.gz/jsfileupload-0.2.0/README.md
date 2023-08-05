
# jsfileupload

FileUpload Widget using the Jupyter Notebook Server API.

The widget is able to upload large files by uploading them in chunks.
The files will only be uploaded into the file system, not into the notebook itself.
That means that file contents will not be directly available over the widget,
but will have to be read into the notebook separately.


## Installation

You can install using `pip`:

```
pip install jsfileupload
```
or from this GitLab directly
```
pip install git+https://gitlab.version.fz-juelich.de/jupyter4jsc/j4j_extras/jsfileupload.git
```

Or if you use jupyterlab:

```
pip install jsfileupload
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```
jupyter nbextension enable --py [--sys-prefix|--user|--system] jsfileupload
```
