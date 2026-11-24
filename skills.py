# skills.py
# Skill reference data for the Skill Gap Analyzer.
# Each skill: a unique ID (key) -> name, aliases (how it appears on resumes), category.

SKILLS = {
    # ---------- Programming & Core ----------
    "python": {
        "name": "Python",
        "aliases": ["python", "python3"],
        "category": "Programming",
    },
    "sql": {
        "name": "SQL",
        "aliases": ["sql", "mysql", "postgresql", "postgres", "t-sql", "pl/sql"],
        "category": "Programming",
    },
    "r": {
        "name": "R",
        "aliases": ["r programming", "rlang", "r language"],
        "category": "Programming",
    },
    "java": {
        "name": "Java",
        "aliases": ["java", "core java"],
        "category": "Programming",
    },
    "git": {
        "name": "Git / Version Control",
        "aliases": ["git", "github", "gitlab", "version control"],
        "category": "Programming",
    },

    # ---------- Data Handling ----------
    "pandas": {
        "name": "Pandas",
        "aliases": ["pandas"],
        "category": "Data Handling",
    },
    "numpy": {
        "name": "NumPy",
        "aliases": ["numpy"],
        "category": "Data Handling",
    },
    "data_cleaning": {
        "name": "Data Cleaning",
        "aliases": ["data cleaning", "data cleansing", "data wrangling", "data preprocessing"],
        "category": "Data Handling",
    },
    "etl": {
        "name": "ETL / Data Pipelines",
        "aliases": ["etl", "data pipeline", "data pipelines", "elt"],
        "category": "Data Handling",
    },
    "excel": {
        "name": "Excel",
        "aliases": ["excel", "microsoft excel", "ms excel", "spreadsheets"],
        "category": "Data Handling",
    },

    # ---------- Statistics & Analysis ----------
    "statistics": {
        "name": "Statistics",
        "aliases": ["statistics", "statistical analysis", "stats"],
        "category": "Statistics",
    },
    "probability": {
        "name": "Probability",
        "aliases": ["probability", "probability theory"],
        "category": "Statistics",
    },
    "hypothesis_testing": {
        "name": "Hypothesis Testing / A/B Testing",
        "aliases": ["hypothesis testing", "a/b testing", "ab testing", "significance testing"],
        "category": "Statistics",
    },
    "regression": {
        "name": "Regression Analysis",
        "aliases": ["regression", "linear regression", "logistic regression"],
        "category": "Statistics",
    },

    # ---------- Visualization & BI ----------
    "data_viz": {
        "name": "Data Visualization",
        "aliases": ["data visualization", "data visualisation", "matplotlib", "seaborn", "plotly"],
        "category": "Visualization",
    },
    "power_bi": {
        "name": "Power BI",
        "aliases": ["power bi", "powerbi"],
        "category": "Visualization",
    },
    "tableau": {
        "name": "Tableau",
        "aliases": ["tableau"],
        "category": "Visualization",
    },
    "looker": {
        "name": "Looker",
        "aliases": ["looker", "looker studio"],
        "category": "Visualization",
    },

    # ---------- Machine Learning ----------
    "machine_learning": {
        "name": "Machine Learning",
        "aliases": ["machine learning", "ml", "supervised learning", "unsupervised learning"],
        "category": "Machine Learning",
    },
    "scikit_learn": {
        "name": "scikit-learn",
        "aliases": ["scikit-learn", "sklearn", "scikit learn"],
        "category": "Machine Learning",
    },
    "deep_learning": {
        "name": "Deep Learning",
        "aliases": ["deep learning", "neural networks"],
        "category": "Machine Learning",
    },
    "pytorch": {
        "name": "PyTorch",
        "aliases": ["pytorch", "torch"],
        "category": "Machine Learning",
    },
    "tensorflow": {
        "name": "TensorFlow",
        "aliases": ["tensorflow", "keras"],
        "category": "Machine Learning",
    },

    # ---------- AI / GenAI ----------
    "nlp": {
        "name": "Natural Language Processing",
        "aliases": ["nlp", "natural language processing", "text mining"],
        "category": "AI / GenAI",
    },
    "computer_vision": {
        "name": "Computer Vision",
        "aliases": ["computer vision", "image processing", "opencv"],
        "category": "AI / GenAI",
    },
    "llm": {
        "name": "Large Language Models",
        "aliases": ["llm", "llms", "large language models", "gpt", "transformers"],
        "category": "AI / GenAI",
    },
    "generative_ai": {
        "name": "Generative AI",
        "aliases": ["generative ai", "genai", "gen ai"],
        "category": "AI / GenAI",
    },
    "rag": {
        "name": "RAG (Retrieval-Augmented Generation)",
        "aliases": ["rag", "retrieval augmented generation", "retrieval-augmented"],
        "category": "AI / GenAI",
    },
    "ai_agents": {
        "name": "AI Agents",
        "aliases": ["ai agents", "agentic", "langchain", "langgraph"],
        "category": "AI / GenAI",
    },
    "prompt_engineering": {
        "name": "Prompt Engineering",
        "aliases": ["prompt engineering", "prompting"],
        "category": "AI / GenAI",
    },
    "vector_db": {
        "name": "Vector Databases",
        "aliases": ["vector database", "vector db", "pinecone", "faiss", "chroma", "weaviate"],
        "category": "AI / GenAI",
    },

    # ---------- Deployment & Infra ----------
    "apis": {
        "name": "APIs / REST",
        "aliases": ["api", "apis", "rest api", "restful", "fastapi", "flask"],
        "category": "Deployment & Infra",
    },
    "docker": {
        "name": "Docker",
        "aliases": ["docker", "containers", "containerization"],
        "category": "Deployment & Infra",
    },
    "kubernetes": {
        "name": "Kubernetes",
        "aliases": ["kubernetes", "k8s"],
        "category": "Deployment & Infra",
    },
    "cloud": {
        "name": "Cloud Platforms",
        "aliases": ["aws", "azure", "gcp", "cloud", "google cloud"],
        "category": "Deployment & Infra",
    },
    "mlops": {
        "name": "MLOps",
        "aliases": ["mlops", "ml ops", "model deployment", "ci/cd"],
        "category": "Deployment & Infra",
    },

    # ---------- Soft / Business ----------
    "communication": {
        "name": "Communication / Data Storytelling",
        "aliases": ["communication", "data storytelling", "presentation", "stakeholder management"],
        "category": "Soft Skills",
    },
}

