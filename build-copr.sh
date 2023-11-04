#!/bin/bash

CLONE_URL=https://git.sr.ht/~sgob/copr-iosevka
COMMITTISH=main
TIMEOUT=43200
COPR_REPO=sgob/iosevka

# all iosevka variants
FONTS=(
    iosevka
    iosevka-slab
    iosevka-curly
    iosevka-curly-slab
    iosevka-ss01
    iosevka-ss02
    iosevka-ss03
    iosevka-ss04
    iosevka-ss05
    iosevka-ss06
    iosevka-ss07
    iosevka-ss08
    iosevka-ss09
    iosevka-ss10
    iosevka-ss11
    iosevka-ss12
    iosevka-ss13
    iosevka-ss14
    iosevka-ss15
    iosevka-ss16
    iosevka-ss17
    iosevka-ss18
    iosevka-aile
    iosevka-etoile
)

for f in ${FONTS[@]}; do
    FONT_NAME=${f}
    FONT_SUBDIR=${f}-fonts
    FONT_SPEC=${FONT_NAME}-fonts.spec

    copr-cli buildscm               \
             --clone-url $CLONE_URL \
             --commit $COMMITTISH   \
             --subdir $FONT_SUBDIR  \
             --spec $FONT_SPEC      \
             --timeout $TIMEOUT     \
             --background           \
             --nowait               \
             $COPR_REPO
done
