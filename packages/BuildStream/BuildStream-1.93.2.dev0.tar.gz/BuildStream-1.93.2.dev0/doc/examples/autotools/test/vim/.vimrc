""" Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'michalbachowski/vim-wombat256mod'
Plugin 'altercation/vim-colors-solarized'

Plugin 'scrooloose/nerdtree'
Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/syntastic'
Plugin 'tomtom/tcomment_vim'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-surround'
Plugin 'kien/ctrlp.vim'
Plugin 'Townk/vim-autoclose'
Plugin 'python/black'

call vundle#end()
filetype plugin indent on

""" Powerline
set laststatus=2
python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup

""" Basic options
syntax enable
set background=dark
colorscheme solarized
" colorscheme wombat256mod

set autoindent
set backspace=indent,eol,start
set confirm
set foldmethod=indent
set nu
set wildmenu
set wildmode=longest,list

""" Search
set incsearch
set ignorecase
set smartcase
set hlsearch

""" Tabs
set expandtab
autocmd FileType make setlocal noexpandtab

""" Indents
set shiftwidth=4
set tabstop=4
autocmd FileType yaml   set tabstop=2 | set shiftwidth=2

""" Restore cursor to position in last editing session
au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal g'\"" | endif

""" Whitespaces
highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/

"""" Syntastic
let g:syntastic_python_checkers = ['mypy', 'flake8', 'pylint']

""" Fix pumvisible random text
let g:AutoClosePreserveDotReg = 0

""" YouCompleteMe!
let g:ycm_python_interpreter_path = ''
let g:ycm_python_sys_path = []
let g:ycm_extra_conf_vim_data = [
  \  'g:ycm_python_interpreter_path',
  \  'g:ycm_python_sys_path'
  \]
let g:ycm_global_ycm_extra_conf = '~/.vim/global_extra_conf.py'

""" Miscellaneous
set spell
nnoremap <space><space> :nohl<CR>
nnoremap <space> za
