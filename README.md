# mano_microprogram_computer_simulator
An assembler and hardware simulator for the Mano Computer with micro program control unit .

Built using simple memory and registers modules such as AC, AR, PC etc...
## Memory
### Program Memory
main program code is written in `program.txt` and it placed in main Memory(16*2048) after assembling process .
### Micro Program Memory
micro program code is written in `microProgram.txt` and it placed in micro Memory(20*128) after assembling process .

It determines control unit micro program routins and it can only be changed by changing `.txt` file .
## Assembler
### Program Asssembler
This Basic Computer has a 16-bit instruction divided into 11-bit address, 4-bit opcode and 1-bit for addressing mode.

decoded opcode is used to determine micro program routine address in micro memory .
### Micro Program Asssembler
control unit has a 20-bit instruction divided into 9-bit for 3 micro opration, 2-bit for condition state , 2 bit for branch mode and 7-bit for addressing .

## Registers
AC | 16*'0' |
--- | --- |
DR | 16*'0' |
PC | 11*'0' |
AR | 11*'0' |
CAR | 7*'0' |
SBR | 7*'0' |

## frontEnd
It is implemented using tkinter and get program code as input . 
> If no code is given to the input, it uses the default memory value in the `program.txt` .

it runs `CPU.py` and shows final resault value of registers .

## Assembly Language Rules
*  Any label that is not following by colon must yield an error. (with no space)
*  Program instruction column can have any of the supported instructions in micro program code .
*  the operand must have static value or correspond to a label included in this assembly code. Reference to labels that do not exist in the same assembly file must cause an error.
*  There is at least one space between every column
*  Empty lines must cause an error.
*  Addresses placed after `ORG` are in hexadecimal

# Usage
clone the project and run `frontEnd.py`

# Contributors
Arash Azarpoor : azarpoor81@gmail.com

Zahra Sarami : z.sarami81@gmail.com

