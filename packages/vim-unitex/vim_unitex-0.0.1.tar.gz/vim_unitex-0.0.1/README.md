# README #

### Purpose ###

Latex to Unicode conversion intended for use in Vim

### Set up ###

Depending on your Python3 installation, one of these should work
assuming that the directory where Pip installs executable files
(e.g. in Linux: `$HOME/.local/bin`) is in your `$PATH`

```
pip3 install --user vim_unitex
pip install vim_unitex
```

Add this (or something similar to suit your taste) to your .vimrc:

```vimscript
function Unitex()
    let s = input("Latex: ")
    return system('tex2unicode "' . s . '"')
endfunction

inoremap <leader>t <C-R>=Unitex()<C-M>
```
