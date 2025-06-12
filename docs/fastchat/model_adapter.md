# Overview

This file, model_adapter.py, defines classes and functions for [general purpose - placeholder].
*This is an auto-generated overview. Please refine it manually.*

## Key Components

### class `BaseModelAdapter`
- **Description:** The base and the default model adapter.
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`load_compress_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `device`: N/A
            - `torch_dtype`: N/A
            - `revision`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PeftModelAdapter`
- **Description:** Loads any "peft" model and it's base model.
- **Methods:**
    - **`match`**
        - **Description:** Accepts any model path with "peft" in the name
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** Loads the base model then the (peft) adapter weights
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** Uses the conv template of the base model
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `VicunaAdapter`
- **Description:** Model adapter for Vicuna models (e.g., lmsys/vicuna-7b-v1.5)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`
    - **`raise_warning_for_old_weights`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model`: N/A

### class `AiroborosAdapter`
- **Description:** The model adapter for jondurbin/airoboros-*
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A

### class `LongChatAdapter`
- **Description:** Model adapter for LongChat models (e.g., lmsys/longchat-7b-16k).
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `GoogleT5Adapter`
- **Description:** The model adapter for google/Flan based models, such as Salesforce/codet5p-6b, lmsys/fastchat-t5-3b-v1.0, flan-t5-*, flan-ul2
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A

### class `KoalaAdapter`
- **Description:** The model adapter for Koala
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `AlpacaAdapter`
- **Description:** The model adapter for Alpaca
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ChatGLMAdapter`
- **Description:** The model adapter for THUDM/chatglm-6b, THUDM/chatglm2-6b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CodeGeexAdapter`
- **Description:** The model adapter for THUDM/codegeex-6b, THUDM/codegeex2-6b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `DollyV2Adapter`
- **Description:** The model adapter for databricks/dolly-v2-12b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `OasstPythiaAdapter`
- **Description:** The model adapter for OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A

