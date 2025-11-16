"""
MCP Tools implementation.
This module contains all the tool definitions for the MCP server.
"""

from typing import Optional, List

def register_tools(mcp_server):
    """
    Register all tools with the MCP server.
    
    Args:
        mcp_server: The FastMCP server instance
    """
    
    @mcp_server.tool
    def ask_user(
        question: str,
        context: Optional[str] = None,
        default_answer: Optional[str] = None
    ) -> dict:
        """
        Ask the user for clarification or additional context (Human-in-the-Loop).
        
        This tool enables the LLM to request human input when:
        - Requirements are ambiguous or unclear
        - Additional context is needed to proceed
        - User preferences or decisions are required
        - Validation of intermediate results is needed
        
        Args:
            question: The question to ask the user
            context: Optional context or background information to help the user understand the question
            default_answer: Optional default answer to suggest to the user
            
        Returns:
            dict: Contains the user's response and metadata
        """
        print("\n" + "="*80)
        print("🤖 AI ASSISTANT NEEDS YOUR INPUT")
        print("="*80)
        
        if context:
            print(f"\n📋 Context:\n{context}\n")
        
        print(f"❓ Question:\n{question}\n")
        
        if default_answer:
            print(f"💡 Suggested answer: {default_answer}")
            prompt = f"Your answer (press Enter for default): "
        else:
            prompt = "Your answer: "
        
        try:
            user_response = input(prompt).strip()
            
            # Use default if user pressed Enter without typing
            if not user_response and default_answer:
                user_response = default_answer
                print(f"✓ Using default: {user_response}")
            
            print("="*80 + "\n")
            
            return {
                "success": True,
                "question": question,
                "answer": user_response,
                "used_default": not user_response and default_answer is not None
            }
            
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  User cancelled the input request\n")
            return {
                "success": False,
                "question": question,
                "answer": None,
                "error": "User cancelled the input request"
            }
    
    @mcp_server.tool
    def ask_user_choice(
        question: str,
        choices: List[str],
        context: Optional[str] = None,
        allow_multiple: bool = False
    ) -> dict:
        """
        Ask the user to choose from a list of options (Human-in-the-Loop).
        
        This tool enables the LLM to present multiple options and get user selection when:
        - Multiple valid alternatives exist
        - User preference is needed between options
        - Decision points require human judgment
        
        Args:
            question: The question to ask the user
            choices: List of available options
            context: Optional context or background information
            allow_multiple: Whether to allow multiple selections (default: False)
            
        Returns:
            dict: Contains the user's selected choice(s) and metadata
        """
        print("\n" + "="*80)
        print("🤖 AI ASSISTANT NEEDS YOUR CHOICE")
        print("="*80)
        
        if context:
            print(f"\n📋 Context:\n{context}\n")
        
        print(f"❓ Question:\n{question}\n")
        print("📝 Available options:")
        
        for idx, choice in enumerate(choices, 1):
            print(f"  {idx}. {choice}")
        
        if allow_multiple:
            prompt = "\nYour choice(s) (comma-separated numbers, e.g., 1,3): "
        else:
            prompt = "\nYour choice (enter number): "
        
        try:
            user_input = input(prompt).strip()
            
            if allow_multiple:
                # Parse multiple selections
                selected_indices = [int(x.strip()) for x in user_input.split(",")]
                selected_choices = [choices[i-1] for i in selected_indices if 1 <= i <= len(choices)]
            else:
                # Single selection
                selected_index = int(user_input)
                if 1 <= selected_index <= len(choices):
                    selected_choices = [choices[selected_index - 1]]
                else:
                    raise ValueError("Invalid choice number")
            
            print(f"✓ Selected: {', '.join(selected_choices)}")
            print("="*80 + "\n")
            
            return {
                "success": True,
                "question": question,
                "selected": selected_choices if allow_multiple else selected_choices[0],
                "all_choices": choices
            }
            
        except (ValueError, IndexError) as e:
            print(f"\n⚠️  Invalid selection: {e}\n")
            return {
                "success": False,
                "question": question,
                "selected": None,
                "error": f"Invalid selection: {str(e)}"
            }
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  User cancelled the choice request\n")
            return {
                "success": False,
                "question": question,
                "selected": None,
                "error": "User cancelled the choice request"
            }
    
    @mcp_server.tool
    def confirm_action(
        action: str,
        details: Optional[str] = None,
        warning: Optional[str] = None
    ) -> dict:
        """
        Ask the user to confirm an action before proceeding (Human-in-the-Loop).
        
        This tool enables the LLM to get explicit user confirmation when:
        - About to perform potentially destructive operations
        - Making significant changes that cannot be easily undone
        - Executing sensitive or critical actions
        
        Args:
            action: Description of the action to be confirmed
            details: Optional additional details about the action
            warning: Optional warning message about potential consequences
            
        Returns:
            dict: Contains whether the user confirmed and metadata
        """
        print("\n" + "="*80)
        print("⚠️  CONFIRMATION REQUIRED")
        print("="*80)
        
        print(f"\n🎯 Action:\n{action}\n")
        
        if details:
            print(f"📋 Details:\n{details}\n")
        
        if warning:
            print(f"⚠️  Warning:\n{warning}\n")
        
        try:
            response = input("Do you want to proceed? (yes/no): ").strip().lower()
            confirmed = response in ['yes', 'y']
            
            if confirmed:
                print("✓ Action confirmed")
            else:
                print("✗ Action cancelled")
            
            print("="*80 + "\n")
            
            return {
                "success": True,
                "action": action,
                "confirmed": confirmed
            }
            
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  User cancelled the confirmation request\n")
            return {
                "success": False,
                "action": action,
                "confirmed": False,
                "error": "User cancelled the confirmation request"
            }
