"""
MCP Resources implementation.
This module contains all the resource definitions for the MCP server.
"""

import os
from pathlib import Path

def register_resources(mcp_server):
    """
    Register all resources with the MCP server.
    
    Args:
        mcp_server: The FastMCP server instance
    """
    
    # Get the resources directory path
    resources_dir = Path(__file__).parent / "resources"
    
    # Check if resources directory exists
    if not resources_dir.exists():
        print(f"Warning: Resources directory not found at {resources_dir}")
        return
    
    # Register each markdown file as a resource
    for md_file in resources_dir.glob("*.md"):
        # Create resource URI from filename (e.g., singleton.md -> design-patterns://singleton)
        resource_name = md_file.stem
        resource_uri = f"design-patterns://{resource_name}"
        
        # Create a closure to capture the file path
        def create_resource_handler(file_path):
            def handler() -> str:
                """Returns the content of the design pattern markdown file."""
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            return handler
        
        # Register the resource
        mcp_server.resource(resource_uri)(create_resource_handler(md_file))
