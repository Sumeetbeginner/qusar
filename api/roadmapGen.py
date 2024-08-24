import json
import numpy as np
from sklearn.decomposition import TruncatedSVD

topics_data = [
    {
        "topic_id": 1,
        "topic_name": "Algorithms",
        "description": "Study algorithms and data structures.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Basic understanding of programming concepts",
            "Proficiency in at least one programming language",
            "Understanding of time and space complexity analysis",
            "Familiarity with basic data structures (arrays, linked lists, stacks, queues)",
            "Knowledge of sorting and searching algorithms",
            "Understanding of recursion and backtracking",
            "Proficiency in dynamic programming techniques",
            "Knowledge of graph algorithms (BFS, DFS)",
            "Problem-solving skills",
            "Understanding of algorithm design paradigms",
            "Basic mathematical knowledge",
            "Familiarity with Big O notation",
            "Understanding of variables",
            "Loops",
            "Conditional statements",
            "Functions",
            "Data types",
            "Algebra",
            "Calculus",
            "Probability"
        ],
        "resources": ["https://example.com/algorithms-tutorial"],
        "related_topics": [
            "Sorting",
            "Searching",
            "Dynamic Programming",
            "Graph Algorithms",
            "Recursion",
            "Backtracking",
            "Data Structures",
            "Algorithm Design",
            "Time Complexity Analysis",
            "Space Complexity Analysis",
            "Binary Search",
            "Divide and Conquer",
            "Greedy Algorithms",
            "Hashing",
            "Tree Traversal",
            "Shortest Paths",
            "Minimum Spanning Trees",
            "Topological Sorting",
            "Heap Data Structure",
            "Linked Lists"
        ]
    },
    {
        "topic_id": 2,
        "topic_name": "Mechanical Engineering",
        "description": "Mechanical engineering is the discipline that applies engineering, physics, and materials science principles to design, analyze, manufacture, and maintain mechanical systems.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic physics principles",
            "Knowledge of mathematics (algebra, calculus)",
            "Familiarity with material science concepts",
            "Understanding of thermodynamics",
            "Proficiency in engineering drawing and CAD software",
            "Knowledge of mechanics (statics, dynamics)",
            "Understanding of fluid mechanics",
            "Familiarity with machine design principles",
            "Knowledge of manufacturing processes",
            "Understanding of heat transfer mechanisms",
            "Knowledge of control systems",
            "Proficiency in numerical methods",
            "Understanding of stress analysis",
            "Knowledge of robotics",
            "Familiarity with renewable energy systems",
            "Understanding of vibrations and acoustics",
            "Knowledge of automotive engineering",
            "Familiarity with aerospace engineering concepts",
            "Understanding of engineering ethics",
            "Proficiency in technical writing"
        ],
        "resources": [
            "https://www.asme.org/",
            "https://www.engineersedge.com/",
            "https://www.engineeringtoolbox.com/"
        ],
        "related_topics": [
            "Materials Science",
            "Thermodynamics",
            "Fluid Mechanics",
            "Machine Design",
            "Heat Transfer",
            "Control Systems",
            "Numerical Methods",
            "Stress Analysis",
            "Robotics",
            "Renewable Energy",
            "Vibrations",
            "Acoustics",
            "Automotive Engineering",
            "Aerospace Engineering",
            "Engineering Ethics",
            "CAD Software",
            "Engineering Drawing",
            "Manufacturing Processes",
            "Statics",
            "Dynamics"
        ]
    },

    {
        "topic_id": 3,
        "topic_name": "Civil Engineering",
        "description": "Civil engineering is the professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including works such as bridges, roads, dams, airports, buildings, and infrastructure.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic physics principles",
            "Knowledge of mathematics (algebra, calculus)",
            "Familiarity with material science concepts",
            "Proficiency in engineering drawing and CAD software",
            "Knowledge of mechanics (statics, dynamics)",
            "Understanding of fluid mechanics",
            "Familiarity with geotechnical engineering principles",
            "Knowledge of structural analysis",
            "Understanding of transportation engineering",
            "Proficiency in construction management",
            "Knowledge of environmental engineering",
            "Understanding of surveying techniques",
            "Familiarity with urban planning",
            "Knowledge of water resources engineering",
            "Understanding of earthquake engineering",
            "Proficiency in project management",
            "Knowledge of construction materials",
            "Understanding of reinforced concrete design",
            "Familiarity with steel structures",
            "Knowledge of building codes and regulations"
        ],
        "resources": [
            "https://www.asce.org/",
            "https://www.concrete.org/",
            "https://www.aisc.org/"
        ],
        "related_topics": [
            "Materials Science",
            "Structural Engineering",
            "Geotechnical Engineering",
            "Transportation Engineering",
            "Construction Management",
            "Environmental Engineering",
            "Surveying",
            "Urban Planning",
            "Water Resources Engineering",
            "Earthquake Engineering",
            "Project Management",
            "Reinforced Concrete Design",
            "Steel Structures",
            "Building Codes",
            "Infrastructure",
            "Bridges",
            "Roads",
            "Dams",
            "Airports",
            "Buildings"
        ]
    },
    {
        "topic_id": 4,
        "topic_name": "Computer Engineering",
        "description": "Computer engineering is a branch of engineering that integrates several fields of computer science and electronic engineering required to develop computer hardware and software.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic programming concepts",
            "Knowledge of at least one programming language (e.g., Python, Java, C++)",
            "Familiarity with data structures (arrays, linked lists, stacks, queues)",
            "Proficiency in algorithm design and analysis",
            "Understanding of computer architecture",
            "Knowledge of digital logic and circuits",
            "Familiarity with operating systems concepts",
            "Understanding of computer networks",
            "Knowledge of database management systems",
            "Proficiency in software engineering principles",
            "Understanding of computer graphics",
            "Familiarity with cybersecurity principles",
            "Knowledge of machine learning basics",
            "Understanding of embedded systems",
            "Proficiency in web development technologies",
            "Knowledge of artificial intelligence concepts",
            "Understanding of parallel and distributed computing",
            "Familiarity with computer vision principles",
            "Knowledge of robotics",
            "Understanding of cloud computing concepts"
        ],
        "resources": [
            "https://www.computer.org/",
            "https://www.stackoverflow.com/",
            "https://www.geeksforgeeks.org/"
        ],
        "related_topics": [
            "Programming Languages",
            "Data Structures",
            "Algorithms",
            "Computer Architecture",
            "Digital Logic",
            "Operating Systems",
            "Computer Networks",
            "Database Management Systems",
            "Software Engineering",
            "Computer Graphics",
            "Cybersecurity",
            "Machine Learning",
            "Embedded Systems",
            "Web Development",
            "Artificial Intelligence",
            "Parallel Computing",
            "Distributed Computing",
            "Computer Vision",
            "Robotics",
            "Cloud Computing"
        ]
    },
    {
        "topic_id": 5,
        "topic_name": "Electrical Engineering",
        "description": "Electrical engineering is a field of engineering that deals with the study and application of electricity, electronics, and electromagnetism.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic physics principles",
            "Knowledge of mathematics (algebra, calculus)",
            "Familiarity with circuit theory",
            "Proficiency in electrical circuit analysis",
            "Understanding of digital electronics",
            "Knowledge of analog electronics",
            "Familiarity with electromagnetic field theory",
            "Understanding of power systems",
            "Proficiency in signal processing",
            "Knowledge of control systems",
            "Understanding of electrical machines",
            "Familiarity with power electronics",
            "Knowledge of renewable energy systems",
            "Understanding of semiconductor devices",
            "Proficiency in electrical measurements",
            "Knowledge of communication systems",
            "Understanding of electrical safety standards",
            "Familiarity with microelectronics",
            "Knowledge of instrumentation and measurement techniques",
            "Understanding of electric drives"
        ],
        "resources": [
            "https://www.ieee.org/",
            "https://www.electrical-engineering-portal.com/",
            "https://www.allaboutcircuits.com/"
        ],
        "related_topics": [
            "Physics",
            "Mathematics",
            "Circuit Theory",
            "Digital Electronics",
            "Analog Electronics",
            "Electromagnetic Field Theory",
            "Power Systems",
            "Signal Processing",
            "Control Systems",
            "Electrical Machines",
            "Power Electronics",
            "Renewable Energy",
            "Semiconductor Devices",
            "Electrical Measurements",
            "Communication Systems",
            "Electric Safety Standards",
            "Microelectronics",
            "Instrumentation",
            "Measurement Techniques",
            "Electric Drives"
        ]
    },
    {
        "topic_id": 6,
        "topic_name": "Chemical Engineering",
        "description": "Chemical engineering is a branch of engineering that applies physical sciences (chemistry and physics), mathematics, and economics to efficiently use, produce, transform, and transport chemicals, materials, and energy.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic chemistry principles",
            "Knowledge of mathematics (algebra, calculus)",
            "Familiarity with physics concepts",
            "Proficiency in thermodynamics",
            "Understanding of fluid mechanics",
            "Knowledge of heat and mass transfer",
            "Familiarity with reaction engineering",
            "Understanding of process control",
            "Proficiency in chemical kinetics",
            "Knowledge of separations processes",
            "Understanding of material and energy balances",
            "Familiarity with environmental engineering principles",
            "Knowledge of polymer science",
            "Understanding of biochemical engineering",
            "Proficiency in reactor design",
            "Knowledge of petrochemical processes",
            "Understanding of plant design and economics",
            "Familiarity with safety and hazard analysis",
            "Knowledge of computational methods in chemical engineering",
            "Understanding of sustainability in chemical processes"
        ],
        "resources": [
            "https://www.aiche.org/",
            "https://www.chemengonline.com/",
            "https://www.learncheme.com/"
        ],
        "related_topics": [
            "Chemistry",
            "Physics",
            "Mathematics",
            "Thermodynamics",
            "Fluid Mechanics",
            "Heat Transfer",
            "Mass Transfer",
            "Reaction Engineering",
            "Process Control",
            "Chemical Kinetics",
            "Separations Processes",
            "Material and Energy Balances",
            "Environmental Engineering",
            "Polymer Science",
            "Biochemical Engineering",
            "Reactor Design",
            "Petrochemical Processes",
            "Plant Design",
            "Safety Analysis",
            "Hazard Analysis"
        ]
    },
    {
        "topic_id": 7,
        "topic_name": "Data Science Engineering",
        "description": "Data Science Engineering is an interdisciplinary field that combines domain knowledge, programming skills, and statistical techniques to extract insights and knowledge from data.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic programming concepts",
            "Proficiency in at least one programming language (e.g., Python, R)",
            "Familiarity with data manipulation and analysis libraries (e.g., Pandas, NumPy)",
            "Knowledge of statistics and probability",
            "Understanding of linear algebra",
            "Proficiency in data visualization techniques",
            "Knowledge of machine learning algorithms",
            "Understanding of data preprocessing techniques",
            "Familiarity with databases and SQL",
            "Proficiency in exploratory data analysis",
            "Knowledge of feature engineering",
            "Understanding of model evaluation metrics",
            "Familiarity with big data technologies (e.g., Hadoop, Spark)",
            "Proficiency in deep learning techniques",
            "Knowledge of natural language processing",
            "Understanding of time series analysis",
            "Familiarity with cloud computing platforms",
            "Proficiency in version control systems (e.g., Git)",
            "Knowledge of software engineering best practices",
            "Understanding of domain-specific knowledge"
        ],
        "resources": [
            "https://www.kaggle.com/",
            "https://www.datacamp.com/",
            "https://www.analyticsvidhya.com/"
        ],
        "related_topics": [
            "Programming Languages",
            "Data Manipulation",
            "Statistical Analysis",
            "Linear Algebra",
            "Data Visualization",
            "Machine Learning",
            "Data Preprocessing",
            "Databases",
            "Exploratory Data Analysis",
            "Feature Engineering",
            "Model Evaluation",
            "Big Data Technologies",
            "Deep Learning",
            "Natural Language Processing",
            "Time Series Analysis",
            "Cloud Computing",
            "Version Control",
            "Software Engineering",
            "Domain Knowledge",
            "Data Mining"
        ]
    },
    {
        "topic_id": 8,
        "topic_name": "AIML Engineering",
        "description": "AIML Engineering focuses on the development and application of artificial intelligence and machine learning algorithms to solve complex problems and make intelligent decisions.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic programming concepts",
            "Proficiency in at least one programming language (e.g., Python, R)",
            "Familiarity with data manipulation and analysis libraries (e.g., Pandas, NumPy)",
            "Knowledge of statistics and probability",
            "Understanding of linear algebra",
            "Proficiency in data visualization techniques",
            "Knowledge of machine learning algorithms",
            "Understanding of neural networks",
            "Familiarity with deep learning frameworks (e.g., TensorFlow, PyTorch)",
            "Proficiency in model evaluation and validation techniques",
            "Knowledge of feature engineering and selection",
            "Understanding of natural language processing",
            "Familiarity with reinforcement learning algorithms",
            "Proficiency in computer vision techniques",
            "Knowledge of time series analysis",
            "Understanding of transfer learning",
            "Familiarity with cloud computing platforms",
            "Proficiency in version control systems (e.g., Git)",
            "Knowledge of software engineering best practices",
            "Understanding of domain-specific knowledge"
        ],
        "resources": [
            "https://www.kaggle.com/",
            "https://www.tensorflow.org/",
            "https://www.pytorch.org/"
        ],
        "related_topics": [
            "Programming Languages",
            "Data Manipulation",
            "Statistical Analysis",
            "Linear Algebra",
            "Data Visualization",
            "Machine Learning",
            "Neural Networks",
            "Deep Learning",
            "Model Evaluation",
            "Feature Engineering",
            "Natural Language Processing",
            "Reinforcement Learning",
            "Computer Vision",
            "Time Series Analysis",
            "Transfer Learning",
            "Cloud Computing",
            "Version Control",
            "Software Engineering",
            "Domain Knowledge",
            "Data Mining"
        ]
    },
    {
        "topic_id": 9,
        "topic_name": "Cybersecurity Engineering",
        "description": "Cybersecurity Engineering involves protecting computer systems, networks, and data from cyber threats, attacks, and unauthorized access through the application of technologies, processes, and practices.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic computer science principles",
            "Proficiency in programming languages (e.g., Python, C, C++)",
            "Familiarity with operating systems concepts",
            "Knowledge of computer networks and protocols",
            "Understanding of cryptography principles",
            "Proficiency in risk assessment and management",
            "Knowledge of penetration testing techniques",
            "Understanding of security architectures and models",
            "Proficiency in secure coding practices",
            "Knowledge of threat modeling",
            "Understanding of incident response and recovery procedures",
            "Proficiency in network security technologies",
            "Knowledge of web security principles",
            "Understanding of cloud security concepts",
            "Proficiency in malware analysis techniques",
            "Knowledge of identity and access management",
            "Understanding of compliance and regulatory requirements",
            "Familiarity with security tools and utilities",
            "Proficiency in ethical hacking methodologies",
            "Knowledge of cybersecurity laws and policies"
        ],
        "resources": [
            "https://www.isc2.org/",
            "https://www.cybrary.it/",
            "https://www.sans.org/"
        ],
        "related_topics": [
            "Computer Science",
            "Programming Languages",
            "Operating Systems",
            "Computer Networks",
            "Cryptography",
            "Risk Assessment",
            "Penetration Testing",
            "Security Architectures",
            "Secure Coding",
            "Threat Modeling",
            "Incident Response",
            "Network Security",
            "Web Security",
            "Cloud Security",
            "Malware Analysis",
            "Identity and Access Management",
            "Compliance and Regulations",
            "Security Tools",
            "Ethical Hacking",
            "Cybersecurity Laws"
        ]
    },
    {
        "topic_id": 10,
        "topic_name": "Software Engineering",
        "description": "Software Engineering is the application of engineering principles to the design, development, testing, and maintenance of software systems.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic programming concepts",
            "Proficiency in at least one programming language (e.g., Python, Java, C++)",
            "Familiarity with data structures and algorithms",
            "Knowledge of software development methodologies (e.g., Agile, Waterfall)",
            "Understanding of version control systems (e.g., Git)",
            "Proficiency in software design patterns",
            "Knowledge of software testing techniques",
            "Understanding of software architecture principles",
            "Proficiency in debugging and troubleshooting",
            "Knowledge of software requirements engineering",
            "Understanding of software quality assurance practices",
            "Proficiency in documentation and technical writing",
            "Knowledge of user interface design principles",
            "Understanding of software project management",
            "Proficiency in continuous integration and continuous deployment (CI/CD)",
            "Knowledge of DevOps principles",
            "Understanding of software maintenance and evolution",
            "Proficiency in team collaboration and communication",
            "Knowledge of cybersecurity principles",
            "Understanding of ethical considerations in software development"
        ],
        "resources": [
            "https://www.sei.cmu.edu/",
            "https://www.infoq.com/",
            "https://www.atlassian.com/software-engineering"
        ],
        "related_topics": [
            "Programming Languages",
            "Data Structures",
            "Algorithms",
            "Software Development Methodologies",
            "Version Control",
            "Software Design Patterns",
            "Software Testing",
            "Software Architecture",
            "Debugging",
            "Requirements Engineering",
            "Quality Assurance",
            "Documentation",
            "User Interface Design",
            "Project Management",
            "Continuous Integration",
            "Continuous Deployment",
            "DevOps",
            "Software Maintenance",
            "Team Collaboration",
            "Cybersecurity",
            "Ethics in Software Engineering"
        ]
    },
    {
        "topic_id": 11,
        "topic_name": "Electronics and Communication Engineering",
        "description": "Electronics and Communication Engineering is a discipline that deals with the design, development, testing, and maintenance of electronic circuits and communication systems.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic physics principles",
            "Knowledge of mathematics (algebra, calculus)",
            "Familiarity with digital electronics",
            "Proficiency in analog electronics",
            "Understanding of semiconductor devices",
            "Knowledge of circuit theory",
            "Familiarity with signals and systems",
            "Proficiency in electronic circuit design",
            "Understanding of electromagnetic field theory",
            "Knowledge of communication systems",
            "Familiarity with microwave engineering",
            "Proficiency in embedded systems programming",
            "Understanding of wireless communication principles",
            "Knowledge of optical communication",
            "Familiarity with VLSI design",
            "Proficiency in control systems",
            "Understanding of telecommunication networks",
            "Knowledge of satellite communication",
            "Familiarity with digital signal processing",
            "Proficiency in FPGA programming"
        ],
        "resources": [
            "https://www.ieee.org/",
            "https://www.electronics-tutorials.ws/",
            "https://www.allaboutcircuits.com/"
        ],
        "related_topics": [
            "Physics",
            "Mathematics",
            "Digital Electronics",
            "Analog Electronics",
            "Semiconductor Devices",
            "Circuit Theory",
            "Signals and Systems",
            "Electronic Circuit Design",
            "Electromagnetic Field Theory",
            "Communication Systems",
            "Microwave Engineering",
            "Embedded Systems",
            "Wireless Communication",
            "Optical Communication",
            "VLSI Design",
            "Control Systems",
            "Telecommunication Networks",
            "Satellite Communication",
            "Digital Signal Processing",
            "FPGA Programming"
        ]
    },
    {
        "topic_id": 12,
        "topic_name": "OOPS",
        "description": "Object-Oriented Programming (OOP) is a programming paradigm based on the concept of 'objects', which can contain data in the form of fields and code in the form of procedures. It focuses on the design and creation of reusable software components.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic programming concepts",
            "Proficiency in at least one programming language (e.g., Java, C++, Python)",
            "Familiarity with procedural programming",
            "Knowledge of data structures and algorithms",
            "Understanding of classes and objects",
            "Proficiency in inheritance and polymorphism",
            "Knowledge of encapsulation and abstraction",
            "Understanding of constructors and destructors",
            "Proficiency in method overriding and overloading",
            "Knowledge of access modifiers",
            "Understanding of class relationships (e.g., association, aggregation, composition)",
            "Proficiency in exception handling",
            "Knowledge of interfaces and abstract classes",
            "Understanding of object-oriented design principles (e.g., SOLID)",
            "Proficiency in design patterns",
            "Knowledge of serialization and deserialization",
            "Understanding of memory management in OOP languages",
            "Proficiency in unit testing",
            "Knowledge of OOP concepts in different programming languages",
            "Understanding of real-world applications of OOP"
        ],
        "resources": [
            "https://www.javatpoint.com/oops-concepts",
            "https://www.tutorialspoint.com/object_oriented_analysis_design/index.htm",
            "https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/"
        ],
        "related_topics": [
            "Programming Languages",
            "Procedural Programming",
            "Data Structures",
            "Algorithms",
            "Inheritance",
            "Polymorphism",
            "Encapsulation",
            "Abstraction",
            "Constructors and Destructors",
            "Access Modifiers",
            "Class Relationships",
            "Exception Handling",
            "Interfaces and Abstract Classes",
            "Object-Oriented Design Principles",
            "Design Patterns",
            "Serialization and Deserialization",
            "Memory Management",
            "Unit Testing",
            "OOP in Different Languages",
            "Real-World Applications of OOP"
        ]
    },
    {
        "topic_id": 13,
        "topic_name": "AI",
        "description": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. It involves the creation of algorithms and models that enable computers to perform tasks that typically require human intelligence.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic programming concepts",
            "Proficiency in at least one programming language (e.g., Python, Java)",
            "Familiarity with data manipulation and analysis libraries (e.g., Pandas, NumPy)",
            "Knowledge of statistics and probability",
            "Understanding of linear algebra",
            "Proficiency in machine learning algorithms",
            "Knowledge of neural networks",
            "Familiarity with deep learning frameworks (e.g., TensorFlow, PyTorch)",
            "Understanding of natural language processing",
            "Knowledge of computer vision techniques",
            "Proficiency in reinforcement learning algorithms",
            "Understanding of optimization algorithms",
            "Knowledge of expert systems",
            "Familiarity with knowledge representation and reasoning",
            "Proficiency in AI model evaluation metrics",
            "Knowledge of AI ethics and bias",
            "Understanding of AI applications in various domains",
            "Familiarity with AI research methodologies",
            "Proficiency in AI project management",
            "Knowledge of AI deployment strategies"
        ],
        "resources": [
            "https://www.analyticsvidhya.com/",
            "https://www.kaggle.com/",
            "https://www.coursera.org/learn/artificial-intelligence"
        ],
        "related_topics": [
            "Programming Languages",
            "Data Manipulation",
            "Statistical Analysis",
            "Linear Algebra",
            "Machine Learning",
            "Neural Networks",
            "Deep Learning",
            "Natural Language Processing",
            "Computer Vision",
            "Reinforcement Learning",
            "Optimization Algorithms",
            "Expert Systems",
            "Knowledge Representation and Reasoning",
            "AI Model Evaluation Metrics",
            "AI Ethics",
            "AI Applications",
            "AI Research Methodologies",
            "AI Project Management",
            "AI Deployment Strategies",
            "AI in Various Domains"
        ]
    },
    {
        "topic_id": 14,
        "topic_name": "Business Economics",
        "description": "Business Economics is a field of applied economics that studies the economic aspects of organizations, markets, and industries, aiming to understand and analyze business decisions, strategies, and outcomes.",
        "difficulty": "Intermediate",
        "prerequisites": [
            "Understanding of basic economics principles",
            "Knowledge of microeconomics and macroeconomics",
            "Familiarity with statistical methods",
            "Proficiency in financial accounting",
            "Understanding of business management principles",
            "Knowledge of market structures and competition",
            "Familiarity with demand and supply analysis",
            "Proficiency in cost and production analysis",
            "Understanding of pricing strategies",
            "Knowledge of investment analysis",
            "Familiarity with risk management",
            "Proficiency in business forecasting",
            "Understanding of economic policies and regulations",
            "Knowledge of international trade and finance",
            "Familiarity with business ethics",
            "Proficiency in business decision-making models",
            "Understanding of corporate finance",
            "Knowledge of strategic management",
            "Familiarity with behavioral economics concepts",
            "Proficiency in economic modeling techniques"
        ],
        "resources": [
            "https://www.investopedia.com/",
            "https://www.khanacademy.org/",
            "https://www.econlib.org/"
        ],
        "related_topics": [
            "Economics Principles",
            "Microeconomics",
            "Macroeconomics",
            "Statistical Methods",
            "Financial Accounting",
            "Business Management",
            "Market Structures",
            "Competition",
            "Demand and Supply",
            "Cost and Production Analysis",
            "Pricing Strategies",
            "Investment Analysis",
            "Risk Management",
            "Business Forecasting",
            "Economic Policies",
            "International Trade",
            "Business Ethics",
            "Decision-Making Models",
            "Corporate Finance",
            "Strategic Management",
            "Behavioral Economics"
        ]
    }

]

