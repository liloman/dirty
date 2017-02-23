#!/usr/bin/env bash
#Execute a rsync time backup machine o the dir passed 


include_dir() {
    local dir=$1
    local abs_dir="$(realpath -P "$dir" 2>/dev/null)"
    local -i max=0 cur=0
    local -a com=(find "." -type d)
    local line=
    count_slashes() {
        local line=$1
        cur=0

        for (( i = 0; i < ${#line}; i++ )); do
            [[ ${line:$i:1} == / ]] && ((cur++))
        done
    }

    [[ -d $abs_dir ]] || { echo "dir $dir not found"; return; }
    
    cd "$abs_dir"

    while IFS= read -r line
    do
        count_slashes "${line:2}"
        (( cur > max )) && max=$cur && win="${line:2}"
    done < <("${com[@]}" 2>&1)

    count_slashes "$dir"
    ((max+=cur)) 

    #split it
    IFS=/ read -a paths <<< "$dir$win"
    line=""
    for path in "${paths[@]}" ; do
        line+="/$path"
        echo "$line/"
        echo "$line/*"
    done

    echo "max:$max para $dir$win"
}

do_backup() {
    local count=${#@}
    local all=("${@}")
    (( count < 2 )) && { echo "You must specify at least two dirs (source dest)"; return; }
    for (( i = 0; i < $((count-1)); i++ )); do
        include_dir "${all[$i]}"
    done

}

# rsync_tmbackup.sh 

do_backup "$@"
