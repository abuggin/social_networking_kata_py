# CLI Social Network

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

Thanks for using this awesome program, with great power comes great responsibility.

---

## TODO

- [ ] `<username> -> <message>` write command
  - [x] create user
    - [x] what happens when you create multiple times the same username?
      - given the use case provided in the example, it should be transparent if the username exists or not.
      - aka don't return error if operation succeed or not
  - [x] save message to user
  - [ ] cli interface
- [ ] `<username>` display user posts
  - [x] already implemented when saving messages by picking dictionary datastructure
  - [x] what happens when the username is not known to the system? two options come to mind
    - inform the users that the system doesn't have such a username
      - this one is more explicit, but not requested, so I'll post-pone the implementation for now
    - return an empty list of posts
      - this make sense as well so I'll go with this one
      - [x] decision documented with a test
  - [ ] cli interface
- [ ] `<username> follow <username1>`
  - [ ] create relationship between users
    - [ ] if one of the two usernames is missing, not a big deal, we make an empty link, we can always restrict later
- [ ] `<username> wall`
  - [ ] display post of users followed by `<username>`
