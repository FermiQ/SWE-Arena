# Overview

This file, common.py, defines classes and functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### class `Judge`
- **Description:** No docstring available.

### class `MatchSingle`
- **Description:** No docstring available.

### class `MatchPair`
- **Description:** No docstring available.

### function `load_questions`
- **Description:** Load questions from a file.
- **Parameters:**
    - `question_file`: N/A
    - `begin`: N/A
    - `end`: N/A

### function `load_model_answers`
- **Description:** Load model answers.

The return value is a python dict of type:
Dict[model_name: str -> Dict[question_id: int -> answer: dict]]
- **Parameters:**
    - `answer_dir`: N/A

### function `load_judge_prompts`
- **Description:** Load judge prompts.

The return value is a python dict of type:
Dict[judge_name: str -> dict]
- **Parameters:**
    - `prompt_file`: N/A

### function `run_judge_single`
- **Description:** No docstring available.
- **Parameters:**
    - `question`: N/A
    - `answer`: N/A
    - `judge`: N/A
    - `ref_answer`: N/A
    - `multi_turn`: N/A

### function `play_a_match_single`
- **Description:** No docstring available.
- **Parameters:**
    - `match`: N/A
    - `output_file`: N/A

### function `run_judge_pair`
- **Description:** No docstring available.
- **Parameters:**
    - `question`: N/A
    - `answer_a`: N/A
    - `answer_b`: N/A
    - `judge`: N/A
    - `ref_answer`: N/A
    - `multi_turn`: N/A

### function `play_a_match_pair`
- **Description:** No docstring available.
- **Parameters:**
    - `match`: N/A
    - `output_file`: N/A

### function `chat_completion_openai`
- **Description:** No docstring available.
- **Parameters:**
    - `model`: N/A
    - `conv`: N/A
    - `temperature`: N/A
    - `max_tokens`: N/A
    - `api_dict`: N/A

### function `chat_completion_openai_azure`
- **Description:** No docstring available.
- **Parameters:**
    - `model`: N/A
    - `conv`: N/A
    - `temperature`: N/A
    - `max_tokens`: N/A
    - `api_dict`: N/A

### function `chat_completion_anthropic`
- **Description:** No docstring available.
- **Parameters:**
    - `model`: N/A
    - `conv`: N/A
    - `temperature`: N/A
    - `max_tokens`: N/A
    - `api_dict`: N/A

### function `chat_completion_palm`
- **Description:** No docstring available.
- **Parameters:**
    - `chat_state`: N/A
    - `model`: N/A
    - `conv`: N/A
    - `temperature`: N/A
    - `max_tokens`: N/A

### function `normalize_game_key_single`
- **Description:** Make the model names sorted in a game key.
- **Parameters:**
    - `gamekey`: N/A
    - `result`: N/A

### function `normalize_game_key_dict`
- **Description:** Make the model names sorted in the game keys.
- **Parameters:**
    - `judgment_dict`: N/A

### function `load_pairwise_model_judgments`
- **Description:** Load model judgments.

The return value is a dict of type:
Dict[judge: Tuple -> Dict[game_key: tuple -> game_result: dict]
- **Parameters:**
    - `filename`: N/A

### function `load_single_model_judgments`
- **Description:** Load model judgments.

The return value is a dict of type:
Dict[judge: Tuple -> Dict[game_key: tuple -> game_result: dict]
- **Parameters:**
    - `filename`: N/A

### function `resolve_pairwise_judgment_dict`
- **Description:** Return the correct pairwise judge.
- **Parameters:**
    - `question`: N/A
    - `model_judgments_normal`: N/A
    - `model_judgments_math`: N/A
    - `multi_turn`: N/A

### function `resolve_single_judgment_dict`
- **Description:** Return the correct single answer grading judge.
- **Parameters:**
    - `question`: N/A
    - `model_judgments_normal`: N/A
    - `model_judgments_math`: N/A
    - `multi_turn`: N/A

### function `get_pairwise_judge_explanation`
- **Description:** Get model judge explanation.
- **Parameters:**
    - `gamekey`: N/A
    - `judgment_dict`: N/A

### function `get_single_judge_explanation`
- **Description:** Get model judge explanation.
- **Parameters:**
    - `gamekey`: N/A
    - `judgment_dict`: N/A

### function `check_data`
- **Description:** No docstring available.
- **Parameters:**
    - `questions`: N/A
    - `model_answers`: N/A
    - `ref_answers`: N/A
    - `models`: N/A
    - `judges`: N/A

### function `get_model_list`
- **Description:** No docstring available.
- **Parameters:**
    - `answer_dir`: N/A

## Important Variables/Constants

- `API_ERROR_OUTPUT`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `API_MAX_RETRY`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `API_RETRY_SLEEP`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `NEED_REF_CATS`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `TIE_DELTA`: [Please describe the purpose of this constant. Verify if it's a true global constant.]

## Usage Examples

*Note: Usage examples are placeholders and may need to be manually added or refined based on the actual functionality of the file.*

```python
# Example usage (if applicable)
# import ...
# result = call_function(...)
```

## Dependencies and Interactions

- **Internal Dependencies:** (Imports from within the FastChat project)
    - `fastchat.model.model_adapter.ANTHROPIC_MODEL_LIST`
    - `fastchat.model.model_adapter.OPENAI_MODEL_LIST`
    - `fastchat.model.model_adapter.get_conversation_template`
    - `fastchat.serve.api_provider.init_palm_chat`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `anthropic`
    - `openai`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
