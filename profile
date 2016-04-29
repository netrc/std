
# interactive stuff

export PS1="\\$ "

# uppercase for "cf" cloudfoundry
# export HTTP_PROXY=proxy.zz.com:8080 
# lower case for curl
#e xport http_proxy=proxy.zz.com:8080 
# export HTTPS_PROXY=proxy.zz.com:8080 
# also npm config set proxy, set https-proxy

# Modules !
export MODULEPATH=$MODULEPATH:${HOME}/.modules
module load ricampbe

#export PATH=~/bin:$PATH

[[ -s ~/.bashrc ]] && . ~/.bashrc

unalias ls
