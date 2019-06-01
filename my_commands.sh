#!/bin/bash

function create()
{
  cd
  cd /Users/peter/Documents/Github/CreateGit
  python3 create.py $1
  cd /Users/peter/Documents/Github/$1
  git init
  git remote add origin git@github.com:pette1999/$1.git
  touch README.md
  git add .
  git commit -m "Initial commit"
  git push -u origin master
}

#source my_commands.sh
