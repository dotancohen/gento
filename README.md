
# Gento

Track bugs in a Git repo.

The name is a a portmanteau of "Git Entomology", the original but hard-to-remember name of the project.


## Features

- All users get updates as soon as they pull the repo. No need to pull multiple repos or otherwise change your workflow.
- Extensible, web GUIs such as that provided by Github can be added.
- Extensible, extant Git GUIs can be extended to support the issues as well.
- 100% Secure. There is no server to hack, and all sensitive information is encrypted.


## Working principal

From [the fine manual](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects):

> Git is a content-addressable filesystem. It means that at the core of Git is a simple key-value data store. What this means is that you can insert any kind of content into a Git repository, for which Git will hand you back a unique key you can use later to retrieve that content.

That sounds like as good a way as any to store and distribute a bug tracker!


## Roadmap

### Pre-release

[x] Ability to create, list, and show basic issues.
[ ] Store issues directly in the git key-value data store, without intermediate files. Support create, list, and show basic issues.
[ ] Store additional metadata such as user who created the issue, and display all data nicely formatted. The system should be usable for tracking basic issues at this point.
[ ] Ability to change issue status, such as to clone or mark as dupe. Duped issues should be properly marked with a reference to the dupe.

### 0.5

[ ] Close issues on [commit message](https://github.blog/2013-01-22-closing-issues-via-commit-messages/). Perhaps change to status "fix-commited" before the feature branch is merged to master.
[ ] Create example web interface.
[ ] Ability to encrypt issues to be viewable only be specific users. This is to facilitate reporting security vulnerabilities.

### Alpha release 0.7

[ ] Support pull requests from remote resources.
[ ] Support encrypting pull requests. Perhaps on PR, encrypted diffs should be added in a new branch. Need input.

### Beta release 0.9

[ ] Should we support documentation, as done in Pagure? Why is documentation separate from code in Pagure?


## Similar projects

### [Pagure](https://pagure.io/)

This project stores code, documentation, issues, and pull requests in separate Git repositories. It also does not provide a CLI to accessing the data.

### [pagure-cli](https://github.com/fedora-infra/pagure-cli)

CLI for Pagure


## Changelog

### 0.1.1 - 2020-11-06

- Project Rename
- Roadmap

### 0.1.0 - 2020-11-05

- Create Issue
- Show Issue
- List Issues


## License

Gento is licensed under the GNU General Public License v2.0. See LICENSE file for further information.


