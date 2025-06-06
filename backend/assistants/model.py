from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS as LangchainFAISS
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from backend.config.config import Config
from dotenv import load_dotenv
import os

load_dotenv()

class ChatbotHandler:
    def __init__(self, vectorDB_path):
        config = Config()

        # Store multiple API keys in a list
        self.api_keys = [
            "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",
            "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",
            "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",
            "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",
            "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",
            "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"
        ]

        self.llm = config.get('settings', 'llm')
        self.model = config.get('settings', 'model')
        self.vectorDB = LangchainFAISS.load_local(
            vectorDB_path,
            HuggingFaceEmbeddings(model_name=self.model),
            allow_dangerous_deserialization=True
        )
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key='chat_history',
            output_key='result',
            input_key='input'
        )
        self.conversation_chain = self.setup_conversation_chain()

    def setup_conversation_chain(self):
        for key in self.api_keys:
            try:
                # Attempt to initialize with each API key until one works
                llm = ChatGroq(
                    api_key=key,
                    model_name=self.llm,
                    temperature=0
                )
                print(f"✅ Using API Key: {key[:10]}...")
                break
            except Exception as e:
                print(f"❌ Failed with key {key[:10]}...: {e}")
                llm = None

        if llm is None:
            raise Exception("All API keys failed!")

        with open('prompt.txt', 'r') as file:
            prompt_text = file.read().strip()

        prompt_chatbot = ChatPromptTemplate.from_messages([
            ('system', prompt_text),
            MessagesPlaceholder('chat_history'),
            ('human', '{input}')
        ])

        context_retriever = create_history_aware_retriever(
            llm, self.vectorDB.as_retriever(), prompt_chatbot
        )
        document_chain = create_stuff_documents_chain(llm, prompt_chatbot)
        return create_retrieval_chain(context_retriever, document_chain)

    def process_text_query(self, user_input):
        documents_retrieved = self.vectorDB.similarity_search(user_input, threshold=0.9)
        if not documents_retrieved:
            return "I don't have information on that. Can you specify another product or feature?"

        context = " ".join([doc.page_content for doc in documents_retrieved])
        result = self.conversation_chain.invoke({
            'input': user_input,
            'chat_history': self.memory.chat_memory.messages,
            'context': context
        })
        self.memory.save_context({'input': user_input}, {'result': result['answer']})
        return result['answer']
