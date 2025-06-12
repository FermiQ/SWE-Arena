# Overview

This file, openai_api_server.py, defines classes and functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### class `AppSettings`
- **Description:** No docstring available.

### function `create_error_response`
- **Description:** No docstring available.
- **Parameters:**
    - `code`: N/A
    - `message`: N/A
- **Returns:** `JSONResponse`

### function `check_requests`
- **Description:** No docstring available.
- **Parameters:**
    - `request`: N/A
- **Returns:** `Optional`

### function `process_input`
- **Description:** No docstring available.
- **Parameters:**
    - `model_name`: N/A
    - `inp`: N/A

### function `create_openai_logprobs`
- **Description:** Create OpenAI-style logprobs.
- **Parameters:**
    - `logprob_dict`: N/A

### function `_add_to_set`
- **Description:** No docstring available.
- **Parameters:**
    - `s`: N/A
    - `new_stop`: N/A

### function `create_openai_api_server`
- **Description:** No docstring available.

## Usage Examples

*Note: Usage examples are placeholders and may need to be manually added or refined based on the actual functionality of the file.*

```python
# Example usage (if applicable)
# import ...
# result = call_function(...)
```

## Dependencies and Interactions

- **Internal Dependencies:** (Imports from within the FastChat project)
    - `fastchat.constants.ErrorCode`
    - `fastchat.constants.WORKER_API_EMBEDDING_BATCH_SIZE`
    - `fastchat.constants.WORKER_API_TIMEOUT`
    - `fastchat.conversation.Conversation`
    - `fastchat.conversation.SeparatorStyle`
    - `fastchat.protocol.api_protocol.APIChatCompletionRequest`
    - `fastchat.protocol.api_protocol.APITokenCheckRequest`
    - `fastchat.protocol.api_protocol.APITokenCheckResponse`
    - `fastchat.protocol.api_protocol.APITokenCheckResponseItem`
    - `fastchat.protocol.openai_api_protocol.ChatCompletionRequest`
    - `fastchat.protocol.openai_api_protocol.ChatCompletionResponse`
    - `fastchat.protocol.openai_api_protocol.ChatCompletionResponseChoice`
    - `fastchat.protocol.openai_api_protocol.ChatCompletionResponseStreamChoice`
    - `fastchat.protocol.openai_api_protocol.ChatCompletionStreamResponse`
    - `fastchat.protocol.openai_api_protocol.ChatMessage`
    - `fastchat.protocol.openai_api_protocol.CompletionRequest`
    - `fastchat.protocol.openai_api_protocol.CompletionResponse`
    - `fastchat.protocol.openai_api_protocol.CompletionResponseChoice`
    - `fastchat.protocol.openai_api_protocol.CompletionResponseStreamChoice`
    - `fastchat.protocol.openai_api_protocol.CompletionStreamResponse`
    - `fastchat.protocol.openai_api_protocol.DeltaMessage`
    - `fastchat.protocol.openai_api_protocol.EmbeddingsRequest`
    - `fastchat.protocol.openai_api_protocol.EmbeddingsResponse`
    - `fastchat.protocol.openai_api_protocol.ErrorResponse`
    - `fastchat.protocol.openai_api_protocol.LogProbs`
    - `fastchat.protocol.openai_api_protocol.ModelCard`
    - `fastchat.protocol.openai_api_protocol.ModelList`
    - `fastchat.protocol.openai_api_protocol.ModelPermission`
    - `fastchat.protocol.openai_api_protocol.UsageInfo`
    - `fastchat.utils.build_logger`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `aiohttp`
    - `fastapi`
    - `fastapi.Depends`
    - `fastapi.HTTPException`
    - `fastapi.exceptions.RequestValidationError`
    - `fastapi.middleware.cors.CORSMiddleware`
    - `fastapi.responses.JSONResponse`
    - `fastapi.responses.StreamingResponse`
    - `fastapi.security.http.HTTPAuthorizationCredentials`
    - `fastapi.security.http.HTTPBearer`
    - `httpx`
    - `pydantic_settings.BaseSettings`
    - `shortuuid`
    - `tiktoken`
    - `uvicorn`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
