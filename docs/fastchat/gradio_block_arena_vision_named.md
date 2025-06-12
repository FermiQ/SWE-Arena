# Overview

This file, gradio_block_arena_vision_named.py, defines functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### function `load_demo_side_by_side_vision_named`
- **Description:** No docstring available.
- **Parameters:**
    - `context`: N/A

### function `clear_history_example`
- **Description:** No docstring available.
- **Parameters:**
    - `request`: N/A

### function `vote_last_response`
- **Description:** No docstring available.
- **Parameters:**
    - `state0`: N/A
    - `state1`: N/A
    - `model_selector0`: N/A
    - `model_selector1`: N/A
    - `named_feedback_details`: N/A
    - `request`: N/A

### function `regenerate_single`
- **Description:** Regenerate message for one side.
- **Parameters:**
    - `state`: N/A
    - `sandbox_state`: N/A
    - `request`: N/A

### function `regenerate_multi`
- **Description:** No docstring available.
- **Parameters:**
    - `state0`: N/A
    - `state1`: N/A
    - `sandbox_state0`: N/A
    - `sandbox_state1`: N/A
    - `request`: N/A

### function `clear_history`
- **Description:** Clear chat history for both sides.
- **Parameters:**
    - `sandbox_state0`: N/A
    - `sandbox_state1`: N/A
    - `request`: N/A
- **Returns:** `List`

### function `add_text_single`
- **Description:** Add text for one side.
- **Parameters:**
    - `state`: N/A
    - `model_selector`: N/A
    - `sandbox_state`: N/A
    - `multimodal_input`: N/A
    - `text_input`: N/A
    - `context`: N/A
    - `request`: N/A

### function `add_text_multi`
- **Description:** No docstring available.
- **Parameters:**
    - `state0`: N/A
    - `state1`: N/A
    - `model_selector0`: N/A
    - `model_selector1`: N/A
    - `sandbox_state0`: N/A
    - `sandbox_state1`: N/A
    - `multimodal_input`: N/A
    - `text_input`: N/A
    - `context`: N/A
    - `request`: N/A

### function `build_side_by_side_vision_ui_named`
- **Description:** No docstring available.
- **Parameters:**
    - `context`: N/A
    - `random_questions`: N/A

## Important Variables/Constants

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
    - `fastchat.constants.SLOW_MODEL_MSG`
    - `fastchat.constants.SURVEY_LINK`
    - `fastchat.constants.TEXT_MODERATION_MSG`
    - `fastchat.model.model_adapter.get_conversation_template`
    - `fastchat.serve.chat_state.LOG_DIR`
    - `fastchat.serve.chat_state.ModelChatState`
    - `fastchat.serve.chat_state.save_log_to_local`
    - `fastchat.serve.gradio_block_arena_named.bot_response_multi`
    - `fastchat.serve.gradio_block_arena_named.clear_sandbox_components`
    - `fastchat.serve.gradio_block_arena_named.flash_buttons`
    - `fastchat.serve.gradio_block_arena_named.set_chat_system_messages_multi`
    - `fastchat.serve.gradio_block_arena_named.share_click`
    - `fastchat.serve.gradio_block_arena_vision._prepare_text_with_image`
    - `fastchat.serve.gradio_block_arena_vision.add_image`
    - `fastchat.serve.gradio_block_arena_vision.convert_images_to_conversation_format`
    - `fastchat.serve.gradio_block_arena_vision.disable_multimodal`
    - `fastchat.serve.gradio_block_arena_vision.enable_multimodal`
    - `fastchat.serve.gradio_block_arena_vision.invisible_btn`
    - `fastchat.serve.gradio_block_arena_vision.invisible_text`
    - `fastchat.serve.gradio_block_arena_vision.moderate_input`
    - `fastchat.serve.gradio_block_arena_vision.set_invisible_image`
    - `fastchat.serve.gradio_block_arena_vision.set_visible_image`
    - `fastchat.serve.gradio_block_arena_vision.visible_text`
    - `fastchat.serve.gradio_global_state.Context`
    - `fastchat.serve.gradio_web_server.acknowledgment_md`
    - `fastchat.serve.gradio_web_server.bot_response`
    - `fastchat.serve.gradio_web_server.disable_btn`
    - `fastchat.serve.gradio_web_server.disable_text`
    - `fastchat.serve.gradio_web_server.enable_btn`
    - `fastchat.serve.gradio_web_server.enable_text`
    - `fastchat.serve.gradio_web_server.get_ip`
    - `fastchat.serve.gradio_web_server.get_model_description_md`
    - `fastchat.serve.gradio_web_server.invisible_btn`
    - `fastchat.serve.gradio_web_server.no_change_btn`
    - `fastchat.serve.gradio_web_server.set_chat_system_messages`
    - `fastchat.serve.remote_logger.get_remote_logger`
    - `fastchat.serve.sandbox.code_analyzer.SandboxEnvironment`
    - `fastchat.serve.sandbox.code_runner.DEFAULT_SANDBOX_INSTRUCTIONS`
    - `fastchat.serve.sandbox.code_runner.SUPPORTED_SANDBOX_ENVIRONMENTS`
    - `fastchat.serve.sandbox.code_runner.create_chatbot_sandbox_state`
    - `fastchat.serve.sandbox.code_runner.on_click_code_message_run`
    - `fastchat.serve.sandbox.code_runner.on_edit_code`
    - `fastchat.serve.sandbox.code_runner.on_edit_dependency`
    - `fastchat.serve.sandbox.code_runner.reset_sandbox_state`
    - `fastchat.serve.sandbox.code_runner.set_sandbox_state_ids`
    - `fastchat.serve.sandbox.code_runner.update_sandbox_config_multi`
    - `fastchat.serve.sandbox.code_runner.update_sandbox_state_system_prompt`
    - `fastchat.serve.sandbox.sandbox_state.ChatbotSandboxState`
    - `fastchat.serve.sandbox.sandbox_telemetry.log_sandbox_telemetry_gradio_fn`
    - `fastchat.serve.sandbox.sandbox_telemetry.save_conv_log_to_azure_storage`
    - `fastchat.utils.build_logger`
    - `fastchat.utils.image_moderation_filter`
    - `fastchat.utils.moderation_filter`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `gradio`
    - `gradio_sandboxcomponent.SandboxComponent`
    - `numpy`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
