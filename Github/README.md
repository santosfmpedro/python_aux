# Github

    git clone repository 
    git add .
    git commit -m 'message'
    git push 
    git branch
    git checkout 

    git init initializes a brand new Git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.

    git clone creates a local copy of a project that already exists remotely. The clone includes all the project's files, history, and branches.

    git add stages a change. Git tracks changes to a developer's codebase, but it's necessary to stage and take a snapshot of the changes to include them in the project's history. This command performs staging, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project's history. Staging and committing separately gives developers complete control over the history of their project without changing how they code and work.

    git commit saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that's been staged with git add will become a part of the snapshot with git commit.

    git status shows the status of changes as untracked, modified, or staged.

    git branch shows the branches being worked on locally.

    git merge merges lines of development together. This command is typically used to combine changes made on two distinct branches. For example, a developer would merge when they want to combine changes from a feature branch into the main branch for deployment.

    git pull updates the local line of development with updates from its remote counterpart. Developers use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment.

    git push updates the remote repository with any commits made locally to a branch.

    download a repository on GitHub to our machine
    Replace `owner/repo` with the owner and name of the repository to clone
    git clone https://github.com/owner/repo.git

    # change into the `repo` directory
    cd repo

    # create a new branch to store any new changes
    git branch my-branch

    switch to that branch (line of development)
    git checkout my-branch

    make changes, for example, edit `file1.md` and `file2.md` using the text editor

    stage the changed files
    git add file1.md file2.md

    # take a snapshot of the staging area (anything that's been added)
    git commit -m "my snapshot"

    push changes to github
    git push --set-upstream origin my-branch

    create a new directory, and initialize it with git-specific functions
    git init my-repo

    change into the `my-repo` directory
    cd my-repo

    create the first file in the project
    touch README.md

    git isn't aware of the file, stage it
    git add README.md

    take a snapshot of the staging area
    git commit -m "add README to initial commit"

    provide the path for the repository you created on github
    git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git

    push changes to github
    git push --set-upstream origin main

    change into the `repo` directory
    cd repo

    update all remote tracking branches, and the currently checked out branch
    git pull

    change into the existing branch called `feature-a`
    git checkout feature-a

    make changes, for example, edit `file1.md` using the text editor

    stage the changed file
    git add file1.md

    take a snapshot of the staging area
    git commit -m "edit file1"

    push changes to github
    git push
