#!/usr/bin/env bash

#Check if local changes
dirty() { git status --porcelain; }

if [[ $(dirty) ]]; then 
    echo "dirty baby"
    # git add .
    # git commit -m "auto commit"
else
    echo "clean"
fi

LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})
BASE=$(git merge-base @ @{u})

if [[ $LOCAL = $REMOTE ]]; then
    echo "Up-to-date"
elif [[ $LOCAL = $BASE ]]; then
    echo "Need to pull"
elif [[ $REMOTE = $BASE ]]; then
    echo "Need to push"
else
    echo "Diverged notify user"
fi



