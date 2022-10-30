# Contributing guide

Welcome to Savannah Silica Django Community

## Community

The [Savannah Silica slack](https://join.slack.com/t/hackathoncommunityorg/shared_invite/zt-1i750moad-N6Y1dgKI5Sef9JXYytH9lg) is the primary communication forum for the Savannah Silica community. It is a good place to start whether you have a question, are a new contributor, are a new user, or anything else. Please review our community norms before posting. The Savannah Silica community is also governed by a [code of conduct](https://docs.github.com/articles/github-community-guidelines)


## Ways to contribute

- Feel free to check the [issues page](https://github.com/savannah-Silica/django-backend/issues).
- Look up for issues you will like to tackle on. You can create new issues.
- Comment on the issue you would like to tackle. For example: ```Hello!, I would like to take up this issue```
- The maintainers will assign you to one of the issues.
- You can now get started ! All the best.

## How do I Contribute ?


**1. Fork the repository**
- Fork the [Django-backend](https://github.com/savannah-Silica/django-backend) by clicking on the fork button on the top of the page.
- This will create a copy of this repository in your account.


**2. clone the repository**
- Now clone the repo to your machine
- Click on the clone button and then click the copy to clipboard icon.
- Open a terminal( bash on linux/mac, command prompt on windows) and run the following git command: ```git clone "url you just copied" ``` 
- For example : ``git clone https://github.com/yourusername/django-backend.git `` where ```yourusername``` is your Github username

**3. Create a branch**
- Change to the repository directory on your computer (if you are not already there): ```cd django-backend```
- Now create a branch rebasing the pre-dev branch using the ``git checkout`` or ``git branch`` command: 
```bash
git checkout -b <issue-number-title> pre-dev
```
or
```bash
git branch <issue-number-title> pre-dev
git checkout <issue-number-title>
```
- For example: 
```bash
git checkout -b issue-10-create-readme-file pre-dev
```
or 
```bash
git branch issue-10-create-readme-file pre-dev
git checkout issue-10-create-readme-file
```
Read more on [git and GitHub](https://docs.github.com/en/get-started/quickstart/hello-world)
> Note the branch needs to show issue, number and title

**4. Make necessary changes and commit those changes**
> Make sure to follow steps laid out on the [README](https://github.com/savannah-Silica/django-backend/blob/main/README.md) file to setup the development environment on your machine
- You can now create/modify files in the code repository in reference to the issue you were assigned.
- Save the file.
- On executing the command ``git status``, you'll see there are changes.
- Add those changes to the branch you just created using the ``git add .`` command:
- ``git add <the file you created or ammended>``
- Now commit those changes using the ``git commit`` command:
- ``git commit -m "a description of the contribution made``


**5. Push changes to GitHub**
- Push your changes using the command ``git push``
```bash
git push origin <issue-number-title>
```
- (replacing < issue-title_number > with the name of the branch you created earlier.)

**6. Submit your changes for review**
- If you go to your repository on GitHub, you’ll see a Compare & pull request button. 
- Click on that button.
- Write a comment on the contributions made making sure to fill the template as provided.
- Link the issue you were working on by making sure the line `Fixes:` has the issue number after it e.g. `Fixes: #10`
- click create pull request button
- Wait for reviews then resolve any issues
- You will get a notification email once the changes have been merged

**You did it!**
- You now have what it takes to my your contributions! Clap for yourself !!👏👏👏
