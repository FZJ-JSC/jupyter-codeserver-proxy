![build](https://github.com/FZJ-JSC/jupyter-codeserver-proxy/workflows/build/badge.svg)

# jupyter-codeserver-proxy
Integrate [code-server](https://github.com/coder/code-server) in your Jupyter environment for an fast, feature-rich and easy to use remote desktop in the browser.

## Requirements
- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab >= 3.x
- jupyter-server-proxy >= 3.1.0

This package executes the `code-server` command. This command assumes the `code-server` command is available in the environment's $PATH.

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
