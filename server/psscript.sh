#!/bin/bash

# Each time the script runs, it will delete all the saved information in the
# 'process' and 'users' tables, in order to save the most recent output and display it in
# the React front end.
sqlite3 db.sqlite3 "delete from api_process; delete from api_users; vacuum;"

# Here I declare a dictionary, and fill it with key-values fetched from the
# '/etc/passwd' file, linking the user with its UID.
declare -A users_map=()

# This loop iterates through each line of the file, storing the username and
# its UID in the dictionary that has been created above. Each username can be
# queried in order to see its UID.
# The variable $user stores the username, whereas the variable $uid stores its UID.
for info in $(cat /etc/passwd | awk -F: '{printf("%s,%s\n"), $1, $3}'); do
    user=$(echo $info | cut -d, -f1)    
    uid=$(echo $info | cut -d, -f2)    
    users_map[$user]=$uid

    sqlite3 db.sqlite3 "insert into api_users(uid, user) values($uid, '$user');"
done

# In this code the 'ps' command is stored, formatted to display the user, 
# pid and the command/process that is running. The 'sed' command is used 
# to remove all white space, in order to be able to iterate through each piece of information
# with the 'awk' command. The code then starts to iterate through
# each item, saving the necessary information in its variable, to save it later
# in the databse, using the sqlite query at the end of the loop. 
for item in $(ps --no-headers -d -o %u: -o %p: -o %c: | sed -r 's/\s+//g' | awk -F: '{printf("%s,%s,%s\n"), $1, $2, $3}'); do
    user=$(echo $item | cut -d, -f1)
    uid=$(echo ${users_map[$user]})
    pid=$(echo $item | cut -d, -f2)
    cmd=$(echo $item | cut -d, -f3)

    sqlite3 db.sqlite3 "insert into api_process(uid, user, pid, cmd) values($uid, '$user', $pid, '$cmd');"
done