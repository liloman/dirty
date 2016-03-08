#!/usr/bin/env bash

main() {
    #function_body
    #Check if local changes
    dirty() { git status --porcelain; }

    if [[ $(dirty) ]]; then 
        echo "unsaved changes"
        git add .
        git commit -m "auto commit"
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
        git pull --rebase
    elif [[ $REMOTE = $BASE ]]; then
        echo "Need to push"
        git push
    else
        echo "Diverged notify user"
    fi

}

main

