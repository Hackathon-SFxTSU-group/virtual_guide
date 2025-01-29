from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_gigachat import GigaChat
from langchain.chains import create_retrieval_chain

class QuestionAnsweringSystem:
    def __init__(self, faiss_index_path: str, gigachat_credentials: str = 'OWU0YzAxZTYtZGFiNC00NjZkLThmNTgtZjA0Nzc5NGY5MDcxOmIzOGE3ZTJmLWMwMjItNDc1My04MzFmLWRiMDhiODA3YTkxNQ=='):
        """
        Инициализация системы ответов на вопросы.

        :param faiss_index_path: Путь к FAISS-индексу.
        :param gigachat_credentials: Ключ доступа для GigaChat API.
        """
        # Загрузка модели для эмбеддингов
        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': False}
        )

        # Загрузка FAISS-индекса
        self.vector_store = FAISS.load_local(
            faiss_index_path,
            self.embedding,
            allow_dangerous_deserialization=True
        )

        # Создание ретривера
        self.embedding_retriever = self.vector_store.as_retriever(search_kwargs={"k": 5})

        # Инициализация GigaChat
        self.llm = GigaChat(
            credentials=gigachat_credentials,
            model='GigaChat:latest',
            verify_ssl_certs=False,
            profanity_check=False
        )

        # Создание промпта
        self.prompt = ChatPromptTemplate.from_template('''
            Ответь на вопрос пользователя. \
            Используй при этом только информацию из контекста. Если в контексте нет \
            информации для ответа, попробуй сам.
            Контекст: {context}
            Вопрос: {input}
            Ответ:
        ''')

        # Создание цепочки для обработки документов
        self.document_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.prompt
        )

        # Создание цепочки для поиска и ответа
        self.retrieval_chain = create_retrieval_chain(
            self.embedding_retriever,
            self.document_chain
        )

    def ask_question(self, question: str):
        """
        Задаёт вопрос системе и возвращает ответ.

        :param question: Вопрос пользователя.
        :return: Ответ системы.
        """
        # Вызов цепочки для получения ответа
        response = self.retrieval_chain.invoke({"input": question})
        return response["answer"]