### class `OasstLLaMAAdapter`
- **Description:** The model adapter for OpenAssistant/oasst-sft-7-llama-30b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `OpenChat35Adapter`
- **Description:** The model adapter for OpenChat 3.5 (e.g. openchat/openchat_3.5)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `TenyxChatAdapter`
- **Description:** The model adapter for TenyxChat (e.g. tenyx/TenyxChat-7B-v1)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PythiaAdapter`
- **Description:** The model adapter for any EleutherAI/pythia model
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A

### class `StableLMAdapter`
- **Description:** The model adapter for StabilityAI/stablelm-tuned-alpha-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `MPTAdapter`
- **Description:** The model adapter for MPT series (mosaicml/mpt-7b-chat, mosaicml/mpt-30b-chat)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `BaizeAdapter`
- **Description:** The model adapter for project-baize/baize-v2-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `RwkvAdapter`
- **Description:** The model adapter for BlinkDL/RWKV-4-Raven
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `OpenBuddyAdapter`
- **Description:** The model adapter for OpenBuddy/openbuddy-7b-v1.1-bf16-enc
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PhoenixAdapter`
- **Description:** The model adapter for FreedomIntelligence/phoenix-inst-chat-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ReaLMAdapter`
- **Description:** The model adapter for FreedomIntelligence/ReaLM-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ChatGPTAdapter`
- **Description:** The model adapter for ChatGPT
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `AzureOpenAIAdapter`
- **Description:** The model adapter for Azure OpenAI
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PplxAIAdapter`
- **Description:** The model adapter for Perplexity AI
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ClaudeAdapter`
- **Description:** The model adapter for Claude
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `BardAdapter`
- **Description:** The model adapter for Bard
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PaLM2Adapter`
- **Description:** The model adapter for PaLM2
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `GeminiAdapter`
- **Description:** The model adapter for Gemini
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `BiLLaAdapter`
- **Description:** The model adapter for Neutralzz/BiLLa-7B-SFT
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `RedPajamaINCITEAdapter`
- **Description:** The model adapter for togethercomputer/RedPajama-INCITE-7B-Chat
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `H2OGPTAdapter`
- **Description:** The model adapter for h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `RobinAdapter`
- **Description:** The model adapter for LMFlow/Full-Robin-7b-v2
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `SnoozyAdapter`
- **Description:** The model adapter for nomic-ai/gpt4all-13b-snoozy
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `WizardLMAdapter`
- **Description:** The model adapter for WizardLM/WizardLM-13B-V1.0
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ManticoreAdapter`
- **Description:** The model adapter for openaccess-ai-collective/manticore-13b-chat-pyg
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `GuanacoAdapter`
- **Description:** The model adapter for timdettmers/guanaco-33b-merged
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ChangGPTAdapter`
- **Description:** The model adapter for lcw99/polyglot-ko-12.8b-chang-instruct-chat
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CamelAdapter`
- **Description:** The model adapter for camel-ai/CAMEL-13B-Combined-Data
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `TuluAdapter`
- **Description:** The model adapter for allenai/tulu-30b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `FalconAdapter`
- **Description:** The model adapter for tiiuae/falcon-40b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `FalconChatAdapter`
- **Description:** No docstring available.
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `TigerBotAdapter`
- **Description:** The model adapter for TigerResearch/tigerbot-7b-sft
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `BaichuanAdapter`
- **Description:** The model adapter for Baichuan models (e.g., baichuan-inc/Baichuan-7B)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `XGenAdapter`
- **Description:** The model adapter for Salesforce/xgen-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `NousHermesAdapter`
- **Description:** The model adapter for NousResearch/Nous-Hermes-13b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `InternLMChatAdapter`
- **Description:** The model adapter for internlm/internlm-chat-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `StarChatAdapter`
- **Description:** The model adapter for HuggingFaceH4/starchat-beta
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `MistralAdapter`
- **Description:** The model adapter for Mistral AI models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Llama2Adapter`
- **Description:** The model adapter for Llama-2 (e.g., meta-llama/Llama-2-7b-hf)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Llama3Adapter`
- **Description:** The model adapter for Llama-3 (e.g., meta-llama/Meta-Llama-3-8B-Instruct)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Llama31Adapter`
- **Description:** The model adapter for Llama-3 (e.g., meta-llama/Meta-Llama-3-8B-Instruct)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `GrokAdapter`
- **Description:** No docstring available.
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CuteGPTAdapter`
- **Description:** The model adapter for CuteGPT
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `OpenOrcaAdapter`
- **Description:** Model adapter for Open-Orca models which may use different prompt templates
- (e.g. Open-Orca/OpenOrcaxOpenChat-Preview2-13B, Open-Orca/Mistral-7B-OpenOrca)
- `OpenOrcaxOpenChat-Preview2-13B` uses their "OpenChat Llama2 V1" prompt template.
    - [Open-Orca/OpenOrcaxOpenChat-Preview2-13B #Prompt Template](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B#prompt-template)
- `Mistral-7B-OpenOrca` uses the [OpenAI's Chat Markup Language (ChatML)](https://github.com/openai/openai-python/blob/main/chatml.md)
    format, with <|im_start|> and <|im_end|> tokens added to support this.
    - [Open-Orca/Mistral-7B-OpenOrca #Prompt Template](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca#prompt-template)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `DolphinAdapter`
- **Description:** Model adapter for ehartford/dolphin-2.2.1-mistral-7b
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Hermes2Adapter`
- **Description:** Model adapter for teknium/OpenHermes-2.5-Mistral-7B and teknium/OpenHermes-2-Mistral-7B models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `NousHermes2MixtralAdapter`
- **Description:** Model adapter for NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO model
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `WizardCoderAdapter`
- **Description:** The model adapter for WizardCoder (e.g., WizardLM/WizardCoder-Python-34B-V1.0)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `QwenChatAdapter`
- **Description:** The model adapter for Qwen/Qwen-7B-Chat
To run this model, you need to ensure additional flash attention installation:
``` bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
pip install csrc/layer_norm
pip install csrc/rotary
```

Since from 2.0, the following change happened
- `flash_attn_unpadded_func` -> `flash_attn_varlen_func`
- `flash_attn_unpadded_qkvpacked_func` -> `flash_attn_varlen_qkvpacked_func`
- `flash_attn_unpadded_kvpacked_func` -> `flash_attn_varlen_kvpacked_func`
You may need to revise the code in: https://huggingface.co/Qwen/Qwen-7B-Chat/blob/main/modeling_qwen.py#L69
to from flash_attn.flash_attn_interface import flash_attn_varlen_func as flash_attn_unpadded_func
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`float_set`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `config`: N/A
            - `option`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `SmaugChatAdapter`
- **Description:** The model adapter for abacusai/Smaug-2-72B.
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `BGEAdapter`
- **Description:** The model adapter for BGE (e.g., BAAI/bge-large-en-v1.5)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `E5Adapter`
- **Description:** The model adapter for E5 (e.g., intfloat/e5-large-v2)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `AquilaChatAdapter`
- **Description:** The model adapter for BAAI/Aquila

Now supports:
- BAAI/AquilaChat-7B
- BAAI/AquilaChat2-7B
- BAAI/AquilaChat2-34B
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Lamma2ChineseAdapter`
- **Description:** The model adapter for FlagAlpha/LLama2-Chinese sft
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Lamma2ChineseAlpacaAdapter`
- **Description:** The model adapter for ymcui/Chinese-LLaMA-Alpaca sft
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `VigogneAdapter`
- **Description:** The model adapter for vigogne (e.g., bofenghuang/vigogne-2-7b-chat)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `OpenLLaMaOpenInstructAdapter`
- **Description:** The model adapter for OpenLLaMa-Open-Instruct (e.g., VMware/open-llama-7b-open-instruct)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CodeLlamaAdapter`
- **Description:** The model adapter for CodeLlama (e.g., codellama/CodeLlama-34b-hf)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `StableVicunaAdapter`
- **Description:** The model adapter for StableVicuna
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PhindCodeLlamaAdapter`
- **Description:** The model adapter for Phind-CodeLlama (e.g., Phind/Phind-CodeLlama-34B-v2)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Llama2ChangAdapter`
- **Description:** The model adapter for Llama2-ko-chang (e.g., lcw99/llama2-ko-chang-instruct-chat)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `ZephyrAdapter`
- **Description:** The model adapter for Zephyr (e.g. HuggingFaceH4/zephyr-7b-alpha)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `NotusAdapter`
- **Description:** The model adapter for Notus (e.g. argilla/notus-7b-v1)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CatPPTAdapter`
- **Description:** The model adapter for CatPPT (e.g. rishiraj/CatPPT)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `TinyLlamaAdapter`
- **Description:** The model adapter for TinyLlama (e.g. TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `XwinLMAdapter`
- **Description:** The model adapter for Xwin-LM V0.1 and V0.2 series of models(e.g., Xwin-LM/Xwin-LM-70B-V0.1)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `LemurAdapter`
- **Description:** The model adapter for OpenLemur/lemur-70b-chat-v1
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `PygmalionAdapter`
- **Description:** The model adapter for Pygmalion/Metharme series of models(e.g., PygmalionAI/mythalion-13b)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `XdanAdapter`
- **Description:** The model adapter for xDAN-AI (e.g. xDAN-AI/xDAN-L1-Chat-RL-v1)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `MicrosoftOrcaAdapter`
- **Description:** The model adapter for Microsoft/Orca-2 series of models (e.g. Microsoft/Orca-2-7b, Microsoft/Orca-2-13b)
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `YiAdapter`
- **Description:** The model adapter for Yi models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `DeepseekCoderAdapter`
- **Description:** The model adapter for deepseek-ai's coder models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `DeepseekChatAdapter`
- **Description:** The model adapter for deepseek-ai's chat models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `GeminiAdapter`
- **Description:** The model adapter for Gemini
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `Yuan2Adapter`
- **Description:** The model adapter for Yuan2.0
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `MetaMathAdapter`
- **Description:** The model adapter for MetaMath models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `BagelAdapter`
- **Description:** Model adapter for jondurbin/bagel-* models
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `SolarAdapter`
- **Description:** The model adapter for upstage/SOLAR-10.7B-Instruct-v1.0
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `SteerLMAdapter`
- **Description:** The model adapter for nvidia/Llama2-70B-SteerLM-Chat
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `GemmaAdapter`
- **Description:** The model adapter for google/gemma
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `LlavaAdapter`
- **Description:** The model adapter for liuhaotian/llava-v1.5 series of models
- **Methods:**
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `YuanAdapter`
- **Description:** The model adapter for Yuan
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `OlmoAdapter`
- **Description:** The model adapter for allenai/OLMo-7B-Instruct
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `YandexGPTAdapter`
- **Description:** The model adapter for YandexGPT
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CllmAdapter`
- **Description:** The model adapter for CLLM
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `CohereAdapter`
- **Description:** The model adapter for Cohere
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `DBRXAdapter`
- **Description:** The model adapter for Databricks
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`load_model`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
            - `from_pretrained_kwargs`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `RekaAdapter`
- **Description:** The model adapter for Reka
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### class `NoSystemAdapter`
- **Description:** No docstring available.
- **Methods:**
    - **`match`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
    - **`get_default_conv_template`**
        - **Description:** No docstring available.
        - **Parameters:**
            - `self`: N/A
            - `model_path`: N/A
        - **Returns:** `Conversation`

### function `register_model_adapter`
- **Description:** Register a model adapter.
- **Parameters:**
    - `cls`: N/A

### function `get_model_adapter`
- **Description:** Get a model adapter for a model_path.
- **Parameters:**
    - `model_path`: N/A
- **Returns:** `BaseModelAdapter`

### function `raise_warning_for_incompatible_cpu_offloading_configuration`
- **Description:** No docstring available.
- **Parameters:**
    - `device`: N/A
    - `load_8bit`: N/A
    - `cpu_offloading`: N/A

### function `load_model`
- **Description:** Load a model from Hugging Face.
- **Parameters:**
    - `model_path`: N/A
    - `device`: N/A
    - `num_gpus`: N/A
    - `max_gpu_memory`: N/A
    - `dtype`: N/A
    - `load_8bit`: N/A
    - `cpu_offloading`: N/A
    - `gptq_config`: N/A
    - `awq_config`: N/A
    - `exllama_config`: N/A
    - `xft_config`: N/A
    - `revision`: N/A
    - `debug`: N/A

### function `get_conversation_template`
- **Description:** Get the default conversation template.
- **Parameters:**
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `get_generate_stream_function`
- **Description:** Get the generate_stream function for inference.
- **Parameters:**
    - `model`: N/A
    - `model_path`: N/A

### function `add_model_args`
- **Description:** No docstring available.
- **Parameters:**
    - `parser`: N/A

### function `remove_parent_directory_name`
- **Description:** Remove parent directory name.
- **Parameters:**
    - `model_path`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `load_compress_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `device`: N/A
    - `torch_dtype`: N/A
    - `revision`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** Accepts any model path with "peft" in the name
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** Loads the base model then the (peft) adapter weights
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** Uses the conv template of the base model
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `raise_warning_for_old_weights`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `float_set`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `config`: N/A
    - `option`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `load_model`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
    - `from_pretrained_kwargs`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `match`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A

### function `get_default_conv_template`
- **Description:** No docstring available.
- **Parameters:**
    - `self`: N/A
    - `model_path`: N/A
- **Returns:** `Conversation`

### function `generate_stream_peft`
- **Description:** No docstring available.
- **Parameters:**
    - `model`: N/A
    - `tokenizer`: N/A
    - `params`: N/A
    - `device`: N/A
    - `context_len`: N/A
    - `stream_interval`: N/A
    - `judge_sent_end`: N/A

## Important Variables/Constants

- `ANTHROPIC_MODEL_LIST`: [Please describe the purpose of this constant. Verify if it's a true global constant.]
- `OPENAI_MODEL_LIST`: [Please describe the purpose of this constant. Verify if it's a true global constant.]

## Usage Examples

*Note: Usage examples are placeholders and may need to be manually added or refined based on the actual functionality of the file.*

```python
# Example usage (if applicable)
# import ...
# result = call_function(...)
```

## Dependencies and Interactions

- **Internal Dependencies:** (Imports from within the FastChat project)
    - `fastchat.constants.CPU_ISA`
    - `fastchat.conversation.Conversation`
    - `fastchat.conversation.get_conv_template`
    - `fastchat.model.compression.load_compress_model`
    - `fastchat.model.llama_condense_monkey_patch.replace_llama_with_condense`
    - `fastchat.model.model_chatglm.generate_stream_chatglm`
    - `fastchat.model.model_cllm.generate_stream_cllm`
    - `fastchat.model.model_codet5p.generate_stream_codet5p`
    - `fastchat.model.model_exllama.generate_stream_exllama`
    - `fastchat.model.model_falcon.generate_stream_falcon`
    - `fastchat.model.model_xfastertransformer.generate_stream_xft`
    - `fastchat.model.model_yuan2.generate_stream_yuan2`
    - `fastchat.model.monkey_patch_non_inplace.replace_llama_attn_with_non_inplace_operations`
    - `fastchat.model.rwkv_model.RwkvModel`
    - `fastchat.modules.awq.AWQConfig`
    - `fastchat.modules.awq.load_awq_quantized`
    - `fastchat.modules.exllama.ExllamaConfig`
    - `fastchat.modules.exllama.load_exllama_model`
    - `fastchat.modules.gptq.GptqConfig`
    - `fastchat.modules.gptq.load_gptq_quantized`
    - `fastchat.modules.xfastertransformer.XftConfig`
    - `fastchat.modules.xfastertransformer.load_xft_model`
    - `fastchat.serve.inference.generate_stream`
    - `fastchat.utils.get_gpu_memory`
- **External Libraries:** (Imports from outside the FastChat project, excluding standard Python libs)
    - `accelerate`
    - `intel_extension_for_pytorch`
    - `modelscope.hub.snapshot_download.snapshot_download`
    - `peft.PeftConfig`
    - `peft.PeftModel`
    - `psutil`
    - `torch`
    - `torch_npu`
    - `transformers`
    - `transformers.AutoConfig`
    - `transformers.AutoModel`
    - `transformers.AutoModelForCausalLM`
    - `transformers.AutoModelForSeq2SeqLM`
    - `transformers.AutoTokenizer`
    - `transformers.BitsAndBytesConfig`
    - `transformers.LlamaForCausalLM`
    - `transformers.LlamaTokenizer`
    - `transformers.T5Tokenizer`
    - `transformers.generation.GenerationConfig`
    - `warnings`
- **Interactions:**
    - *[This section requires manual analysis. Describe how this file interacts with other components of the FastChat system, such as which modules it calls, which modules call it, and any data it exchanges with other parts of the system.]*
