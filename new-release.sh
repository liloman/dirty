#!/usr/bin/env bash

#create a new tag, upload it and release a build in copr
tito tag
git push --follow-tags
