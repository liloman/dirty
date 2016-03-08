#!/usr/bin/env bash
# Sync local repos 
readonly ROOT=~/Clones

#Repos
readonly repos="dirty "

#Change dir to $root
cd $ROOT

update_repo() {
    #Check for local changes
    dirty() { git status --porcelain; }

    if [[ $(dirty) ]]; then 
        echo "unsaved changes"
        git add .
        git commit -m "auto commit"
    else
        echo "clean"
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
    echo "Doing $dir"
    cd $dir && update_repo
    cd $ROOT
done

