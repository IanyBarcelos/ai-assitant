import numexpr
from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun


@tool
def calculator(expression: str) -> str:
    """
    Performs numerical calculations.
    The input must be a simple mathematical expression, Eg: '2 + 2' or '3 * 5'.
    """
    try:
        expression = expression.replace("=", "").strip()
        result = numexpr.evaluate(expression).item()
        return str(result)
    except Exception as e:
        return f"Error in calculations: {e}"
    
# @tool
# def search_answer(query: str) -> str:
#     """
#     Searches Wikipedia for a summary of a topic.
#     Use this tool ONLY when the user explicitly agrees to a search or asks for details.
#     """
#     api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
#     wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
#     return wiki_tool.invoke(query)

available_tools = [calculator]