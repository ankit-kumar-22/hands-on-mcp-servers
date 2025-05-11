from mcp.server.fastmcp import FastMCP
import os

# 1. Initialize your FastMCP server
mcp = FastMCP("PersonalInformation")

# 2. Hard-coded path to your file
ABOUT_PATH = "/Users/ankitkumar/Downloads/hands-on-mcp-servers/about_me.txt"

# 3. Define the prompt using @mcp.prompt()
@mcp.prompt(
    name="personal_information",
    description="Give all the personal information about the user"
)
def personal_information() -> str:
    """
    Give all the personal information about the user
    """
    if not os.path.isfile(ABOUT_PATH):
        raise FileNotFoundError(f"File not found: {ABOUT_PATH}")
    with open(ABOUT_PATH, "r", encoding="utf-8") as f:
        return f.read()

# 4. Run your server (default: stdio transport)
if __name__ == "__main__":
    mcp.run(transport="stdio")
