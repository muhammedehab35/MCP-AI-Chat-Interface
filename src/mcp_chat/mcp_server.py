from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc
@mcp.tool(
    name="read_doc",
    description="Read a content of a document and return it as a string.",
)
def read_doc(doc_name: str) -> str: 
    """Read a document from the file system."""
    doc = docs.get(doc_name)
    if not doc:
        raise Exception(f"Document '{doc_name}' not found")
    return doc


# TODO: Write a tool to edit a doc
@mcp.tool(
    name="edit_doc",
    description="Edit a document by replacing a string in the documents content with a new string.",
)
def edit_doc(doc_name: str, old_string: str, new_string: str) -> str:
    """Edit a document by replacing a string in the documents content with a new string."""
    doc = docs.get(doc_name) 
    if not doc:
        raise Exception(f"Document '{doc_name}' not found")
    return doc.replace(old_string, new_string)


# TODO: Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json",
   
)
def get_doc_ids() -> list[str]:
    """Get a list of all document ids."""
    return list(docs.keys())
# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def get_doc_content(doc_id: str) -> str:
    if doc_id not in docs:
        raise Exception(f"Document '{doc_id}' not found")
    return docs[doc_id] 

# Prompt to rewrite a document in markdown format
@mcp.prompt(
    name="rewrite_markdown",
    description="Rewrite a document in clean markdown format",
)
def rewrite_markdown_prompt(doc_id: str) -> list[dict]:
    """Generate a prompt to rewrite a document in markdown format."""
    doc_content = docs.get(doc_id)
    if not doc_content:
        raise Exception(f"Document '{doc_id}' not found")

    return [
        {
            "role": "user",
            "content": {
                "type": "text",
                "text": f"""Please rewrite the following document in clean, well-structured markdown format:

<document id="{doc_id}">
{doc_content}
</document>

Format the output with:
- Proper headings (# ## ###)
- Bullet points where appropriate
- Bold and italic emphasis where needed
- Code blocks if applicable
- Tables if data is structured

Preserve all important information while improving readability."""
            }
        }
    ]


# Prompt to summarize a document
@mcp.prompt(
    name="summarize",
    description="Generate a concise summary of a document",
)
def summarize_prompt(doc_id: str) -> list[dict]:
    """Generate a prompt to summarize a document."""
    doc_content = docs.get(doc_id)
    if not doc_content:
        raise Exception(f"Document '{doc_id}' not found")

    return [
        {
            "role": "user",
            "content": {
                "type": "text",
                "text": f"""Please provide a concise summary of the following document:

<document id="{doc_id}">
{doc_content}
</document>

Include:
- Main topic or purpose
- Key points (3-5 bullet points)
- Important details or conclusions
- Any action items if applicable

Keep the summary brief but comprehensive."""
            }
        }
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")
