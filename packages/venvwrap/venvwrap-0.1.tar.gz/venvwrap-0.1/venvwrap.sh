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

_G=$(tput setaf 2)   #green, good
_R=$(tput setaf 1)   #red, bad
_C=$(tput setaf 6)   #cyan, note
_M=$(tput setaf 240) #meh, dark grey
_D=$(tput sgr0)      #default, reset

function venvmk {
    local help="  Create venv(s), installs pip, wheel, setuptools

  usage: venvmk [-p|--python PATH] <venv>...

  ex: \`venvmk alpha\` -> creates a venv called 'alpha'
  ex: \`venvmk bravo charlie\` -> creates two seperate venvs
  ex: \`venvmk delta -p /opt/bin/python3.6\` ->  create venv using alternate python"
    if ! _help "$1"; then
        # parse $@
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
                venvs+=("$1")
                shift
                ;;
            esac
        done
        
        if [[ -z "$python" ]]; then
            local python="$VENV_PY"
        fi
        
        # create venvs, install pip        
        local venv
        for venv in "${venvs[@]}"; do
            if ! _is_venv "$venv"; then
                local note="creating venv..."
                local succ="created venv: '$venv'"
                local fail="'$venv' venv creation failed"
                if doc_exec "$python" -m venv "$VENV_HOME"/"$venv"; then
                    workon "$venv"
                    if [[ -n "$VIRTUAL_ENV" ]]; then
                        #local venvpip=$"${VENV_HOME}/${venv}/bin/pip"
                        note="setting up pip, wheel, setuptools..."
                        succ="installed pip in '$venv'"
                        fail="pip install encountered an error in $venv"
                        doc_exec pip install --upgrade pip wheel setuptools -q
                        venvex
                    else
                        _warn "\`workon $venv\` failed."
                    fi
                fi
            else
                _note "'$venv' already exists. Doing nothing."
            fi
        done
        return 0
    fi
    return 1
}

function venvrm {
    local help="  Delete venv(s)

  usage: venvrm <venv>...

  ex: \`venvrm delta\` -> deletes the venv called 'delta'
  ex: \`venvrm echo foxtrot\` deletes two venvs"
    if ! _help "$1"; then
        if [[ -n "$VIRTUAL_ENV" ]]; then
            venvex
        fi
        _note "deleting venv(s)"
        local venv
        for venv in "$@"; do
            if _is_venv "$venv"; then
                local succ="deleted venv: '$venv'"
                local fail="unable to delete '$venv'"
                doc_exec rm -r "${VENV_HOME:?}"/"${venv:?}"
            else
                _note "'$venv' is not a venv, ignoring"
            fi
        done
        return 0
    fi
    return 1
}

function workon {
    local help="  Enter/activate a venv

  usage: workon <venv>

  ex: \`workon golf\` -> activates the 'golf' venv context"
    if ! _help "$1"; then
        if _is_venv "$1"; then
            if [[ -n "$VIRTUAL_ENV" ]]; then
                venvex || return 1
            fi
            local succ="activated '$1'"
            local fail="unable to activate '$1'"
            doc_exec source "${VENV_HOME}"/"$1"/bin/activate &&
            pushd "${VENV_HOME}"/"$1" 1>/dev/null || return 1
            VENV="$1"
            return 0
        else
            _note "'$1' is not a venv in '$VENV_HOME'\n"
            _help
        fi
    fi
    return 1
}

function venvex {
    local help="  Exit/deactivate the current venv

  usage: venvex

  ex: \`venvex\` -> deactivates the current venv"
    if ! _help "$1"; then
        if [[ -n "$VIRTUAL_ENV" ]]; then
            local succ="exited '${VIRTUAL_ENV##*/}'"
            local fail="unable to deactivate '${VIRTUAL_ENV##*/}'"
            doc_exec deactivate &&
            popd 1>/dev/null || return 1
            unset VENV
            return 0
        else
            _note "     unnecessary venvex; no venv activated\n"
        fi
    fi
    return 1
}

function venvls {
    local help="  List all virtual environments managed by venvwrap

  usage: venvls
  
  ex \`venvls\` -> returns a dir listing of \$VENV_HOME"
    if ! _help "$1"; then   
        if ls "$VENV_HOME"; then
            return 0
        else
            _warn "Something is broken with \$VENV_HOME. I can't find that dir"
        fi
    fi
    return 1
}

function _lspkgln {
    # get site-packages dir via pip
    local pkgdir
    if _get_pkg_dir "$1" pip; then
        
        # parse through files, retain link files only
        local links=()
        local file
        for file in "$pkgdir"/*; do
            if [[ -L "$file" ]]; then
                links+=("$file")
        fi
        done
        
        # display link files
        if [[ "${#links[@]}" -gt 0 ]]; then
            printf '%s\n' "$pkgdir"
            printf '%.0s-' {1..79}
            printf '\n'
            local link
            for link in "${links[@]}"; do
                pushd "$pkgdir" 1>/dev/null || return 1
                ls -l "${link##*/}"
                local rslt="$?"
                popd 1>/dev/null || return  1
            done
            return "$rslt"
        else
            _note "I did not find any links"
            return 0
        fi
    fi
    return 1
}

function venvpkgls {
    local help="  List packages installed or linked in <venv>

  usage: venvpkgls <venv>...

  ex: \`venvpkgls juliet\` -> runs pip list for 'juliet', then displays links in the site-packages directory"
    if ! _help "$1"; then
        if _is_venv "$1"; then
            local venv=$1
            # display pip installed packages
            if workon "$venv"; then
                # local venvpip=$"${VENV_HOME}/$venv/bin/pip"
                local note="getting pip packages"
                local succ="got packages from '$venv'"
                local fail="pip failed to list packages"
                if doc_exec pip list -v -q; then
                    # display link files in site-packages
                    local note="examining site-packages for possible links in '$venv'"
                    local succ="examined site-packages"
                    local fail="unable to examine site-packages"
                    doc_exec _lspkgln "$venv"
                    local rslt="$?"
                fi
                venvex
                return "$rslt"
            else
                _warn "\`workon $venv\` failed."
            fi
        else
            _help
        fi
    fi
    return 1
}

function venvcmd {
    local help="  Run <cmd> in <venv>

  usage: venvcmd <venv> <cmd>

  ex: \`venvcmd kilo python3 ./server.py\` -> runs server.py in 'kilo' venv" 
    if ! _help "$1"; then
        if _is_venv "$1"; then
            workon "$1"
            if [[ -n "$VIRTUAL_ENV" ]]; then
                shift
                _doc "$@"
                "$@"
                local rslt="$?"
                venvex
                return "$rslt"
            fi
        else
            _help
        fi
    fi
    return 1
}

function venvinstall {
    local help="  Install pip package(s) in <venv>

  usage: venvinstall <venv> <pkg>...'

  ex: \`venvinstall mike urllib3\` -> installs urllib3 in 'mike'
  ex: \`venvinstall november numpy chardet\` -> installs numpy and chardet"
    if ! _help "$1"; then
        if _is_venv "$1"; then
            local venv="$1"
            #local venvpip=$"${VENV_HOME}/$venv/bin/pip"
            shift
            venvcmd "$venv" pip install "$@"
            return "$?"
        else
            _help
        fi
    fi
    return 1
}

function venvlink {
    local help="  Link a package from <source_venv> to <target_venv>

  usage: venvlink <source_venv> <source_pkg> <target_venv>

  ex: \`venvlink oscar matplotlib papa\` -> creates a link in 'papa' pointing to the matplotlib package in oscar"
    if ! _help "$1"; then
        if _is_venv "$1" && _is_venv "$3"; then
            local pkgdir srcdir tgtdir
            _get_pkg_dir "$1" "$2" 
            srcdir="$pkgdir"
            if [[ -n "$srcdir" ]]; then
                _get_pkg_dir "$3" "pip"
                tgtdir="$pkgdir"
                if [[ -n "$tgtdir" ]]; then
                    local note="linking package..."
                    local succ="linked '$2' from '$1' to '$3'"
                    local fail="failed to link '$2' from '$1' to '$3'"
                    doc_exec ln -s "$srcdir"/"$2" "$tgtdir"/"$2"
                    return "$?"
                else
                    _note "'pip' not found in '$3', aborting\n"
                fi
            else
                _note "Package '$2' not found in '$1'.  Doing nothing\n"
            fi
        else
            _help
        fi
    fi
    return 1
}

function _is_venv {
    if [[ -d "$VENV_HOME"/"$1" ]] && [[ -n "$1" ]]; then
        return 0
    else
    _note "venv not found: '$1'"
    return 1
    fi
}

function _help {
    if [[ "$1" =~ "--help" ]] || [[ $# -eq 0 ]]; then
        printf "%s\n" "$help"
        return 0
    fi
    return 1
}

function _get_pkg_dir {
    local venvpip loc
    venvpip="${VENV_HOME}/$1/bin/pip"
    loc="$("$venvpip" show "$2")"     # run pip command to get dir
    loc="${loc##$'*\nLocation: '}"    # drop all before '\nLocation: '
    pkgdir="${loc%%$'\n*'*}"  # drop all after  '\n'
    if [[ -n "$pkgdir" ]]; then
        return 0
    fi
    return 1
}

function _doc {
    if [[ -n $note ]]; then
        _note "$note"
        unset note
    fi
    printf "     %b" "$_M"
    if [[ -n ${VENV} ]]; then
        printf "%s " "($VENV)"
    fi
    printf '`'
    printf "%s " "$@"
    printf "\b"
    printf "\`%b" "$_D"
    printf '\n'
}

function doc_exec {
    _doc "$@"
    _exec "$@"
    return "$?"
}

function _exec {
    if "$@"; then
        #printf " [${_G}+${_D}] ${_G}${succ}${_D}\n"
        printf ' ['
        printf '%b+' "$_G"
        printf '%b] ' "$_D"
        printf '%b' "$_G"
        printf '%s' "$succ"
        printf '%b\n' "$_D"
        return 0
    else
       #printf " [${_R}-${_D}] ${_R}${fail}${_D}\n" >&2
        printf ' ['
        printf '%b+' "$_R"
        printf '%b] ' "$_D"
        printf '%b' "$_R"
        printf '%s' "$fail"
        printf '%b\n' "$_D"
    fi
    return 1
}

function _note {
    #printf "${_C}     $@${_D}\n"
    printf '%b     ' "$_C"
    printf '%s' "$*"
    printf '%b\n' "$_D"
}

function _warn {
    # ( printf "${_R}     $@${_D}\n" >&2 )
    printf '%b     ' "$_R" >&2
    printf '%s' "$*" >&2
    printf "%b\n" "$_D" >&2
}
