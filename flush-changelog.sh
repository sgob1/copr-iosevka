#!/usr/bin/bash
set -e

read -rp "This will flush ALL changelogs in this project's .spec files. Are you REALLY sure? (y/N): " answer

if [ "$answer" = "y" ]; then
	find . -name "*.spec" -exec sed -i '/\%changelog/q' {} \;
else
	echo "Nothing done."
fi
