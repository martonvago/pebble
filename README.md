# Pebble
Pebble is a paperless, non-networked voting application for the Uxn virtual machine.

## How to run
### Setting up
#### Emulator:
`pebble` runs on [Uxn](https://wiki.xxiivv.com/site/uxn.html), a virtual stack-machine.  To run `pebble` you need to have `uxncli`, the Uxn emulator without a graphics mode. You can download `uxncli` from https://sr.ht/~rabbits/uxn/#download-binaries .
 #### Pebble:
 You can build `pebble` from the source code yourself using the Uxn assembler from https://sr.ht/~rabbits/uxn/#download-binaries :

    <path/to>uxnasm <path/to>pebble.tal <path/to>pebble.rom

Alternatively, you can use the pre-built `pebble.rom` file included in this repository.

Start Pebble by typing:

    <path/to>uxncli <path/to>pebble.rom

### Commands

|Name                      |Example                          |Description                         |
|----------------------|-------------------------------|-----------------------------|
|`setup <#candidates>`|`setup 5`            |Set the number of candidates. This number is exclusive of the invalid vote option, which is always included by default. The minimum number of candidates is 2. Resets the vote counts.            |
|`start vote`          |`start vote`            |Start the election / vote. Resets the vote counts.           |
|`vote <#candidate>`          |`vote 2`|Cast a vote for a candidate / option. `vote 0` casts an invalid vote. Casting multiple votes in a row is not allowed.|
|`next voter`          |`next voter`|Allow the next voter to enter a vote.|
|`end vote`          |`end vote`|End the election / vote.|
|`add results <results>`          |`add results 2;64;54;233;9;`|Add vote results from another voting machine to the vote results on this machine.* |
|`tabulate`          |`tabulate`|Display the results of the vote / election.|

\*`add results` argument format:
 - Vote counts provided must be separated by `;`.
 - Must start with a digit, can end with a digit or a `;`.
 - Number of vote counts provided must match the number of candidates configured on this machine, including the invalid vote option.

## Development
### Source code

### Tests
