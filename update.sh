#!/bin/bash

author="Marco Sgobino"
email="<marco.sgobino@gmail.com>"
old_version=28.0.6
new_version=28.0.7
old_release=1
new_release=1

today=$(LANG=C date "+%a %b %d %T %Z %Y")
content="- Version ${new_version}"
#content+="\n"
#content+="- Removed clean section"
#content+="\n"
#content+="- Removed period in Summary"

entry="* ${today} ${author} ${email} - v${new_version}-${new_release}"
entry+="\n"
entry+="${content}"

find . -type f -name '*.spec' -exec sed -i          \
    -e "/Version:/s/${old_version}/${new_version}/" \
    -e "/Release:/s/${old_release}/${new_release}/" \
    {} \;
    #-e "/%changelog/a ${entry}" {} \;
