# Robotics
Please follow these steps when beginning a project. 
Since we are all working together on one repo, it can cause some major problems.
Make sure that you follow ALL of these steps, or you could ruin everything.
## Setup
First you need to setup a branch for you to work on.
* In Github, go to the top of the file explorer. There you should see something called "# branches". Click on that.
* That should bring you to the list of branches, and a button to click that says "New Branch"
* Create your branch with the name of yours (capital first).
  * example: Anthony

You will need to create a codespace using the your branch.
* At the top of the page, press the + button, and click "New codespace".
  * The Repo is Scecina-STEM/Robotics
  * Make sure that the branch is main
* Once the code editor loads up, first change what branch you are on.
  * At the very bottom left, next to the codespace name, it should say main
  * Click on that, then at the top select your branch

After you change branches, do the following.
* Once you are in, you need to run a command to create a folder for yourself.
* Go to the terminal and type in the following code (replacing words in brackets as needed)

```
mkdir [your name (lowercase)]
```

```
EXAMPLE
mkdir anthony
```

* This is the ONLY place that you should be writing your code. Each user will have their own, so that when we merge them together, everyone's code is sperate.
* IF YOU DON'T, then we'll have really big problems when we merge the codes.
* DO NOT EDIT ANOTHER PERSON'S DIRECTORY (FOLDER) OR BRANCH!

Lastly, you'll need to run some code to setup your Github envirment.
* Run the following code, exactly as it is.
```
git config pull.rebase true
```
* Lastly, change your location using the cd command
```
cd [your directory]
```

```
EXAMPLE
cd anthony
```

## Helpful Bash Commands

The terminal is a powerful tool, one that you shall master. For now, here are some simple commands.

### cd [directory]

* This changes what directory you are in.
* There are some special things to note:
  * ```./``` means 'this directory'.
  * ```../``` means 'parent directory' or the directory higher than it.
  * ```/``` specifies a directory, i.e. 'anthony' whould be a file with no extention and 'anthony/' would be a directory.

### ls | la

* This function tell you what files are in the directory you are in.
* The different between ```ls``` and ```la``` is that the first shows defualt directories and file, while the second whould hidden items as well.