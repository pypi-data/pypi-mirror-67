#!/bin/bash
if [[ -z "$VENV_HOME" ]]; then
    export VENV_HOME="${HOME}/.venvs"
fi
if [[ ! -d "$VENV_HOME" ]]; then
    mkdir "$VENV_HOME"
fi
if [[ -z "$VENV_PY" ]]; then
    export VENV_PY
    VENV_PY="$(which python3)"
fi

function venvmk {
    local help="  Create venv(s), installs pip, wheel, setuptools

  usage: venvmk [-p|--python PATH] <venv>...

  ex: \`venvmk alpha\` -> creates a venv called 'alpha'
  ex: \`venvmk bravo charlie\` -> creates two seperate venvs
  ex: \`venvmk delta -p /opt/bin/python3.6\` ->  create venv using alternate python"
    if ! _help "$@"; then
        local venvs=()
        while [[ $# -gt 0 ]]; do
            local key="$1"
            case $key in
              -p|--python)
                local python=$2
                shift
                shift
                ;;
              *)
                local venvs+=("$1")
                shift
                ;;
            esac
        done
    
        if [[ -z "$python" ]]; then
            local python="$VENV_PY"
        fi
    
        for venv in "${venvs[@]}"; do
        if ! _is_venv "$venv"; then
                local succ=" [+] created venv: '$venv'"
        local fail=" [-] '$venv' venv creation failed"
                "$python" -m venv "$VENV_HOME"/"$venv" &&
        echo "$succ" || echo "$fail"
              
              local succ=" [+] installed pip in $venv"
            local fail=" [-] pip install encountered an error in $venv"
            venvpip "$venv" install --upgrade pip wheel setuptools &&
            echo "$succ" || echo "$fail"
        else
            echo " [-] '$venv' already exists. Doing nothing." 
        fi
            if [[ "${#venvs[@]}" -eq 1 ]]; then
                venvex
            fi
        done
    fi
}

function venvrm {
    local help="  Delete venv(s)

  usage: venvrm <venv>...

  ex: \`venrm delta\` -> deletes the venv called 'delta'
  ex: \`venrm echo foxtrot\` deletes two venvs"
    if ! _help "$@"; then
        if [[ -n "$VIRTUAL_ENV" ]]; then
            venvex
        fi
        for venv in "$@"; do
            if _is_venv "$venv"; then
                  local succ=" [+] deleting venv: '$venv'"
          local fail=" [-] unable to delete '$venv'"
                rm -r "${VENV_HOME:?}"/"${venv:?}" &&
          echo "$succ" || echo "$fail"
            fi
        done
    fi
}

function workon {
    local help="  Enter/activate a venv

  usage: workon <venv>

  ex: \`workon golf\` -> activates the 'golf' venv context"
    if ! _help "$@"; then
        if _is_venv "$1"; then
	    if [[ -n "$VIRTUAL_ENV" ]]; then
                popd 1>/dev/null || return
	    fi
            local succ=" [+] activated '$1'"
            local fail=" [-] unable to activate '$1'"
            source "${VENV_HOME}"/"$1"/bin/activate &&
            echo "$succ" || echo "$fail"
            pushd "${VENV_HOME}"/"$1" 1>/dev/null || return
        else
            echo "     Maybe try one of these:"
            venvls
        fi
    fi
}

function venvex {
    local help="  Exit/deactivate the current venv

  usage: venvex

  ex: \`venvex\` -> deactivates the current venv"
    if ! _help "$@"; then
        if [[ -n "$VIRTUAL_ENV" ]]; then
            local succ=" [+] exiting '${VIRTUAL_ENV##*/}'"
        local fail=" [-] unable to deactivate '${VIRTUAL_ENV##*/}'"
        deactivate && echo "$succ" || echo "$fail"
            popd 1>/dev/null || return
        fi
    fi
}

function venvls {
    local help="  List all virtual environments managed by venvwrap

  usage: venvls
  
  ex \`venvls\` -> returns a dir listing of \$VENV_HOME"
    if ! _help "$@"; then   
        ls "$VENV_HOME"
    fi
}

function venvpy {
    local help="  Run python command in <venv>

  usage: venvpy <venv> <python cmd>

  ex: \`venvpy hotel --version\` -> returns python version for venv 'hotel'"
    if ! _help "$@"; then
    venv="$1"
    shift
    venvcmd "$venv" python "$@"
    fi
}

function venvpip {
    local help="  Run a pip command in <venv>

  usage: venvpip <venv> <pip cmd>

  ex: \`venvpip india show numpy\` -> returns numpy details from venv 'india'"
    if ! _help "$@"; then
    venv="$1"
    shift
        venvcmd "$venv" pip "$@"
    fi
}

function venvpkgls {
    local help="  List packages installed or linked in <venv>

  usage: venvpkgls <venv>...

  ex: \`venpkgls juliet\` -> runs pip list for 'juliet', then displays links in the site-packages directory"
    if ! _help "$@"; then
    venv="$1"
        echo " [ ] '$venv' pip reports these packages"
        local fail=" [-] pip failed to list packages"
        venvpip "$venv" list -v -q || echo "$fail"
    local pkgdir
        pkgdir="$(_get_pkg_dir "$venv" pip)"        
        local links=()
        for file in "$pkgdir"/*; do
            if [[ -L "$file" ]]; then
                links+=("$file")
        fi
        done
        if [[ "${#links[@]}" -gt 0 ]]; then
            echo " [+] I also found these linked pkgs from other venv(s)"
            for l in "${links[@]}"; do
                echo "    $l"
            done
        else
            echo " [ ] I did not find any linked packages"
        fi
    fi
}

function venvcmd {
    local help="  Run <cmd> in <venv>

  usage: venvcmd <venv> <cmd>
  
  ex: \`venvcmd kilo python3 ./server.py\` -> runs server.py in 'kilo' venv" 
    if ! _help "$@"; then
        workon "$1"
    shift
    "$@"
    venvex
    fi
}

function venvinstall {
    local help="  Install pip package(s) in <venv>

  usage: venvinstall <venv> <pkg>...'

  ex: \`venvinstall mike urllib3\` -> installs urllib3 in 'mike'
  ex: \`venvinstall november numpy chardet\` -> installs numpy and chardet"
    if ! _help "$@"; then
        if _is_venv "$1"; then
            venv="$1"
            shift
            venvpip "$venv" install "$@"
    fi
    fi
}

function venvlink {
    local help="  Link a package from <source_venv> to <target_venv>

  usage: venvlink <source_venv> <source_pkg> <target_venv>

  ex: venvlink oscar matplotlib papa\` -> creates a link in 'papa' pointing to the matplotlib package in oscar"
    if ! _help "$@"; then
        if _is_venv "$1" && _is_venv "$3"; then
             local srcdir
         srcdir=$(_get_pkg_dir "$1" "$2")
         if [[ -n "$srcdir" ]]; then
                 local tgtdir
         tgtdir=$(_get_pkg_dir "$3" "pip")
             if [[ -n "$tgtdir" ]]; then
                     local succ=" [+] linked '$2' from '$1' to '$3'"
             local fail=" [-] ln failed to link pkgs"
                     ln -s "$srcdir"/"$2" "$tgtdir"/"$2" && 
                 echo "$succ" || echo "$fail"
                 fi
             else
             echo " [-] Package '$2' not found in '$1'.  Doing nothing"
         fi
        fi
    fi
}


function _is_venv {
    if [[ -d "$VENV_HOME"/"${1:?}" ]]; then
        return 0
    else
    echo " [ ] venv not found: '$1'"
    return 1
    fi
}

function _get_pkg_dir {
    venvpip "$1" show "$2" | grep 'Location: ' | cut -d' ' -f2-
}

function _help {
    for arg in "$@"; do
        if [[ "$arg" =~ "--help" ]]; then
            echo -e "$help\n"
            return 0
        fi
    done
    return 1
}
