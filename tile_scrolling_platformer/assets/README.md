The assets directory contains costumes and sounds for the tile scrolling
platformer game. The assets come from Griffpatch's project
[Tile Scrolling Tutorial Assets | Parts 1 to 20](https://scratch.mit.edu/projects/485855713/).
The assets were extracted from the Scratch project as follows:

1. Save the Scratch project as a file using File > Save to your computer.
2. Rename the Scratch project so that it ends with `.zip` instead of `.sb3`:
   ```
   mv "Tile Scrolling Tutorial Assets _ Parts 1 to 20.sb3" project.zip`
   ```
3. Unzip the file:
   ```
   unzip project.zip
   ```
4. Write a script file that will create directories for each sprite in the
   project:
   ```
   jq -r '
     .targets[] |
     .name as $sprite |
     "mkdir -p \($sprite)/costumes \($sprite)/sounds"
   ' project.json > dirs.sh
   ```
   This creates costumes and sounds directories for each sprite in the Scratch
   project.
5. Execute the script just created: `sh dirs.sh`
6. Scratch stores costumes using filenames like
   `7e8ac47439b6e317171b978587129b0d.png`. To make these human-readable, I
   created a script to rename them. The script uses `project.json` to figure
   out their original names, and then moves them to the costumes subdirectories:
   ```
   jq -r '
     .targets[] |
     .name as $sprite |
     .costumes |
     to_entries[] |
     "mv \(.value.md5ext) \\
       \($sprite)/costumes/\((1000 + .key | tostring)[1:])-\(.value.name |
         gsub(" "; "-")).\(.value.md5ext | split(".")[1])"
   ' project.json > costumes.sh
   ```
   This deserves some explanation.
   * Having access to the costume number is useful to emulate Scratch behavior
     such as the `next costume` block. I left-padded the costume number with
     leading zeros using `(1000 + .key | tostring)[1:]`. `[1:]` removes the
     leading `1` added by `1000 + .key`.
   * To substitute `-` for spaces, I used `gsub(" "; "-")`.
   * Finally, I added the file extension using `.value.md5ext | split(".")[1]`.
7. Execute the script to rename the costumes: `sh costumes.sh`.
8. Write another script file to rename sounds:
   ```
   jq -r '
     .targets[] |
     .name as $sprite |
     .sounds |
     to_entries[] |
     "cp \(.value.md5ext) \\
       \($sprite)/sounds/\((1000 + .key | tostring)[1:])-\(.value.name |
         gsub(" "; "-")).\(.value.md5ext | split(".")[1])"                   
   ' project.json > sounds.sh
   ```
   Notes:
   * The `jq` script leaves a single quote character (`'`) in one of the file
     names. Rather than editing the `jq` script, I just removed the character in
     `sounds.sh`.
   * The script uses `cp` instead of `mv` because some of the sounds in the
     Scratch project are shared between sprites.
9. Execute the script to rename the sounds: `sh sounds.sh`.