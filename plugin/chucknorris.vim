" directory to store quotes
" This dir must be writable to the current user
let chucknorris#inspiration_storage_dir = "$HOME/.vim-chucknorris"

python << EOP
import vim
import sys
from os import path

def fix_syspath():
    current_file = vim.eval('expand("<sfile>")')
    current_path = path.join(path.split(current_file)[:-1])[0]
    if current_path not in sys.path:
        sys.path.insert(0, current_path)

fix_syspath()

from chucknorris.chucknorris import shuffle

EOP


function! RoundHouse()
    python shuffle()
endfunction

nnoremap <Leader>z :call RoundHouse()<CR>
