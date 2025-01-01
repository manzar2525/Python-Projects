import os
from dotenv import load_dotenv

def configure():
        load_dotenv()




import openai



def main():
        configure()
        print("High")
        print(os.getenv('OPENAI_API_KEY'))
        print("Low")


main()