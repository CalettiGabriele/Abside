from fastmcp import FastMCP
import asyncio
import sys
from pathlib import Path

# Add parent directory to path to import design_patterns_mcp
sys.path.insert(0, str(Path(__file__).parent.parent))

from design_patterns_mcp.main import design_patterns_mcp

# Define main server
main_mcp = FastMCP(name="Abside")

# Import subserver
async def setup():
    await main_mcp.import_server(design_patterns_mcp, prefix="design_patterns")

# Result: main_mcp now contains prefixed components from design_patterns_mcp
# - Tools, resources, and prompts with "design_patterns_" prefix 

if __name__ == "__main__":
    asyncio.run(setup())
    main_mcp.run()