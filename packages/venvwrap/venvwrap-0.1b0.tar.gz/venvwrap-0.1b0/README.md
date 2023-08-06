# venvwrap
A collection of bash functions for python venv mangement

## Install
via pip

```
pip install venvwrap
source bin/venvwrap.sh
```

via github

```
git clone https://github.com/hunkeydee/venvwrap
sha256sum -c venvwrap/sha256
source venvwrap/venvwrap.sh
```

## Asciicast Demos
- [basic create, pip-install, use, destroy](https://asciinema.org/a/326317)
- [create venvs from varied python versions](https://asciinema.org/a/326320)
- [link packages between venvs](https://asciinema.org/a/326319)

---

## Bash Environment and File System effects
- The script exports the following variables and default values.  Change them as needed before installation.

  - `VENV_HOME="${HOME}"/.venvs` -> Default folder for venv directories

  - `VENV_PY=$(which python3)` -> Default python installation

- If `$VENV_HOME` does not already exist on the file system, this script will create it.

- All venvwrap commands are bash functions, with a small reliance on common linux binaries such as `rm`, `ln`, `grep`, `cut`, `popd` and `pushd`

## Usage
**venvmk** - Create venv(s), installs pip, wheel, setuptools
```
usage: venvmk <venv>...

  ex: `venvmk alpha` -> creates a venv called 'alpha'
  ex: `venvmk bravo charlie` -> creates two seperate venvs
  ex: `venvmk delta -p /opt/bin/python3.6\` -> create venv using alt python
```
**venvrm** - Delete venv(s)
```
usage: venvrm <venv>...

  ex: `venrm delta` -> deletes the venv called 'delta'
  ex: `venrm echo foxtrot` deletes two venvs
```
**workon** - Enter/activate a venv
```
  usage: workon <venv>

  ex: `workon golf` -> activates the 'golf' venv context
```
**venvex** - Exit/deactivate the current venv
```
  usage: venvex

  ex: `venvex` -> deactivates the current venv
```
**venvls** - List all virtual environments managed by venvwrap
```
  usage: venvls
  
  ex `venvls` -> returns a dir listing of $VENV_HOME
```
**venvpy** - Run python command in venv
```
  usage: venvpy <venv> <python cmd>

  ex: `venvpy hotel --version` -> returns python version for venv 'hotel'
```
**venvpip** - Run a pip command in venv
```
  usage: venvpip <venv> <pip cmd>

  ex: `venvpip india show numpy` -> returns numpy details from venv 'india'
```
**venvpkgls** - List packages installed or linked in venv(s)
```
  usage: venvpkgls <venv>...

  ex: `venpkgls juliet` -> runs pip list for 'juliet', then displays link in the site-packages directory
```
**venvcmd** - Run cmd in venv
```
  usage: venvcmd <venv> <cmd>
  
  ex: `venvcmd kilo python3 ./server.py` -> runs server.py in 'kilo' venv
```
**venvinstall** - Install pip package(s) in venv
```
  usage: venvinstall <venv> <pkg>...'

  ex: `venvinstall mike urllib3` -> installs urllib3 in 'mike'
  ex: `venvinstall november numpy chardet` -> installs numpy and chardet
```
**venvlink** - link a package from  source venv> to target venv
```
  usage: venvlink <source_venv> <source_pkg> <target_venv>

  ex: venvlink oscar matplotlib papa` -> creates a link in 'papa' pointing to the matplotlib package in oscar
```

## Background
I didn't know enough about venvs (or bash functions), so I spent a weekend learning/making this project.  Its generally inspired by [`virtualenvwrapper`](https://pypi.org/project/virtualenvwrapper/).  Instead of wrapping virtualenv, these functions support the built-in python `venv`.  *I think you can use virtualenvwrapper to wrap venvs since they're almost equivilent, but just using someone elses code means I learn less.*

No effort was made to make these functions portable.  *It works for me* on Debian Buster x86_64.  I used `python3.7.3` from debian apt packages.  `python3.6.10`, `python3.7.7`, and `python3.8.3` were later compiled and successfully tested with venvwrap on the same system. `python2` has been completely ignored since it's EOL.   

Some dependencies include:

| python         | other cmds            |
|----------------|-----------------------|
| `python3`      | `bash`                |
| `python3-venv` | `rm` `ln` `cut` `grep`|
| `python3-pip`  | `pushd` `popd`        |
