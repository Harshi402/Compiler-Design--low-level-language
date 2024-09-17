# Compiler-Design--low-level-language
## Two major functionalities are:
Assembly-like instruction: It reads a specific ADD operation and processes it at the binary level, directly manipulating register values, which is similar to the way real hardware works. 
Register manipulation: This compiler interacts with a register file, retrieves values, performs binary arithmetic, and updates the register file. This emulates a key function of a CPU.

# Key Components
Binary Conversion Functions:

binaryToDecimal(): Converts a binary number to decimal format. It uses bitwise operations and powers of 2 to calculate the decimal value.
decimalToBinary(): Converts a decimal number to binary using Python’s bin() function and removes the '0b' prefix.
Register Handling:

The code uses a CSV file (register.csv) to represent registers, where each row corresponds to a register (e.g., R1, R7, R11), and the values might represent their current contents in binary format.
It loads the CSV file using pandas and processes the data with Numpy. This register handling is akin to a real CPU's register set, making it different from the previous high-level arithmetic interpreter.
Instruction Parsing:

The instruction "ADD R1, R7, R11" is split into individual components (ADD, R1, R7, R11) using regex, similar to how a CPU parses instructions into operations and operands.
The instruction ADD R1, R7, R11 means: add the contents of register R7 and R11, and store the result in register R1.
Binary Addition:

The code retrieves the binary values from R7 and R11 using pandas (np.where() is used to find the row indices for the registers). These values are processed by:
Converting them to decimal using binaryToDecimal().
Adding the two decimal values.
Converting the result back to binary with decimalToBinary().
The binary result is padded to 25 bits, which seems to reflect the target system's word size.
Register Update:

The result of the addition is split into 5 chunks, each of 5 bits.
These chunks are then used to update the values in the register.csv file, corresponding to register R1.
