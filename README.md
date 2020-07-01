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
  - [ ] create user
    - what happens when you create multiple times the same username?
    - given the use case provided in the example, it should be transparent if the username exists or not.
  - [ ] save message to user
- [ ] `<username>` display user posts
- [ ] `<username> follow <username1>`
  - [ ] create relationship between users
- [ ] `<username> wall`
  - [ ] display post of users followed by `<username>`
