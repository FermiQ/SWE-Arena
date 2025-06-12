import ast
import json
import os

def analyze_python_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    tree = ast.parse(content)

    docstrings = {}
    functions = []
    classes = []
    imports = []
    constants = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            params = [(arg.arg, None) for arg in node.args.args]
            returns = ast.get_docstring(node.returns) if hasattr(node, 'returns') and node.returns else None # Basic return annotation if available
            functions.append({
                "name": node.name,
                "docstring": docstring,
                "params": params,
                "returns": returns
            })
        elif isinstance(node, ast.ClassDef):
            docstring = ast.get_docstring(node)
            methods = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_docstring = ast.get_docstring(item)
                    method_params = [(arg.arg, None) for arg in item.args.args]
                    method_returns = ast.get_docstring(item.returns) if hasattr(item, 'returns') and item.returns else None
                    methods.append({
                        "name": item.name,
                        "docstring": method_docstring,
                        "params": method_params,
                        "returns": method_returns
                    })
            classes.append({
                "name": node.name,
                "docstring": docstring,
                "methods": methods
            })
        elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper(): # Basic check for constants
                    constants.append(target.id)

    # Simplified overview - could be improved with more sophisticated analysis
    overview = f"This file, {os.path.basename(filepath)}, appears to be responsible for [general purpose based on filename/content - placeholder]."
    if not functions and not classes:
        overview = f"This file, {os.path.basename(filepath)}, likely contains utility functions or scripts. Its primary purpose is [general purpose based on filename/content - placeholder]."
    elif functions and not classes:
        overview = f"This file, {os.path.basename(filepath)}, defines several functions related to [general purpose based on filename/content - placeholder]."
    elif classes and not functions:
        overview = f"This file, {os.path.basename(filepath)}, defines classes for [general purpose based on filename/content - placeholder]."
    elif classes and functions:
        overview = f"This file, {os.path.basename(filepath)}, defines both functions and classes for [general purpose based on filename/content - placeholder]."


    return {
        "overview": overview,
        "functions": functions,
        "classes": classes,
        "imports": sorted(list(set(imports))),
        "constants": sorted(list(set(constants)))
    }

def generate_markdown(analysis, filepath):
    filename = os.path.basename(filepath)
    markdown_content = f"# Overview\n\n{analysis['overview']}\n\n"

    if analysis["classes"]:
        markdown_content += "## Key Components\n\n"
        for c in analysis["classes"]:
            markdown_content += f"### class `{c['name']}`\n"
            markdown_content += f"- **Description:** {c['docstring'] or 'N/A'}\n"
            if c["methods"]:
                markdown_content += "- **Methods:**\n"
                for m in c["methods"]:
                    markdown_content += f"    - `{m['name']}`: {m['docstring'] or 'N/A'}\n"
                    if m['params']:
                        markdown_content += "        - **Parameters:**\n"
                        for p_name, p_desc in m['params']:
                             markdown_content += f"            - `{p_name}`: {p_desc or 'N/A'}\n"
                    if m['returns']:
                        markdown_content += f"        - **Returns:** {m['returns']}\n"
            markdown_content += "\n"

    if analysis["functions"]:
        if not analysis["classes"]: # Add Key Components header if not already added
             markdown_content += "## Key Components\n\n"
        for f in analysis["functions"]:
            markdown_content += f"### function `{f['name']}`\n"
            markdown_content += f"- **Description:** {f['docstring'] or 'N/A'}\n"
            if f['params']:
                markdown_content += "- **Parameters:**\n"
                for p_name, p_desc in f['params']:
                    markdown_content += f"    - `{p_name}`: {p_desc or 'N/A'}\n"
            if f['returns']:
                 markdown_content += f"- **Returns:** {f['returns']}\n"
            markdown_content += "\n"

    if analysis["constants"]:
        markdown_content += "## Important Variables/Constants\n\n"
        for const in analysis["constants"]:
            markdown_content += f"- `{const}`: [Description of the constant.]\n"
        markdown_content += "\n"

    markdown_content += "## Usage Examples\n\n"
    markdown_content += "*Note: Usage examples may need to be manually added or refined.*\n\n"

    markdown_content += "## Dependencies and Interactions\n\n"

    # Simplified: Listing imported names as internal/external based on common libraries
    internal_deps = [dep for dep in analysis["imports"] if dep.startswith("fastchat.") or dep.startswith(".")]
    external_deps = [dep for dep in analysis["imports"] if not (dep.startswith("fastchat.") or dep.startswith("."))]

    markdown_content += "- **Internal Dependencies:**\n"
    if internal_deps:
        for dep in internal_deps:
            markdown_content += f"    - {dep}\n"
    else:
        markdown_content += "    - N/A\n"

    markdown_content += "- **External Libraries:**\n"
    if external_deps:
        for dep in external_deps:
            markdown_content += f"    - {dep}\n"
    else:
        markdown_content += "    - N/A\n"

    markdown_content += "- **Interactions:**\n"
    markdown_content += "    - [Describe how this file interacts with other components of the system.]\n"

    return markdown_content

if __name__ == "__main__":
    python_file_path = "fastchat/llm_judge/clean_judgment.py" # This will be replaced by sed
    markdown_file_path = "docs/fastchat/clean_judgment.md" # This will be replaced by sed

    analysis_data = analyze_python_file(python_file_path)
    markdown_output = generate_markdown(analysis_data, python_file_path)

    with open(markdown_file_path, 'w') as f:
        f.write(markdown_output)

    print(f"Documentation generated for {python_file_path} at {markdown_file_path}")
