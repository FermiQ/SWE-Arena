# Overview

This file, gradio_web_server.py, defines functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### function `set_global_vars`
- **Description:** No docstring available.
- **Parameters:**
    - `controller_url_`: N/A
    - `enable_moderation_`: N/A
    - `use_remote_storage_`: N/A

### function `get_model_list`
- **Description:** No docstring available.
- **Parameters:**
    - `controller_url`: N/A
    - `register_api_endpoint_file`: N/A
    - `vision_arena`: N/A

### function `load_demo_single`
- **Description:** No docstring available.
- **Parameters:**
    - `context`: N/A
    - `query_params`: N/A

### function `load_demo`
- **Description:** No docstring available.
- **Parameters:**
    - `url_params`: N/A
    - `request`: N/A

### function `vote_last_response`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `vote_type`: N/A
    - `model_selector`: N/A
    - `request`: N/A

### function `upvote_last_response`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `request`: N/A

### function `downvote_last_response`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `request`: N/A

### function `flag_last_response`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `request`: N/A

### function `regenerate`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `request`: N/A

### function `clear_history`
- **Description:** Clear the conversation history and reset the state.
- **Parameters:**
    - `sandbox_state`: N/A
    - `request`: N/A

### function `clear_sandbox_components`
- **Description:** No docstring available.

### function `get_ip`
- **Description:** No docstring available.
- **Parameters:**
    - `request`: N/A

### function `set_chat_system_messages`
- **Description:** Add sandbox instructions to the system message.
- **Parameters:**
    - `state`: N/A
    - `sandbox_state`: N/A
    - `model_selector`: N/A

### function `update_system_prompt`
- **Description:** TODO: Rewrite the code
- **Parameters:**
    - `system_prompt`: N/A
    - `sandbox_state`: N/A

### function `add_text`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `sandbox_state`: N/A
    - `text`: N/A
    - `request`: N/A

### function `model_worker_stream_iter`
- **Description:** No docstring available.
- **Parameters:**
    - `conv`: N/A
    - `model_name`: N/A
    - `worker_addr`: N/A
    - `prompt`: N/A
    - `temperature`: N/A
    - `repetition_penalty`: N/A
    - `top_p`: N/A
    - `max_new_tokens`: N/A
    - `images`: N/A

### function `is_limit_reached`
- **Description:** No docstring available.
- **Parameters:**
    - `model_name`: N/A
    - `ip`: N/A

### function `bot_response`
- **Description:** The main function for generating responses from the model.
- **Parameters:**
    - `state`: N/A
    - `temperature`: N/A
    - `top_p`: N/A
    - `max_new_tokens`: N/A
    - `sandbox_state`: N/A
    - `request`: N/A
    - `apply_rate_limit`: N/A
    - `use_recommended_config`: N/A

### function `get_model_description_md`
- **Description:** No docstring available.
- **Parameters:**
    - `models`: N/A

### function `build_about`
- **Description:** No docstring available.

### function `build_single_model_ui`
- **Description:** No docstring available.
- **Parameters:**
    - `models`: N/A
    - `add_promotion_links`: N/A

### function `build_demo`
- **Description:** No docstring available.
- **Parameters:**
    - `models`: N/A

## Usage Examples

*Note: Usage examples are placeholders and may need to be manually added or refined based on the actual functionality of the file.*

```python
# Example usage (if applicable)
# import ...
# result = call_function(...)
```

## Dependencies and Interactions

- **Internal Dependencies:** (Imports from within the FastChat project)
    - `fastchat.constants.CONVERSATION_LIMIT_MSG`
    - `fastchat.constants.CONVERSATION_TURN_LIMIT`
    - `fastchat.constants.ErrorCode`
    - `fastchat.constants.INPUT_CHAR_LEN_LIMIT`
    - `fastchat.constants.MODERATION_MSG`
    - `fastchat.constants.RATE_LIMIT_MSG`
    - `fastchat.constants.SERVER_ERROR_MSG`
    - `fastchat.constants.SESSION_EXPIRATION_TIME`
    - `fastchat.constants.SURVEY_LINK`
    - `fastchat.constants.WORKER_API_TIMEOUT`
    - `fastchat.conversation.Conversation`
    - `fastchat.model.model_registry.get_model_info`
    - `fastchat.model.model_registry.model_info`
    - `fastchat.serve.api_provider.get_api_provider_stream_iter`
    - `fastchat.serve.chat_state.LOG_DIR`
    - `fastchat.serve.chat_state.ModelChatState`
    - `fastchat.serve.chat_state.save_log_to_local`
    - `fastchat.serve.gradio_global_state.Context`
    - `fastchat.serve.remote_logger.get_remote_logger`
    - `fastchat.serve.sandbox.code_analyzer.SandboxEnvironment`
    - `fastchat.serve.sandbox.code_runner.DEFAULT_SANDBOX_INSTRUCTIONS`
    - `fastchat.serve.sandbox.code_runner.RUN_CODE_BUTTON_HTML`
    - `fastchat.serve.sandbox.code_runner.SUPPORTED_SANDBOX_ENVIRONMENTS`
    - `fastchat.serve.sandbox.code_runner.SandboxEnvironment`
    - `fastchat.serve.sandbox.code_runner.SandboxGradioSandboxComponents`
    - `fastchat.serve.sandbox.code_runner.create_chatbot_sandbox_state`
    - `fastchat.serve.sandbox.code_runner.on_click_code_message_run`
    - `fastchat.serve.sandbox.code_runner.on_edit_code`
    - `fastchat.serve.sandbox.code_runner.on_edit_dependency`
    - `fastchat.serve.sandbox.code_runner.reset_sandbox_state`
    - `fastchat.serve.sandbox.code_runner.set_sandbox_state_ids`
    - `fastchat.serve.sandbox.code_runner.update_sandbox_config`
    - `fastchat.serve.sandbox.code_runner.update_sandbox_state_system_prompt`
    - `fastchat.serve.sandbox.code_runner.update_visibility_for_single_model`
    - `fastchat.serve.sandbox.sandbox_state.ChatbotSandboxState`
    - `fastchat.serve.sandbox.sandbox_telemetry.log_sandbox_telemetry_gradio_fn`
    - `fastchat.serve.sandbox.sandbox_telemetry.save_conv_log_to_azure_storage`
    - `fastchat.utils.build_logger`
    - `fastchat.utils.get_window_url_params_js`
    - `fastchat.utils.get_window_url_params_with_tos_js`
    - `fastchat.utils.load_image`
    - `fastchat.utils.moderation_filter`
    - `fastchat.utils.parse_gradio_auth_creds`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `gradio`
    - `gradio_sandboxcomponent.SandboxComponent`
    - `hashlib`
    - `json5`
    - `requests`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
