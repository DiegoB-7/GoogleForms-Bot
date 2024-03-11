class Option:
    
    def __init__(self,question:str,answers:list[str],id:str):
        self.id = id
        self.question = question
        self.answers = answers
        
    def __str__(self):
        print("Question:", self.question)
    