#!/usr/bin/env bash

. ~/Scripts/libnotify
# Sync local repos 
readonly ROOT=~/Clones

#Repos
readonly mines="dirty dirStack checkUndocumented generate-autocompletion pomodoroTasks rmalias"

#Change dir to $root
cd $ROOT

main() {
    repo_failed() { notify_err "$1"; }

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
            git push || repo_failed $1
        else
            echo "Diverged notify user"
        fi
    }


    for dir in $mines; do
        echo "**********************************"
        echo "Doing $dir"
        [[ ! -d $dir ]] && repo_failed "$dir not found" && continue
        cd $dir && update_repo $dir
        cd $ROOT
    done

}

main
