# Some reminders of semantics - http://linux.die.net/man/1/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROG=$(basename ${0})

echo $*
echo "$*"      # a single argument with all the args
echo $@
echo "$@"       # all the args singly

echo $MACHTYPE
echo $RANDOM
echo $SECONDS       # seconds since running of this shell

# Arithmetic expansion
a=$((3 + 4)) ; echo $a
b=$((a++ * 3)) ; echo $b    # 21,  a is now 8
# ~ bitwise negation, <<,>> bitwise shift, & ^ |  bitwise and, xor, or

z=${varName:-10}    # use 10 if unset
                    # ! no spaces before/after "=" (otherwise looks like a cmd)
echo ${varName:=10}      # use 10 if unset *and* set varName

echo ${#var}     # length of $var value

v[2]=foo      # indexed array
w[bar]=baz    # associative array
echo arrays ${v[2]}  ${w[bar]}     # got to use braces
v[3]=goo
echo "${v[*]}"      # one word
echo "${v[@]}"      # separate words
echo ${!v[@]}       # the keys

v=$(date)       # command substitution

echo $#         # num of params

# Brace Expansion - generate arbitrary strings....
echo a{1,2,3}b      # a1b a2b a3b
echo 1.{1..9}      # 1.1 1.2 1.3...
echo {A..Z}{0..9}   # A0 A1... B0 B1... ..Z9

# Conditional expressions
[[ -a filenameExists ]]
[[ -f regularFile ]]
[[ -d directiryExists ]]
[[ -s fileIsBiggerThanZero ]] 
[[ -z isThisStringZeroLength ]] && echo zero length string
[[ ! string1 = string2 ]]  && echo yes
[[ 2 -eq 2 ]]  && echo yes	# -eq -ne -gt -lt


function aFunc() {
    echo $@     # args are avail automatically
    date
    printf "%6.3f\n" 2    # std printf
}
aFunc some args
declare -f      # list/show functions

# interactive shells read from
# /etc/profile, ~/.bash_profile, ~/.bash_login, ~/.profile
# (when exiting, then reads from ~/.bash_logout, /etc/bash/bash.bash_logout)

# non-interactive
# file $BASH_ENV, 
