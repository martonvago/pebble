
# Pebble
Pebble is a paperless, non-networked voting application for the Uxn virtual machine.
This was my final year project at Birkbeck in 2023.

## How to run
### Setting up
#### Emulator:
`pebble` runs on [Uxn](https://wiki.xxiivv.com/site/uxn.html), a virtual stack-machine.  To run `pebble` you need to have `uxncli`, the Uxn emulator without a graphics mode. You can download `uxncli` from https://sr.ht/~rabbits/uxn/#download-binaries .
 #### Pebble:
 You can build Pebble from the source code yourself:
 1. Make sure imports are set up correctly (see [Imports](#imports) section).
 2. Download the Uxn assembler from https://sr.ht/~rabbits/uxn/#download-binaries
 3. Run: `uxnasm pebble.tal pebble.rom`, assuming that `uxnasm` is on the `PATH`.

**Alternatively**, you can use the pre-built `pebble.rom` file included in this repository.

Start Pebble by typing:

    uxncli pebble.rom
assuming that `uxncli` is on the `PATH`.
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

> Note: Pebble works with unsigned 32-bit integers, supporting numbers up to and including 4 294 967 295.

## Development
To work on the project you need to download the Uxn assembler (`uxnasm`) and CLI emulator (`uxncli`) from [https://sr.ht/~rabbits/uxn/#download-binaries](https://sr.ht/~rabbits/uxn/#download-binaries) .
### Source code
The source code is located in the `src` folder:
- `pebble.tal`: entry point and program control logic
- `functions.tal`: state-independent subroutines 
- [math32.tal](http://plastic-idolatry.com/erik/nxu/math32.tal): library providing support for unsigned 32-bit integers

### Imports
The code uses absolute file names when importing `.tal` files in other `.tal` files to allow for a more complex folder structure.  This is necessary because Uxn resolves imports relative to the entry point `.tal` file, and `.tal` entry points in the test folder are at various different locations. 

Therefore, when setting the project up for the first time, the absolute path to the project root folder has to be substituted in for the imports to resolve successfully.

To do this, run

    ./resolve-imports.sh
   
**from the project root folder**.

### Tests
Tests are located in the `test` folder:
- `unit`: tests for subroutines in `functions.tal`
- `integration`: tests for the application as a whole

A test suite consists of a `.test.tal` and a `.test.py` file: the former sets up a template of an operation or function call in `uxntal` and the latter populates and executes this template over a series of test cases, validating the output of the Uxn machine.

Both types of tests are instrumented using the `Tester` class in `tester.py`. 
- the `test` method is used when the component under test takes no input.
- the `interact` method is used when the component under test does take input.

**To run all tests:**
1. Install Python 3 and the following packages:
   * [ultraimport](https://github.com/ronny-rentner/ultraimport)
   * [colorama](https://github.com/tartley/colorama)
2. Make sure imports are set up correctly (see [Imports](#imports) section).
3. Make sure `tester.py` is pointing to the correct location for `uxnasm` and `uxncli`. By default it is assumed that they are both on the `PATH`.
4. From the `test` folder run: `./run-tests.sh`

Individual tests can be run by running individual `.test.py` files.
