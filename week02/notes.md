1. What did 'pwd' print?
/Users/anushkayadav
2. What did 'ls-a' show that plain 'ls' did not?
It showed hidden configuration files and directories starting with dot, such as.Trash, .vscode and .zsh_history. 

3. Pick one line from `ls -l`. What do you think the first column means?
Line: drwx---- + 5 anushkayadav staff 160 20 Aug 16:47 Desktop
The first column represents the file type and access permissions. The ‘d’ means it is a directory (folder).

4. Why does that work from where you are standing? Which kind of path is `coding-cafe/week02`? Absolute or Relative?
It works because the path starts looking from your current working directory (the home folder) rather than the root directory. This is a Relative path.
5. `mv` did two different jobs above. What were they?
The first `mv` command moved a file from one folder to another. The second `mv` command renamed the file.
6. How many folders are on your `PATH`? (They are separated by `:`)
There are 8 folders on my PATH.

7. Write down exactly where your `python3` lives.
/usr/bin/python3

8. Compare your answer to 7 with the person next to you. Are they the same? If not, why might that be?
NO, its not the same. Our outputs are different because we have python installed in different locations in our PC. Her output is C:\Users\YASHITA\AppData\Local\Programs\Python\Python314\python.exe
9. What exactly did the shell say? Explain the error in your own words, using the word **PATH**.
The shell said `zsh: command not found: pytor`. This error happens because `pytor` is misspelled, so the shell searched through every single folder listed on my **PATH** environment variable and could not find an executable program with that name.
10. `.venv` did not appear with plain `ls`. Why not? 
Because its name begins with a dot (.), making it a hidden file/directory that can only be seen using the `ls -a` command.

11. What changed about your prompt?

The prefix (.venv) appeared at the very beginning of my terminal prompt string, indicating that the virtual environment is currently active. 

12. Compare this with what you wrote down for question 7. Is it the same path? If not, what does that tell you about what activate actually did to your PATH?

No, it is a different path pointing to the Python executable inside my local .venv/bin/ folder. This tells me that the activate script prepended the virtual environment's bin folder to the front of my system **PATH** variable. 

13. What is in the second list that was not in the first?

The second list contains the requests package along with its necessary dependencies (such as charset-normalizer, idna, urllib3, and certifi) which were installed via pip. 

14. Where does python3 point now?

It points back to my system's original default Python folder (like /usr/bin/python3) because running deactivate removed the virtual environment path from the front of my **PATH** variable. 


15. Find what ls -h does. Write it in your own words.

The -h flag stands for human-readable format. When used along with -l, it alters the file sizes from large, hard-to-read byte counts into friendly formats like Kilobytes (K), Megabytes (M), or Gigabytes (G). 


16. What is the difference between what Ctrl + C and Ctrl + D did?
 
Pressing Ctrl + C sends a kill signal that interrupts and terminates the active process running in the foreground (like exiting a stuck script). Pressing Ctrl + D sends an End-of-File (EOF) marker to the shell, which cleanly closes the current python interactive session or logs out of the current terminal 
   