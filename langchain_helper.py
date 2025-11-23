from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from cfg import Config


print(Config.API_KEY)  # Проверка, что ключ загружен правильно


llm = ChatGroq(
    model=Config.MODEL_NAME,      
    temperature=Config.TEMPERATURE, 
    api_key=Config.API_KEY     
)
    

def generate_pet_name(animal_type, pet_color):

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet. Return only names"
    )
    

    name_chain = prompt_template_name | llm | StrOutputParser()

    response = name_chain.invoke({'animal_type': animal_type, 'pet_color': pet_color })
    return response


if __name__ == "__main__":
    print(generate_pet_name(input(), input()))