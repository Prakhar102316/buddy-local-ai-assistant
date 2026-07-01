# Changelog

All notable changes to **Buddy** will be documented in this file.

The format is based on **Keep a Changelog**, and this project follows **Semantic Versioning** where applicable.

---
## [0.5] - 2026-07-02

### Added

* Rich terminal interface using Rich
* `/help` command with formatted command list
* `/model` command to display current AI configuration
* `/about` command with Buddy information
* `/version` command showing Buddy version details
* Rich banner and improved startup screen

### Improved

* Cleaner terminal conversation interface
* Better command-line user experience
* Consistent UI styling across all commands
* Improved project organization
* Removed development debug output

### Fixed

* Memory retrieval after conversation clear
* Various indentation and UI issues
* Conversation display formatting

## [0.4] - 2026-06-30

### Added

* Long-term persistent memory using `buddy_memory.json`
* Automatic memory detection from user messages
* Automatic memory saving
* Memory retrieval across sessions
* Context injection for personalized responses
* Streaming response generation
* `MemoryManager` module
* `MemoryDetector` module

### Improved

* Modular architecture with dedicated memory components
* Personalized responses using stored user information
* Cleaner response generation pipeline

### Fixed

* Buddy now remembers information after `/clear`
* Fixed memory integration into conversations
* Corrected prompt injection order

### Removed

* Development debug logs (`MESSAGES SENT TO OLLAMA`)
* Memory context debug output


## [0.3.0] - 2026-06-30

### Added

* Implemented real-time streaming AI responses.
* Added `stream_generate()` method to the Ollama Client.
* Buddy now displays responses progressively instead of waiting for the entire response.
* Preserved conversation history while streaming responses.

### Improved

* Improved overall user experience by making conversations feel more natural.
* Maintained compatibility with the existing `generate()` method.

### Internal

* Integrated Ollama's `stream=True` API.
* Refactored response handling for streaming output.

---

## [0.2.0] - 2026-06-30

### Added

* Conversation memory system.
* Prompt Manager module.
* External system prompt (`system_prompt.txt`).
* Honest-response behaviour through prompt engineering.
* `/clear` command to reset conversation history while preserving Buddy's personality.

### Improved

* Buddy now responds with a friendly, humble personality.
* Eliminated hallucinated personal information through improved prompting.

### Internal

* Refactored architecture into:

  * Buddy
  * Conversation Manager
  * Prompt Manager
  * Ollama Client

---

## [0.1.0] - 2026-06-29

### Added

* Integrated Buddy with Ollama.
* Created the Ollama Client.
* Enabled the first successful offline AI conversation.

### Internal

* Verified complete offline execution.
* Configured Python virtual environment for the project.

---

## [0.0.0] - 2026-06-28

### Added

* Initialized the Buddy project.
* Created the complete project folder structure.
* Configured Git and GitHub.
* Added the initial README.
* Designed the modular software architecture.
