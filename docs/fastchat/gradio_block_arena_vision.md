# Overview

This file, gradio_block_arena_vision.py, defines functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### function `set_visible_image`
- **Description:** No docstring available.
- **Parameters:**
    - `textbox`: N/A

### function `set_invisible_image`
- **Description:** No docstring available.

### function `add_image`
- **Description:** No docstring available.
- **Parameters:**
    - `textbox`: N/A

### function `vote_last_response`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `vote_type`: N/A
    - `model_selector`: N/A
    - `request`: N/A

### function `upvote_last_response`
- **Description:** Input: [state, model_selector, sandbox_state],
Output: [textbox] + user_buttons,
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `sandbox_state`: N/A
    - `request`: N/A

### function `downvote_last_response`
- **Description:** Input: [state, model_selector, sandbox_state],
Output: [textbox] + user_buttons,
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `sandbox_state`: N/A
    - `request`: N/A

### function `flag_last_response`
- **Description:** Input: [state, model_selector, sandbox_state],
Output: [textbox] + user_buttons,
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `sandbox_state`: N/A
    - `request`: N/A

### function `regenerate`
- **Description:** Regenerate the chatbot response.

    regenerate,
    state,
    [state, chatbot, textbox] + user_buttons

    user_buttons: list[gr.Button] = [
        # send button
        send_btn,
        # regenerate button
        regenerate_btn,
        # vote buttons
        upvote_btn, downvote_btn, flag_btn,
        # clear button
        clear_btn,
    ]
- **Parameters:**
    - `state`: N/A
    - `sandbox_state`: N/A
    - `request`: N/A

### function `clear_history`
- **Description:** Clear the conversation history and reset the state.

    clear_history,
    sandbox_state,
    [state, chatbot, sandbox_state] + [multimodal_textbox, textbox] + user_buttons,

    user_buttons: list[gr.Button] = [
        # send button
        send_btn,
        # regenerate button
        regenerate_btn,
        # vote buttons
        upvote_btn, downvote_btn, flag_btn,
        # clear button
        clear_btn,
    ]
- **Parameters:**
    - `sandbox_state`: N/A
    - `request`: N/A

### function `report_csam_image`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `image`: N/A

### function `_prepare_text_with_image`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `text`: N/A
    - `images`: N/A
    - `csam_flag`: N/A

### function `convert_images_to_conversation_format`
- **Description:** No docstring available.
- **Parameters:**
    - `images`: N/A
- **Returns:** `list`

### function `moderate_input`
- **Description:** No docstring available.
- **Parameters:**
    - `state`: N/A
    - `text`: N/A
    - `all_conv_text`: N/A
    - `model_list`: N/A
    - `images`: N/A
    - `ip`: N/A

### function `add_text`
- **Description:** Add text to the chatbot state and update the chatbot UI.

    add_text,
    [state, model_selector, sandbox_state] + [multimodal_textbox, textbox], + [context_state],
    [state, chatbot, sandbox_state] + [multimodal_textbox, textbox] + user_buttons,
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `sandbox_state`: N/A
    - `multimodal_input`: N/A
    - `text_input`: N/A
    - `context`: N/A
    - `request`: N/A

### function `build_single_vision_language_model_ui`
- **Description:** No docstring available.
- **Parameters:**
    - `context`: N/A
    - `add_promotion_links`: N/A
    - `random_questions`: N/A

## Important Variables/Constants

- `MAX_NSFW_ENDPOINT_IMAGE_SIZE_IN_MB`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `USER_BUTTONS_LENGTH`: [Please describe the purpose of this constant. Verify if it's a true global constant.]

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
    - `fastchat.constants.IMAGE_MODERATION_MSG`
    - `fastchat.constants.INPUT_CHAR_LEN_LIMIT`
    - `fastchat.constants.MODERATION_MSG`
    - `fastchat.constants.SURVEY_LINK`
    - `fastchat.constants.TEXT_MODERATION_MSG`
    - `fastchat.model.model_adapter.get_conversation_template`
    - `fastchat.serve.chat_state.LOG_DIR`
    - `fastchat.serve.chat_state.ModelChatState`
    - `fastchat.serve.chat_state.save_log_to_local`
    - `fastchat.serve.gradio_global_state.Context`
    - `fastchat.serve.gradio_web_server.acknowledgment_md`
    - `fastchat.serve.gradio_web_server.bot_response`
    - `fastchat.serve.gradio_web_server.clear_sandbox_components`
    - `fastchat.serve.gradio_web_server.disable_btn`
    - `fastchat.serve.gradio_web_server.get_ip`
    - `fastchat.serve.gradio_web_server.get_model_description_md`
    - `fastchat.serve.gradio_web_server.get_remote_logger`
    - `fastchat.serve.gradio_web_server.set_chat_system_messages`
    - `fastchat.serve.gradio_web_server.update_system_prompt`
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
    - `fastchat.serve.sandbox.sandbox_state.ChatbotSandboxState`
    - `fastchat.serve.sandbox.sandbox_telemetry.log_sandbox_telemetry_gradio_fn`
    - `fastchat.serve.sandbox.sandbox_telemetry.save_conv_log_to_azure_storage`
    - `fastchat.serve.vision.image.Image`
    - `fastchat.serve.vision.image.ImageFormat`
    - `fastchat.utils.build_logger`
    - `fastchat.utils.image_moderation_filter`
    - `fastchat.utils.moderation_filter`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `base64`
    - `gradio`
    - `gradio.data_classes.FileData`
    - `gradio_sandboxcomponent.SandboxComponent`
    - `numpy`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
