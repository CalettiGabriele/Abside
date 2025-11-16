from fastmcp import FastMCP
from .tools import register_tools
from .resources import register_resources
from .prompts import register_prompts

# Define MCP server
design_patterns_mcp = FastMCP(name="DesignPatterns")

# Register tools, resources, and prompts
register_tools(design_patterns_mcp)
register_resources(design_patterns_mcp)
register_prompts(design_patterns_mcp)

if __name__ == "__main__":
    design_patterns_mcp.run()