from colorama import Fore, Style, init

# Initialize colorama
init()

class About:
    def __init__(self):
        self.hobbies = ["Cybersecurity", "Programming", "Drumming", "Making music", "Obviously spending time with close friends and family!"]
        self.interests = ["A general love for learning new things, meeting interesting people and just grow as a person!"]
        self.traits = ["Detail-oriented", "Analytical with a very high work ethic", 
                       "Teamwork makes the dream work! I truly believe in a diverse range of opinions and personalities in a team. What I care about is merit and how each person contributes to the end goal."]

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_trait(self, trait):
        self.traits.append(trait)

    def get_hobbies(self):
        return self.hobbies

    def get_interests(self):
        return self.interests

    def get_traits(self):
        return self.traits

class Program:
    def __init__(self, name, category, source, description):
        self.name = name
        self.category = category  # Offensive/defensive/both
        self.source = source  # Open/proprietary
        self.description = description

class Skill:
    def __init__(self, name, theory, usage, usage_time):
        self.name = name
        self.theory = theory
        self.usage = usage
        self.usage_time = usage_time

class Person:
    def __init__(self, firstname, lastname, age, jobtitles, website, blog, musicsite, bonus_skills, interests, hobbies, skills, traits, programs, programming_languages):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.jobtitles = jobtitles
        self.website = website
        self.blog = blog
        self.musicsite = musicsite
        self.interests = interests
        self.bonus_skills = bonus_skills
        self.hobbies = hobbies
        self.skills = skills
        self.traits = traits
        self.programs = programs
        self.programming_languages = programming_languages

    def add_skill(self, name, theory, usage, usage_time):
        self.skills.append(Skill(name, theory, usage, usage_time))

    def add_program(self, name, category, source, description):
        self.programs.append(Program(name, category, source, description))

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_bonus_skill(self, bonus_skill):
        self.bonus_skills.append(bonus_skill)

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

    def add_trait(self, trait):
        self.traits.append(trait)

    def add_programming_language(self, language):
        self.programming_languages.append(language)

    def get_knowledge(self, skill):
        n = (skill.theory + skill.usage + skill.usage_time) / 3

        if n >= 4.5:
            return "Highly experienced and competent", n
        elif 3 <= n < 4.5:
            return "Very experienced and competent", n
        elif 2 <= n < 3:
            return "Experienced, as competent as time allowed", n
        elif 1 <= n < 2:
            return "Familiar with, would be fully operational very quickly", n
        elif 0 <= n < 1:
            return "Have tried but not very experienced", n
        else:
            return "Might know what it is, but haven't handled it directly", n

    def experience(self):
        return [
            f"{Fore.LIGHTBLUE_EX} Penetration testing:{Style.RESET_ALL} No matter if it's different forms of bug bounty hunting, to more proper OSCP kind of engagement, I'm here for it and I'm always looking to learn and grow!",
            f"{Fore.LIGHTBLUE_EX} OSINT:{Style.RESET_ALL} Experience in gathering and analyzing information from open sources",
            f"{Fore.LIGHTBLUE_EX} SOC/Analyst roles:{Style.RESET_ALL} Having used basically every single major SIEM/XDR-systems known to man, along with decades of learning new software ranging from Adobe's Photoshop, AE, Premiere, moving to 3D-modelling/rendering software",
            f"{Fore.LIGHTBLUE_EX} Problem-solving:{Style.RESET_ALL} Experience in breaking down and solving complex problems",
            f"{Fore.LIGHTBLUE_EX} Data analysis:{Style.RESET_ALL} Experience in analyzing large amounts of data and drawing insightful conclusions"
        ]

    def get_personal_info(self):
        return {
            "Name": f"{self.firstname} {self.lastname}",
            "Age": self.age,
            "Job Titles": self.jobtitles,
            "Website": self.website,
            "Blog": self.blog,
            "Music Site": self.musicsite,
            "Interests": self.interests,
            "Hobbies": self.hobbies,
            "Bonus Skills": self.bonus_skills,
            "Skills": [(skill.name, self.get_knowledge(skill)) for skill in self.skills],
            "Traits": self.traits,
            "Programs": [(program.name, program.category, program.description) for program in self.programs],
            "Programming Languages": self.programming_languages,
            "Experience": self.experience()
        }

    def print_info(self):
        info = self.get_personal_info()
        print(f"{Fore.LIGHTBLUE_EX}Name:{Style.RESET_ALL} {info['Name']}")
        print(f"{Fore.LIGHTBLUE_EX}Age:{Style.RESET_ALL} {info['Age']}")
        print(f"{Fore.LIGHTBLUE_EX}Job Titles:{Style.RESET_ALL} {', '.join(info['Job Titles'])}")
        print(f"{Fore.LIGHTBLUE_EX}Website:{Style.RESET_ALL} {Fore.WHITE}{info['Website']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Blog:{Style.RESET_ALL} {Fore.WHITE}{info['Blog']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Music Site:{Style.RESET_ALL} {Fore.WHITE}{info['Music Site']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Bonus Skills:{Style.RESET_ALL} {Fore.WHITE}{', '.join(info['Bonus Skills'])}{Style.RESET_ALL}")
        print(f"\n{Fore.LIGHTBLUE_EX}Skills:{Style.RESET_ALL}")
        for skill_name, (level, score) in info["Skills"]:
            print(f"  {Fore.YELLOW}Skill:{Style.RESET_ALL} {Fore.WHITE}{skill_name}{Style.RESET_ALL}, Level: {Fore.WHITE}{level}{Style.RESET_ALL}, Score: {Fore.WHITE}{score}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Programs:{Style.RESET_ALL}")
        categories = {'Offensive': [], 'Defensive': [], 'Offensive/Defensive': []}
        for program in self.programs:
            categories[program.category].append(program)

        for category, programs in categories.items():
            if programs:
                color = Fore.RED if category == "Offensive" else Fore.GREEN if category == "Defensive" else Fore.YELLOW
                print(f"{color}{category}:{Style.RESET_ALL}")
                for program in programs:
                    print(f"  {color}Program:{Style.RESET_ALL} {program.name}, {Fore.YELLOW}Description:{Style.RESET_ALL} {program.description}")
                print("\n")

        print(f"{Fore.GREEN}Programming Languages:{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}{', '.join(info['Programming Languages'])}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Experience:{Style.RESET_ALL}")
        for exp in info["Experience"]:
            print(f"{Fore.WHITE}{exp}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Personality Traits:{Style.RESET_ALL}")
        for trait in info["Traits"]:
            print(f"  {Fore.CYAN}{trait}{Style.RESET_ALL}")

        print(f"\n{Fore.LIGHTBLUE_EX}Hobbies:{Style.RESET_ALL}")
        for hobby in info["Hobbies"]:
            print(f"{Fore.CYAN}{hobby}{Style.RESET_ALL}")

