from RAG.vectorstore.ingestion import IngestionPipeline
from RAG.generation.rag_chain import RAGGenerator
import os


pipeline = None
generator = None

def run_generation():

    global pipeline, generator

    if generator is None:
        pipeline = IngestionPipeline(
        collection_name='github_issues_api_gen'
        )

        pipeline.ingest_url(
            url='https://docs.github.com/en/rest/issues/issues',
            api_name='github'
        )

        generator= RAGGenerator(
                            vector_store= pipeline.vector_store,
                            groq_api_key=os.getenv("GROQ_API_KEY")
                            )

        return generator


def generate_answer(question):

    gen = run_generation()
    return gen.generate(question)

