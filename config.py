# config.py
# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "Daniel Fine": {
        "objectives": [
            "Partner with e-commerce platforms to add 500 small businesses in a quarter."
        ],
        "tasks": [
            "Identify top 3 platforms for small businesses and discuss API integration."
        ]
    }, 
    "InvestorB": {
        "objectives": ["Objective 1 for InvestorB", "Objective 2 for InvestorB", "Objective 3 for InvestorB"],
        "tasks": ["Task 1 for InvestorB", "Task 2 for InvestorB", "Task 3 for InvestorB"]
    },
    # Add more investors and their specific tasks as needed
}
# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "Daniel Fine"