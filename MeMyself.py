from colorama import Fore, Style, init

# Initialize colorama
init()

class About:
    def __init__(self):
        self.hobbies = ["Cybersecurity", "Programming", "Drumming", "Making music", "Obviously spending time with close friends and family!"]
        self.interests = ["A general love for learning new things, meeting interesting people and just grow as a person!"]
        self.traits = ["Detail-oriented", "Analytical with a very high work ethic", "Teamwork makes the dream work! I truly believe in a diverse range of opinions and personalities in a team, which all bring something different to the table, what I only care about is merit and hoping to find a workplace where people genuinely are eager to get to work, see if you and your team can crack that problem that you've spent the night thinking about, that's something truly wonderful -People loving their work, which most often rubs of and creates a really fun, productive and learning environment for everyone!"]

class Program:
    def __init__(self, name, category, source, description):
        self.name = name
        self.category = category  # Offensive/defensive/both
        self.source = source  # Open/proprietary
        self.description = description

class Skill:
    def __init__(self, name, theory, usage, usage_time, scope):
        self.name = name
        self.theory = theory
        self.usage = usage
        self.usage_time = usage_time
        self.scope = scope

class Person:
    def __init__(self, firstname, lastname, age, jobtitles, website, blog, musicsite, interests, hobbies, skills, traits, programs, programming_languages):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.jobtitles = jobtitles
        self.website = website
        self.blog = blog
        self.musicsite = musicsite
        self.interests = interests
        self.hobbies = hobbies
        self.skills = skills
        self.traits = traits
        self.programs = programs
        self.programming_languages = programming_languages

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_program(self, program):
        self.programs.append(program)

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
        return {
            "Penetration testing": "No matter if it's different forms of bug bounty hunting, to more proper OSCP kind of engagement, I'm here for it and I'm always looking to learn and grow!",
            "OSINT": "Experience in gathering and analyzing information from open sources",
            "SOC/Analyst roles: Having used basically every single major SIEM/XDR-systems known to man, along with decades of learning new software ranging from Adobes Photoshop, AE, Premiere, moving to 3D-modelling/rendering software like Cinema 4D, or 3DS Max, to infinity and beyond has provided a natural methodology for adapting to new tech, which also happens to be something I find super interesting, so lucky me!"
            "Problem-solving": "Experience in breaking down and solving complex problems",
            "Data analysis": "Experience in analyzing large amounts of data and drawing insightful conclusions"
        }

    def print_info(self):
        print(f"{Fore.LIGHTBLUE_EX}Name:{Style.RESET_ALL} {self.firstname} {self.lastname}")
        print(f"{Fore.LIGHTBLUE_EX}Age:{Style.RESET_ALL} {self.age}")
        print(f"{Fore.LIGHTBLUE_EX}Job Titles:{Style.RESET_ALL} {', '.join(self.jobtitles)}")
        print(f"{Fore.LIGHTBLUE_EX}Website:{Style.RESET_ALL} {Fore.WHITE}{self.website}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Blog:{Style.RESET_ALL} {Fore.WHITE}{self.blog}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Music Site:{Style.RESET_ALL} {Fore.WHITE}{self.musicsite}{Style.RESET_ALL}")
        print(f"\n{Fore.LIGHTBLUE_EX}Skills:{Style.RESET_ALL}")
        for skill in self.skills:
            level, score = self.get_knowledge(skill)
            print(f"  {Fore.YELLOW}Skill:{Style.RESET_ALL} {Fore.WHITE}{skill.name}{Style.RESET_ALL}, Level: {Fore.WHITE}{level}{Style.RESET_ALL}, Score: {Fore.WHITE}{score}{Style.RESET_ALL}")

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
        print(f"  {Fore.YELLOW}{', '.join(self.programming_languages)}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Experience:{Style.RESET_ALL}")
        for key, value in self.experience().items():
            print(f"  {Fore.YELLOW}{key}: {value}{Style.RESET_ALL}")

        about = About()
        print(f"\n{Fore.GREEN}Personality Traits:{Style.RESET_ALL}")
        for trait in about.traits:
            print(f"  {Fore.YELLOW}{trait}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Hobbies:{Style.RESET_ALL}")
        for hobby in about.hobbies:
            print(f"  {Fore.YELLOW}{hobby}{Style.RESET_ALL}")

# Create an instance of Person and add skills and programs
victor = Person(
    firstname="Victor",
    lastname="Åhgren",
    age=34,
    jobtitles=["Cyber Security Consultant/Analyst/Engineer"],
    website="https://victorahgren.com/",
    blog="https://victorahgren.notion.site/VICTOR-HGREN-CYBER-SECURITY-SPECIALIST-f9e8a93d1a634af09c7d1ce083ade798",
    musicsite="https://open.spotify.com/user/XXXXX",
    interests=[],
    hobbies=["Cybersecurity", "Programming", "Drumming", "Making music", "Obviously spending time with close friends and family!"],
    skills=[
        Skill("Defensive security", 4.28, 3.5, 3),
        Skill("Offensive security", 4.6, 4.78, 4.36),
        Skill("Programming", 4.5, 4.8, 5, 4),
        Skill("Cybersecurity", 4.7, 4.9, 5, 4.5)
    ],
    traits=["Detail-oriented", "Analytical with a very high work ethic", "Teamwork makes the dream work! I truly believe in a diverse range of opinions and personalities in a team, which all bring something different to the table, what I only care about is merit and hoping to find a workplace where people genuinely are eager to get to work, see if you and your team can crack that problem that you've spent the night thinking about, that's something truly wonderful -People loving their work, which most often rubs of and creates a really fun, productive and learning environment for everyone!"],
    programs=[
        Program("Nessus", "Defensive", "Proprietary", "A vulnerability scanner developed by Tenable, Inc."),
        Program("Metasploit", "Offensive", "Open-source & proprietary pro version", "A framework for developing and executing exploit code against a remote target machine."),
        Program("Burp Suite", "Offensive", "Proprietary", "A graphical tool for testing web application security."),
        Program("Nmap", "Offensive/Defensive", "Open-source", "A network scanning tool to discover hosts and services on a computer network."),
        Program("Naabu", "Offensive/Defensive", "Open-source", "A fast port scanner written in Go."),
        Program("Dnsx", "Defensive", "Open-source", "A fast and multi-purpose DNS toolkit powered by the simple and fast Golang."),
        Program("Rapid7 InsightVM", "Defensive", "Proprietary", "A vulnerability management solution."),
        Program("Trellix package", "Defensive", "Proprietary", "A cybersecurity package."),
        Program("Qualys", "Defensive", "Proprietary", "A cloud-based platform for vulnerability management."),
        Program("IBM QRadar", "Defensive", "Proprietary", "A security information and event management (SIEM) product."),
        Program("CrowdStrike Falcon", "Defensive", "Proprietary", "A cloud-native endpoint security solution."),
        Program("Splunk", "Defensive", "Proprietary", "A platform for searching, monitoring, and analyzing machine-generated data."),
        Program("BBot", "Offensive", "Open-source", "A bundle of close to 100 different tools with API keys to widen its amazing capabilities")
    ],
    programming_languages=["Python", "C", "Java", "JavaScript", "C++"]
)

# Print all information about Victor Åhgren
victor.print_info()
