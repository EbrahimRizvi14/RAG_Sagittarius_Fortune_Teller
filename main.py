from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class Chatbot():
    def __init__(self):
        loader = TextLoader('horoscope.txt')
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=20, separator="\n")
        docs = text_splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings()

        docsearch = FAISS.from_documents(docs, embeddings)
        retriever = docsearch.as_retriever(search_kwargs={"k": 2})

        llm = ChatGroq(model='groq/compound',
                     temperature=0,
                     max_tokens=120)


        template = """
            You are a mystical fortune teller.

            Answer the question using ONLY the provided context below. If you don't know the answer, just say that you do not know.
            Respond in exactly two complete sentences. No extra text.
            Do NOT create bullet points.
            Do NOT create numbered lists.
            Do NOT make up an answer.
            Do NOT repeat the question.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        self.rag_chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )


if __name__ == "__main__":
    bot = Chatbot()
    user_input = input("Ask me anything: ")
    result = bot.rag_chain.invoke(user_input)
    print(result.strip())