#!/usr/bin/env bash

. ~/Scripts/libnotify
# Sync local repos 
readonly ROOT=~/Clones

#Repos
readonly repos="dirty dirStack checkUndocumenteds"

#Change dir to $root
cd $ROOT

main() {
    die() { notify-err "$1"; }

    update_repo() {
        #Check for local changes
        dirty() { git status --porcelain; }

        if [[ $(dirty) ]]; then 
            echo "Unsaved changes,doing commit so."
            git add .
            git commit -m "auto commit"
        fi

        local LOCAL=$(git rev-parse @)
        local REMOTE=$(git rev-parse @{u})
        local BASE=$(git merge-base @ @{u})

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


    for dir in $repos; do
        [[ ! -d $dir ]] && die "$dir not found" && continue
        echo "**********************************"
        echo "Doing $dir"
        cd $dir && update_repo
        cd $ROOT
        echo "************END********************"
    done

}

main
