# Linux Journey

Link [here](https://linuxjourney.com/)

- Advanced Text-fu : a bit of a shame they don't spawn an interactive vim editor

- Permissions : umask changed the default missing permissions, stored in /etc/login.defs

- Permissions : even with SUID, you can't change the password of someone else because the passwd command look at your **real user ID**, not your **effective user ID**

- Permissions : the sticky bit ( *chmod +t* allows the user to be the only one able to delete a file/directory )