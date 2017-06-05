
set expandtab
set tabstop=4
set shiftwidth=4

" https://vimcolorschemetest.googlecode.com/svn/colors/ashen.vim
" guifg=ctermfg gui=cterm guibg=ctermbg

"hi clear
syntax off

autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

hi MatchParen cterm=none ctermbg=none ctermfg=none