# Adjacent skills: having the value gives partial credit (half weight) for the key.
RELATED = {
    "pytorch": ["tensorflow"],
    "tensorflow": ["pytorch"],
    "power_bi": ["tableau", "looker"],
    "tableau": ["power_bi", "looker"],
    "looker": ["power_bi", "tableau"],
    "scikit_learn": ["machine_learning"],
    "machine_learning": ["scikit_learn", "regression"],
    "deep_learning": ["pytorch", "tensorflow"],
    "pandas": ["numpy", "excel"],
    "numpy": ["pandas"],
    "statistics": ["probability", "hypothesis_testing", "regression"],
    "probability": ["statistics"],
    "hypothesis_testing": ["statistics"],
    "regression": ["statistics"],
    "data_viz": ["power_bi", "tableau", "looker"],
    "data_cleaning": ["pandas", "etl"],
    "etl": ["data_cleaning", "sql"],
    "llm": ["nlp", "generative_ai"],
    "generative_ai": ["llm", "prompt_engineering"],
    "rag": ["vector_db"],
    "vector_db": ["rag"],
    "ai_agents": ["llm"],
    "prompt_engineering": ["generative_ai", "llm"],
    "kubernetes": ["docker"],
    "mlops": ["docker", "cloud"],
    "cloud": ["docker"],
    "python": ["r", "java"],
}