users = [
    {"user_id": 1, "name": "User1", "test_score": 80, "watched_content": [
        "Software Engineering","AI"], "interests": ["Cybersecurity Engineering","Business Economics"]},
    # {"user_id": 2, "name": "User2", "test_score": 70, "watched_content": [
    #     "Cybersecurity Engineering"], "interests": ["Software Engineering"]},
    # {"user_id": 3, "name": "User3", "test_score": 90, "watched_content": [
    #     "Software Engineering", "OOPS"], "interests": ["Business Economics"]},
    # {"user_id": 4, "name": "User4", "test_score": 75, "watched_content": [
    #     "OOPS"], "interests": ["Web Development"]},
    # {"user_id": 5, "name": "User5", "test_score": 85, "watched_content": [
    #     "AI"], "interests": ["Algorithms"]},
]


def generate_roadmap(user):
    capability_matrix = np.array([
        [user["test_score"], len(user["watched_content"]),
         len(user["interests"])],
    ])

    svd = TruncatedSVD(n_components=1, random_state=42)
    svd.fit(capability_matrix)
    user_capability = svd.components_[0]

    roadmap = []

    for topic in topics_data:
        user_capability_list = list(user_capability)

        if topic["topic_name"] in user["watched_content"] or any(topic_keyword in topic["topic_name"] for topic_keyword in user["interests"]):
            # roadmap.append(topic)
             # Create the new roadmap item with the desired structure
            roadmap_item = {
                'label': topic['topic_name'],
                'description': f"{topic['description']}\n\nPrerequisites: {', '.join(topic['prerequisites'][:3])}\n\nRelevant resources: {', '.join(topic['resources'][:2])}\n\nRelated topics: {', '.join(topic['related_topics'][:2])}"
            }
            roadmap.append(roadmap_item)

    return roadmap


def roadmapGenFunc():
    roadmap = generate_roadmap(users[0])
    return roadmap



    # with open(f'user_{user["user_id"]}_roadmap.json', 'w') as f:
    #     json.dump(roadmap, f, indent=4)