# Create an instance of Person and print the information
victor = Person(
    firstname="Victor",
    lastname="Åhgren",
    age=34,
    jobtitles=["Cyber Security Consultant/Analyst/Engineer"],
    website="https://victorahgren.com/",
    blog="https://victorahgren.notion.site/VICTOR-HGREN-CYBER-SECURITY-SPECIALIST-f9e8a93d1a634af09c7d1ce083ade798",
    musicsite="https://www.youtube.com/@victorahgren560",
    interests=['problem-solving', 'coding', 'hacking', '(quantum)-cryptography', 'Privacy', 'Freedom'],
    bonus_skills=["2x zero-day finder"],
    hobbies=["Cybersecurity", "Programming", "Drumming", "Making music", "Spending time with close friends and family"],
    skills=[
        Skill("Defensive security", 4.28, 3.4, 3.5),
        Skill("Offensive security", 4.6, 4.78, 4.36),
        Skill("Programming", 4.5, 4.8, 5),
        Skill("Cybersecurity", 4.7, 4.9, 5)
    ],
    traits=["Detail-oriented", "Analytical", "Team-oriented", "High work ethic"],
    programs=[
        Program("Nessus", "Defensive", "Proprietary", "A vulnerability scanner developed by Tenable, Inc."),
        Program("Metasploit", "Offensive", "Open-source & proprietary pro version", "A framework for developing and executing exploit code."),
        Program("Nmap", "Offensive/Defensive", "Open-source", "A network scanning tool to discover hosts and services."),
        Program("Burp Suite", "Offensive", "Proprietary", "A graphical tool for testing web application security.")
    ],
    programming_languages=["Python", "C", "Java", "JavaScript", "C++", "Rust", "Golang", "PHP"]
)

# Print all information about Victor Åhgren
victor.print_info()
