
# things set in preinstalled .bashrc /etc/profile /etc/bash.bashrc
unalias ls
unset command_not_found_handle    # from /etc/bash.bashrc

# my favorites
set -o vi
export PS1="$ "
export EDITOR=vi
cd ${HOME}

# apt-get install environment modules locally (includes tclsh)
[ -d /usr/share/modules/init ] && {
  source /usr/share/modules/init/bash
  module use /rc/richard/lib/modules   # prepends
  module load Richard   # /rc/bin : /rc/richard/bin
}
