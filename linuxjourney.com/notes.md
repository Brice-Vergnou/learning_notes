# Linux Journey

Link [here](https://linuxjourney.com/)

## Advanced text fu

- a bit of a shame they don't spawn an interactive vim editor

## Permissions

- umask changed the default missing permissions, stored in /etc/login.defs

- even with SUID, you can't change the password of someone else because the passwd command look at your **real user ID**, not your **effective user ID**

- the sticky bit ( *chmod +t* allows the user to be the only one able to delete a file/directory )

## Processes

- TTY terminal were the command was executed and

- Process creation...