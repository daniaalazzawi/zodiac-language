# Zodiac Programming Language

A domain-specific language (DSL) for generating personalized zodiac sign summaries based on user-provided birth data.

Created by DaniaA

## Overview

Zodiac is a specialized programming language designed for astrology and personality analysis applications. It simplifies the process of collecting user birth information and generating structured astrological insights.

### Key Features

- **Built-in Zodiac Sign type** with enums for all 12 signs
- **Automatic date parsing** and time-zone aware calculations
- **Template literals** for combining user data with zodiac descriptions
- **Functional paradigm** with first-class functions
- **Clean, intuitive syntax** for working with astrological data

## Installation

### Prerequisites

- Python 3.8 or higher
- textX (for language parsing)
- PyTZ (for timezone calculations)

### Setup

1. Clone the repository:
   ```
   https://github.com/daniaalazzawi/zodiac-language.git
   ```

2. Navigate to the project directory:
   ```
   cd zodiac-language
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run an example program:
   ```
   python run_zodiac.py examples/hello_world.zod
   ```

## Language Syntax

### Variables

```
var firstName: String = input("Enter first name:");
var age: Int = 25;
var isBirthday: Bool = true;
var sign: ZodiacSign = getZodiac(birthDate);
```

### Control Structures

```
if (sign == "Aries") {
    print("You are bold and energetic.");
} else {
    print("Different traits apply.");
}
```

### Functions

```
func getZodiac(day: Int, month: Int) -> String {
    // returns zodiac sign based on date
}
```

## Example Programs

### Hello World

```
// Hello World Program in Zodiac language
func main() {
    print("Welcome to Zodiac Programming Language!");
}

main();
```

### Basic Zodiac Summary

```
// Basic Zodiac Summary Program
func main() {
    var firstName: String = input("First Name: ");
    var birthDate: String = input("Birthdate (YYYY-MM-DD): ");
    var sign: String = getZodiac(birthDate);
    
    print("Hello " + firstName + ", your zodiac sign is " + sign + "!");
}

main();
```

### Detailed Personality Report

```
// Detailed Personality Report Program
func main() {
    var info = collectUserInfo(); // asks for name, date, time, region, gender
    var report = generateReport(info);
    print(report);
}

main();
```

### FizzBuzz Implementation

```
// FizzBuzz Program in Zodiac language
func main() {
    print("FizzBuzz Program");
    print("---------------");
    
    var limit: String = input("Enter the maximum number: ");
    var max: Int = parseInt(limit);
    
    runFizzBuzz(max);
}

func parseInt(str: String) -> Int {
    // Simple parsing function
    return str;
}

func runFizzBuzz(max: Int) {
    for (var i = 1; i <= max; i = i + 1) {
        if (i % 15 == 0) {
            print("FizzBuzz");
        } else if (i % 3 == 0) {
            print("Fizz");
        } else if (i % 5 == 0) {
            print("Buzz");
        } else {
            print(i);
        }
    }
}

main();
```

## Project Structure

```
zodiac-language/
├── examples/                  # Example Zodiac programs
│   ├── hello_world.zod
│   ├── basic_summary.zod
│   ├── detailed_report.zod
│   ├── compatibility_checker.zod
│   └── fizzbuzz.zod
├── src/
│   ├── zodiac_grammar.py      # textX grammar definition
│   └── zodiac_interpreter.py  # Interpreter implementation
├── run_zodiac.py              # Runner script
├── website/                   # Language website
│   └── index.html
├── README.md
└── requirements.txt
```

## Implementation Details

The Zodiac language is implemented using:

1. **textX** for grammar definition and model parsing
2. **Python** for the interpreter implementation
3. **Entity-based** modeling for language concepts

## License

This project is provided for educational purposes and is available under the MIT License.

## Acknowledgments

- Special thanks to the textX framework for making language development accessible
- Inspired by astrological applications like Co-Star
