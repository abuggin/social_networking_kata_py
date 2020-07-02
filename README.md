# CLI Social Network

## What is it

Kata exercise on TDD and an excuse for me to some active learning in Python.

- _Red, Green, Refactor prefixes to commit_ are not going to happen in a real codebase.
- project structure is very flat
  - I think that being a very simple problem there is no harm in having everything very reachable.
- any feedback is welcome

### How to Run program

`python main.py`

### How to Run tests

Run all test in folder by:
`python -m unittest discover .`

---

## Description of the Kata

This application allows you have a mini cli social network on your device!

EXAMPLE COMMANDS:

1. Josh -> Hello!
    This command will create a new user called "Josh" and will post a message saying "Hello!"

2. Josh
    Simply typing the username will display all the posts that user has added.

3. Josh follows Bob
    By using this command, you can follow other users on the system

4. Josh wall
    This command will show all the posts the user Josh and all of the users they are following.
    These posts are sorted by the most recent first.

Assume valid input

---

## TODO

- [ ] check if runs on another machine as well
- [x] make it interactive
  - [x] run on main
  - [ ] display output
    - [ ] could improve display with author name and time, since I already have both
- [x] `<username> -> <message>` write command
  - [x] create user
    - [x] what happens when you create multiple times the same username?
      - given the use case provided in the example, it should be transparent if the username exists or not.
      - aka don't return error if operation succeed or not
  - [x] save message to user
  - [x] cli interface
- [x] `<username>` display user posts
  - [x] already implemented when saving messages by picking dictionary datastructure
  - [x] what happens when the username is not known to the system? two options come to mind
    - inform the users that the system doesn't have such a username
      - this one is more explicit, but not requested, so I'll post-pone the implementation for now
    - return an empty list of posts
      - this make sense as well so I'll go with this one
      - [x] decision documented with a test
  - [x] cli interface
- [x] `<username> follow <username1>`
  - [x] create relationship between users
    - [x] if one of the two usernames is missing, not a big deal, we make an empty link, we can always restrict later
  - [x] cli interface
- [x] `<username> wall`
  - [x] display post of users followed by `<username>`
  - [x] sort them by most recent first
  - [x] include own posts
  - [x] cli interface

---

## TODO for fun

- [ ] split message id and message body
  - [ ] store message body separately in a db
- [ ] fix time complexity of feed creation
  - [ ] pagination of feed creation

---

## Feed creation time complexity

This is a toy example but we can still find a better time complexity for the algorithm.

Right now, there are no limits to the size of a `wall`/feed generation call.

In a real life scenario, we can't pull all the data from a database of all the _comments_ of all the _users_ that the requesting user is following.

### Half baked idea

[omissis]
