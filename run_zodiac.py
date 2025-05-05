#!/usr/bin/env python3
"""
Zodiac Language Runner
Usage: python run_zodiac.py <program_file.zod>
"""

import sys
import os
from src.zodiac_interpreter import run_zodiac_program

def main():
    if len(sys.argv) < 2:
        print("Error: No Zodiac program file specified")
        print("Usage: python run_zodiac.py <program_file.zod>")
        print("\nAvailable example programs:")
        
        # List available .zod files
        examples = [f for f in os.listdir('.') if f.endswith('.zod')]
        for i, example in enumerate(examples, 1):
            print(f"{i}. {example}")
        
        # Allow selecting an example
        choice = input("\nEnter the number of the example to run (or press Enter to exit): ")
        if choice and choice.isdigit() and 1 <= int(choice) <= len(examples):
            program_file = examples[int(choice) - 1]
        else:
            return
    else:
        program_file = sys.argv[1]
    
    if not os.path.exists(program_file):
        print(f"Error: File '{program_file}' does not exist.")
        return
    
    print(f"\nRunning Zodiac program: {program_file}\n")
    try:
        run_zodiac_program(program_file)
        print("\nProgram completed successfully.")
    except Exception as e:
        print(f"\nError running program: {str(e)}")

if __name__ == "__main__":
    main()