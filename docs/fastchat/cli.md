# Overview

This file, cli.py, defines classes and functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### class `SimpleChatIO`
- **Description:** No docstring available.
- **Methods:**
    - **`__init__`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `multiline`: N/A
    - **`prompt_for_input`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `role`: N/A
        - **Returns:** `str`
    - **`prompt_for_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `role`: N/A
    - **`stream_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `output_stream`: N/A
    - **`print_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `text`: N/A

### class `RichChatIO`
- **Description:** No docstring available.
- **Methods:**
    - **`_`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `event`: N/A
    - **`__init__`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `multiline`: N/A
            - `mouse`: N/A
    - **`prompt_for_input`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `role`: N/A
        - **Returns:** `str`
    - **`prompt_for_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `role`: N/A
    - **`stream_output`**
        - **Description:** Stream output from a role.
        - **Parameters:**
            - `self`: N/A
            - `output_stream`: N/A
    - **`print_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `text`: N/A

### class `ProgrammaticChatIO`
- **Description:** No docstring available.
- **Methods:**
    - **`prompt_for_input`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `role`: N/A
        - **Returns:** `str`
    - **`prompt_for_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `role`: N/A
    - **`stream_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `output_stream`: N/A
    - **`print_output`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `text`: N/A

### function `main`
- **Description:** No docstring available.
- **Parameters:**
    - `args`: N/A

### function `__init__`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `multiline`: N/A

### function `prompt_for_input`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `role`: N/A
- **Returns:** `str`

### function `prompt_for_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `role`: N/A

### function `stream_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `output_stream`: N/A

### function `print_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `text`: N/A

### function `_`
- **Description:** No docstring available.
- **Parameters:**
    - `event`: N/A

### function `__init__`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `multiline`: N/A
    - `mouse`: N/A

### function `prompt_for_input`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `role`: N/A
- **Returns:** `str`

### function `prompt_for_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `role`: N/A

### function `stream_output`
- **Description:** Stream output from a role.
- **Parameters:**
    - `self`: N/A
    - `output_stream`: N/A

### function `print_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `text`: N/A

### function `prompt_for_input`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `role`: N/A
- **Returns:** `str`

### function `prompt_for_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `role`: N/A

### function `stream_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `output_stream`: N/A

### function `print_output`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `text`: N/A

## Usage Examples

*Note: Usage examples are placeholders and may need to be manually added or refined based on the actual functionality of the file.*

```python
# Example usage (if applicable)
# import ...
# result = call_function(...)
```

## Dependencies and Interactions

- **Internal Dependencies:** (Imports from within the FastChat project)
    - `fastchat.model.model_adapter.add_model_args`
    - `fastchat.modules.awq.AWQConfig`
    - `fastchat.modules.exllama.ExllamaConfig`
    - `fastchat.modules.gptq.GptqConfig`
    - `fastchat.modules.xfastertransformer.XftConfig`
    - `fastchat.serve.inference.ChatIO`
    - `fastchat.serve.inference.chat_loop`
    - `fastchat.utils.str_to_torch_dtype`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `prompt_toolkit.PromptSession`
    - `prompt_toolkit.auto_suggest.AutoSuggestFromHistory`
    - `prompt_toolkit.completion.WordCompleter`
    - `prompt_toolkit.history.InMemoryHistory`
    - `prompt_toolkit.key_binding.KeyBindings`
    - `rich.console.Console`
    - `rich.live.Live`
    - `rich.markdown.Markdown`
    - `torch`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
