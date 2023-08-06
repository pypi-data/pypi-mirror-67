# PATH
PATH="$HOME/Library/Python/3.7/bin:$PATH"
PATH="$HOME/git/buildstream/buildstream/contrib:$PATH"
export PATH

# Powerline
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. "$HOME"/Library/Python/3.7/lib/python/site-packages/powerline/bindings/bash/powerline.sh

# Git
. ~/.git-completions.bash

# Aliases
alias git='hub'
alias grep='grep --color=auto'
alias ls='ls -G'
alias ll='ls -l'
alias la='ls -a'

# Venv management
function activate() {
    venv_dir="$HOME"/.venvs/"$1"
    if [[ ! -d "$venv_dir" ]]; then
        mkdir -p "$venv_dir"
        python3 -m venv "$venv_dir"
    fi
    . "$venv_dir"/bin/activate
}
