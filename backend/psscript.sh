#!/bin/bash

# The first thing the script does is to get a formatted 'ps' output, displaying
# the user, pid and the command that's running currently separated by semicolon. This will be saved in
# a .txt file called psoutput, in order to save the data in the database.
ps --no-headers -d -o %u: -o %p: -o %c: | sed -r 's/\s+//g' > psoutput.txt

# Each time the script runs, it will delete all the saved information in the
# 'process' table, in order to save the most recent output and display it in
# the React front end.
sqlite3 db.sqlite3 "delete from api_process"

# Here I declare a dictionary, and fill it with key-values fetched from the
# '/etc/passwd' file, linking the user with its UID.
declare -A users_map=()

# This loop iterates through each line of the file, storing the username and
# its UID in the dictionary that has been created above. Each username can be
# queried in order to see its UID.
# The variable $u stores the username, whereas the variable $uid stores its UID.
for i in `cat /etc/passwd | awk -F: '{printf("%s,%s\n"), $1, $3}'`; do
    u=$(echo $i | cut -d, -f1)    
    uid=$(echo $i | cut -d, -f2)    
    users_map[$u]=$uid
done

# Here the output.txt file created earlier will be iterated. Here is where the
# dictionary created earlier comes into play, in order to assign the UID to each user
# that is found in the file. 
# The $user variable saves the username from the ps output, which is then used to retrieve
# the UID from the dictionary.
# Each column of the 'ps' output is saved in individual variables and then saved into the database
for i in `cat psoutput.txt | awk -F: '{printf("%s,%s,%s\n"), $1, $2, $3}'`; do
    user=$(echo $i | cut -d, -f1)
    uid=$(echo ${users_map[$user]})
    pid=$(echo $i | cut -d, -f2)
    cmd=$(echo $i | cut -d, -f3)

    sqlite3 db.sqlite3 "insert into api_process(uid, user, pid, cmd) values($uid, '$user', $pid, '$cmd')"
done