#!/bin/bash

author="Marco Sgobino"
email="<marco.sgobino@gmail.com>"
old_version=27.3.3
new_version=27.3.3
old_release=3
new_release=4

today=$(LANG=C date "+%a %b %d %T %Z %Y")
content="- Fixed formatting of descriptions"
content+="\n"
content+="- Introduced new changelog format"

entry="* ${today} ${author} ${email} - v${new_version}-${new_release}"
entry+="\n"
entry+="${content}"

find . -type f -name '*.spec' -exec sed -i          \
    -e "/Version:/s/${old_version}/${new_version}/" \
    -e "/Release:/s/${old_release}/${new_release}/" \
    -e "/%changelog/a ${entry}" {} \;
