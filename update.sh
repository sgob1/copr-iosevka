#!/bin/bash

author="Marco Sgobino"
email="<marco.sgobino@gmail.com>"
old_version=27.3.3
new_version=27.3.4
old_release=4
new_release=1

today=$(LANG=C date "+%a %b %d %T %Z %Y")
content="- Version ${new_version}"

entry="* ${today} ${author} ${email} - v${new_version}-${new_release}"
entry+="\n"
entry+="${content}"

find . -type f -name '*.spec' -exec sed -i          \
    -e "/Version:/s/${old_version}/${new_version}/" \
    -e "/Release:/s/${old_release}/${new_release}/" \
    -e "/%changelog/a ${entry}" {} \;
