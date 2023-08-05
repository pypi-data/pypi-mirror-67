dicom-upload
===============================

Upload DICOM files with patient und study data removed from header

Installation
------------

To install use pip:

    $ pip install dicom_upload
    $ jupyter nbextension enable --py --sys-prefix dicom_upload

Alternatively, install directly from GitLab:

    $ pip install git+https://gitlab.version.fz-juelich.de/jupyter4jsc/j4j_extras/dicom-upload.git

To install for jupyterlab

    $ jupyter labextension install dicom_upload

For a development installation (requires npm),

    $ git clone https://gitlab.version.fz-juelich.de/jupyter4jsc/j4j_extras/dicom-upload.git
    $ cd dicom-upload
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix dicom_upload
    $ jupyter nbextension enable --py --sys-prefix dicom_upload
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This take a minute or so to get started, but then allows you to hot-reload your javascript extension.
To see a change, save your javascript, watch the terminal for an update.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

