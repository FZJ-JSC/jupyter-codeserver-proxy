![build](https://github.com/FZJ-JSC/jupyter-codeserver-proxy/workflows/build/badge.svg)

# jupyter-codeserver-proxy
Integrate [code-server](https://github.com/coder/code-server) in your Jupyter environment for an fast, feature-rich and easy to use remote desktop in the browser.

![Jupyter-codeserver-proxy example](docs/screenshot.png 'Jupyter-codeserver-proxy example')

**ATTENTION:**  
`code-server` has no official support for passing the password/token via url-parameters. Sad thing, a pull request was not merged [[more]](https://github.com/coder/code-server/pull/2428).
Hence, we need to disable authentication at the moment completly with `--auth=none` [[more]](https://github.com/FZJ-JSC/jupyter-codeserver-proxy/blob/main/jupyter_codeserver_proxy/__init__.py#L93).
This allows any user who can access localhost:port of the machine running the `code-server` to use it - even if he is not authorized to do so. 
An alternative solution to close this security hole might be to use unix sockets instead of ports. As soon as this is fully supported by `jupyter-server-proxy` we will switch [[more]](https://github.com/jupyterhub/jupyter-server-proxy/pull/337).

## Requirements
- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab >= 3.x
- jupyter-server-proxy >= 3.1.0

This package executes the `code-server` command.  
It tries to find the `code-server` executable checking the following:  
- 1. environment variable $CODESERVER_BIN
- 2. `<dir-of-__init__.py>/bin/code-server`
- 3. `which code-server` (searching standard $PATH)
- 4. special locations:
     - `/opt/codeserver/bin/code-server`

## Install 

#### Create and Activate Environment
```
virtualenv -p python3 venv
source venv/bin/activate
```

#### Install jupyter-codeserver-proxy
```
pip install git+https://github.com/FZJ-JSC/jupyter-codeserver-proxy.git
```

#### Enable jupyter-codeserver-proxy extensions
For Jupyter Classic, activate the jupyter-server-proxy extension:
```
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

For Jupyter Lab, install the @jupyterlab/server-proxy extension:
```
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

#### Start Jupyter Classic or Jupyter Lab
Click on the code-server icon from the Jupyter Lab Launcher or the code-server item from the New dropdown in Jupyter Classic.  
Connect to your database as instructed in the Quickstart section.

## Configuration
This package calls `code-server` with a bunch of settings.  
You have to modify `setup_codeserver()` in `jupyter_codeserver_proxy/__init__.py` for change.

## Credits
- [code-server](https://github.com/coder/code-server) 
- jupyter-server-proxy

## License
BSD 3-Clause
