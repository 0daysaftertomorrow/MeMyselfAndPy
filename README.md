# MeMyselfAndPy (WORK IN PROGRESS)
A fun little project for trying to describe myself (mostly for a bit of a new take on job applications and because it seemed like fun idea) in code.

# Victor Åhgren's Cybersecurity and Programming Profile

### I'm a cyber security consultant, bug bounty hunter, pentester, programmer, I basically do a bit of everything, and thought that this could be a fun way to make a presentation about yourself. I've only had a few hours to work on it, so it's a rough draft, but feel to use it if you want, nothing exceptional really, but if you want to tweak it and have fun - have at it!

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Class Descriptions](#class-descriptions)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is designed to encapsulate and display the personal and professional details of Victor Åhgren, a cybersecurity consultant with a diverse range of skills and interests. The information includes skills, programs, programming languages, hobbies, and personal traits.

## Features

- **Display Personal Information**: Prints personal information such as name, age, job titles, website, blog, and music site.
- **Skill Level Calculation**: Calculates and displays the skill level based on theory, usage, and usage time.
- **Categorized Program Listing**: Lists programs categorized into Offensive, Defensive, and Offensive/Defensive.
- **Traits and Hobbies**: Displays personal traits and hobbies.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/victor-profile.git
   cd victor-profile
   ```

2. **Install Dependencies**:
   This project requires `colorama` for colored terminal output. Install it using pip:
   ```bash
   pip install colorama
   ```

## Usage

Run the script to display Victor Åhgren's information:
```bash
python victor_profile.py
```

## Class Descriptions

### `About`
- Stores hobbies, interests, and traits.

### `Program`
- Represents a program with attributes such as name, category (Offensive/Defensive/Both), source (Open/Proprietary), and description.

### `Skill`
- Represents a skill with attributes such as name, theory, usage, usage time, and scope.

### `Person`
- Represents a person with personal and professional details.
- Methods:
  - `add_skill(skill)`: Adds a skill to the person's skill list.
  - `add_program(program)`: Adds a program to the person's program list.
  - `get_knowledge(skill)`: Calculates and returns the knowledge level and score of a skill.
  - `experience()`: Returns a dictionary of experiences.
  - `print_info()`: Prints all the information about the person in a formatted way.

## Example

An example instance of `Person` is created with detailed attributes and methods to add skills and programs. Running the script will display the following:

- Personal details
- Skills and their levels
- Categorized programs
- Programming languages
- Experiences
- Personal traits and hobbies

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or suggestions.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for visiting the repository! If you have any questions or feedback, feel free to open an issue or contact me directly.

Happy coding!
