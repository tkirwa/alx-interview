# Star Wars API (0x06)

This repository contains a JavaScript script (`0-starwars_characters.js`) that interacts with the Star Wars API to retrieve and display characters from a specific movie. The script adheres to certain coding standards and requirements outlined below.

## Requirements

### General
- Editors: vi, vim, emacs
- Interpretation environment: Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- File specifications: All files should end with a new line, and the first line of each file should be `#!/usr/bin/node`.
- Mandatory files: README.md
- Code standards: Semistandard compliant with rules of Standard + semicolons on top (AirBnB style)
- Executability: All files must be executable
- No usage of `var`

### Additional Setup
- Install Node 10:
    ```bash
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```
- Install semistandard:
    ```bash
    $ sudo npm install semistandard --global
    ```
- Install the request module:
    ```bash
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
    ```

## Tasks

### 0. Star Wars Characters
**Mandatory**
Write a script (`0-starwars_characters.js`) that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID (e.g., `3` for "Return of the Jedi").
- Display one character name per line in the same order as the "characters" list in the `/films/` endpoint.
- Utilize the Star Wars API and the request module.

**Example:**
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Repository Information

- GitHub repository: [alx-interview](https://github.com/tkirwa/alx-interview)
- Directory: 0x06-starwars_api
- File: 0-starwars_characters.js