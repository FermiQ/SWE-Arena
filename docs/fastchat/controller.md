# Overview

This file, controller.py, defines classes and functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### class `DispatchMethod`
- **Description:** No docstring available.
- **Methods:**
    - **`from_str`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `cls`: N/A
            - `name`: N/A

### class `WorkerInfo`
- **Description:** No docstring available.

### class `Controller`
- **Description:** No docstring available.
- **Methods:**
    - **`__init__`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `dispatch_method`: N/A
    - **`register_worker`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `worker_name`: N/A
            - `check_heart_beat`: N/A
            - `worker_status`: N/A
            - `multimodal`: N/A
    - **`get_worker_status`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `worker_name`: N/A
    - **`remove_worker`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `worker_name`: N/A
    - **`refresh_all_workers`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
    - **`list_models`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
    - **`list_multimodal_models`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
    - **`list_language_models`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
    - **`get_worker_address`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_name`: N/A
    - **`receive_heart_beat`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `worker_name`: N/A
            - `queue_length`: N/A
    - **`remove_stale_workers_by_expiration`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
    - **`handle_no_worker`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `params`: N/A
    - **`handle_worker_timeout`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `worker_address`: N/A
    - **`worker_api_get_status`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
    - **`worker_api_generate_stream`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `params`: N/A

### function `heart_beat_controller`
- **Description:** No docstring available.
- **Parameters:**
    - `controller`: N/A

### function `create_controller`
- **Description:** No docstring available.

### function `from_str`
- **Description:** No docstring available.
- **Parameters:**
    - `cls`: N/A
    - `name`: N/A

### function `__init__`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `dispatch_method`: N/A

### function `register_worker`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `worker_name`: N/A
    - `check_heart_beat`: N/A
    - `worker_status`: N/A
    - `multimodal`: N/A

### function `get_worker_status`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `worker_name`: N/A

### function `remove_worker`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `worker_name`: N/A

### function `refresh_all_workers`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A

### function `list_models`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A

### function `list_multimodal_models`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A

### function `list_language_models`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A

### function `get_worker_address`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_name`: N/A

### function `receive_heart_beat`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `worker_name`: N/A
    - `queue_length`: N/A

### function `remove_stale_workers_by_expiration`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A

### function `handle_no_worker`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `params`: N/A

### function `handle_worker_timeout`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `worker_address`: N/A

### function `worker_api_get_status`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A

### function `worker_api_generate_stream`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `params`: N/A

## Important Variables/Constants

- `LOTTERY`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `SHORTEST_QUEUE`: [Please describe the purpose of this constant. Verify if it's a true global constant.]

## Usage Examples

*Note: Usage examples are placeholders and may need to be manually added or refined based on the actual functionality of the file.*

```python
# Example usage (if applicable)
# import ...
# result = call_function(...)
```

## Dependencies and Interactions

- **Internal Dependencies:** (Imports from within the FastChat project)
    - `fastchat.constants.CONTROLLER_HEART_BEAT_EXPIRATION`
    - `fastchat.constants.ErrorCode`
    - `fastchat.constants.SERVER_ERROR_MSG`
    - `fastchat.constants.WORKER_API_TIMEOUT`
    - `fastchat.utils.build_logger`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `fastapi.FastAPI`
    - `fastapi.Request`
    - `fastapi.responses.StreamingResponse`
    - `numpy`
    - `requests`
    - `uvicorn`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
