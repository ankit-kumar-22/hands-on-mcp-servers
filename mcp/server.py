from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("PersonalInfo")
# @mcp.tool()
# def reverse_string(text: str) -> str:
#     """Reverses the given string."""
#     return text[::-1]

# @mcp.tool()
# def count_words(text: str) -> int:
#     """Counts the number of words in a sentence."""
#     return len(text.split())

ABOUT_PATH = "/Users/ankitkumar/Downloads/hands-on-mcp-servers/shampoo.txt"

@mcp.tool()
def shampoo_available() -> str:
    """
    Give the Shampoo Stocks Available information
    """
    if not os.path.isfile(ABOUT_PATH):
        raise FileNotFoundError(f"File not found: {ABOUT_PATH}")
    with open(ABOUT_PATH, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    mcp.run(transport="stdio")