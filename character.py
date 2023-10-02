from langchain.chains import ConversationChain
from langchain.llms import LlamaCpp
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory import CombinedMemory, ConversationBufferWindowMemory, ConversationEntityMemory, ConversationSummaryMemory, ConversationSummaryBufferMemory

#Necessary packages for the LLM.

#Character class, every individual character will be an instance of this class.
class Character():
    #In the init, we need to initialize the character's stats. This will effect how the character operates.
    def __init__(self, charname:str, model:str, stats:dict[str, int], abilities:dict[str, int], backstory:str):
        self.charname = charname
        self.stats = stats
        self.backstory = SystemMessage(backstory)
        self.parameters = self.__stat_converter(self.stats)
        self.llm = LlamaCpp(model_path=model)
        self.chain = ConversationChain(llm=self.llm, **self.parameters)

    #This function defines what each stat means practically for the llm.
    def __stat_converter(stats)-> dict:
        #TODO

    #talk functionality, simply returns whatever the llm says in response to the prompt.
    def reply(self, input):
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="Respond to the message in character, your backstory is as follows:/n"+self.backstory),
            HumanMessage(content=input)]
            )
        self.chain(prompt=prompt)