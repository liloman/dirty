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
            git commit -m "auto commit" || repo_failed $1
        fi

        #update refs for remote
        git remote -v update || { repo_failed " update for remote on repo $1"; return; }
        local LOCAL=$(git rev-parse @)
        local REMOTE=$(git rev-parse @{u})
        local BASE=$(git merge-base @ @{u})

        if [[ $LOCAL = $REMOTE ]]; then
            echo "Up-to-date"
        elif [[ $LOCAL = $BASE ]]; then
            echo "Needs to pull"
            git pull --rebase || repo_failed "pull failed for $1"
        elif [[ $BASE = $REMOTE ]]; then
            echo "Needs to push"
            git push || repo_failed "push failed for $1"
        else
            echo "Diverged notify user"
            repo_failed "repo $1 needs manual merge/rebase..."
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
