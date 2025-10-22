"""Entry point for MCP Chat application."""

from src.mcp_chat.main import main
import asyncio
import sys

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
