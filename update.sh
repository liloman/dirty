#!/usr/bin/env bash
# Sync local repos 
readonly ROOT=~/Clones

#Repos
readonly repos="dirty dirStack checkUndocumented"

#Change dir to $root
cd $ROOT

main() {
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
        [[ ! -e $dir ]] && die "$dir not found"
        echo "**********************************"
        echo "Doing $dir"
        cd $dir && update_repo
        cd $ROOT
    done

}

main
