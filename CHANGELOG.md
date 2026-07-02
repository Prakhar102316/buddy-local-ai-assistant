# Changelog

All notable changes to **Buddy** will be documented in this file.

The format is based on **Keep a Changelog**, and this project follows **Semantic Versioning** where applicable.

---

[0.8] - 2026-07-02

## Overview

Version 0.8 marks Buddy's transition from a terminal-based AI assistant to a desktop application with its own graphical user interface. This is the largest user-facing update since the project began.

---

## Added

### GUI Foundation

* Introduced Flet-based desktop interface.
* Created a modular GUI architecture.
* Added:

  * Main Window
  * Sidebar
  * Chat Area
  * Input Bar
  * Centralized Style Manager

### Backend Integration

* Connected the GUI with Buddy's backend.
* Chat messages are now processed through the existing AI pipeline.
* Backend now powers the GUI instead of the terminal.

### Chat System

* User messages appear in dedicated chat bubbles.
* Buddy responses appear in separate assistant bubbles.
* Automatic scrolling to the latest message.

### Project Structure

* New `gui/` module added.
* Separated UI components into individual files.
* Improved maintainability through modular design.

---

## Improvements

* Preserved all existing backend capabilities:

  * Memory System
  * Memory Search
  * Question Classifier
  * Conversation History
  * Ollama Integration
  * Prompt Management

* Backend now works seamlessly with both terminal and GUI environments.

---

## Known Issues

* Buddy responses are displayed after generation completes instead of streaming token-by-token.
* GUI briefly blocks while the model generates long responses.
* Streaming architecture has been postponed to **v0.9** for a complete implementation.

---

## Statistics

* New GUI framework integrated.
* Modular desktop interface completed.
* Backend successfully connected to GUI.
* Buddy officially transitions from a console application to a desktop AI assistant.

---

## Next Version

### v0.9 — Performance & Professional UX

Planned improvements:

* True streaming responses
* Zero GUI freezing
* Background response generation
* Typing indicator
* Improved responsiveness
* General GUI polish


## [0.7] - 2026-07-01

### Added
- Intelligent Question Classifier
- Intelligent Memory Search Engine
- Keyword extraction for personal queries
- Stop-word filtering for improved search accuracy
- Synonym normalization (favorite ↔ favourite)
- Ranked memory retrieval
- Relevant context injection into prompts
- Smarter retrieval pipeline for personal memories

### Improved
- Personal questions now retrieve only relevant memories
- General questions bypass memory search completely
- Reduced unnecessary prompt context
- Improved response accuracy for stored memories

### Fixed
- Fixed memory retrieval failures caused by keyword mismatch
- Fixed British/American spelling differences during retrieval
- Improved retrieval scoring for better memory matching

### Internal
- Introduced QuestionClassifier module
- Introduced MemorySearch module
- Refactored Buddy architecture into an intelligent retrieval pipeline
- Improved modularity and maintainability


## [v0.6] - 2026-07-01

### Added

* Added `/memory` command to display all stored memories.
* Added `/remember` command to manually save memories.
* Added `/forget` command to remove saved memories.
* Added `/edit` command to update existing memories.
* Added `/search` command to search memories by keyword.
* Added `/stats` command to display Buddy statistics.

### Improved

* Redesigned `/help` using Rich tables.
* Improved `/about` screen.
* Improved `/version` screen.
* Better formatted memory display.
* Cleaner command-line interface.

### Memory System

* Manual memory management.
* Automatic memory detection.
* Memory search capability.
* Memory statistics.

### Fixed

* Fixed multiple indentation issues.
* Fixed UI rendering problems.
* Fixed command handling bugs.
* Fixed memory display issues.

### ✅ QA Status

* Full command testing completed successfully.
* Stable release verified.

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
