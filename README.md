🤖 Buddy

Privacy-First Offline Personal AI Companion

Buddy is an open-source, offline-first AI companion designed to run entirely on your local machine. Unlike cloud-based AI assistants, Buddy keeps conversations, memories, and reasoning on your own computer, giving you complete control over your data while providing a fast and highly customizable AI experience.

Originally developed as a BCA major project, Buddy is evolving into a long-term personal AI platform focused on productivity, learning, cybersecurity, software development, and everyday assistance.

---

✨ Features

- 🧠 Local AI powered by Ollama
- 💬 Beautiful desktop chat interface built with Flet
- ⚡ Real-time response streaming
- 📝 Persistent conversation history
- 🧩 Long-term memory retrieval
- 🎯 Intelligent question classification
- 🔒 100% privacy-first (no cloud dependency)
- 🌐 Works completely offline after setup
- 🛠 Modular architecture for future expansion

---

🛠 Tech Stack

AI

- Ollama
- Custom Modelfiles
- Sentence Transformers
- ChromaDB

Frontend

- Flet

Backend

- Python
- Async Streaming
- Thread-safe architecture

Memory

- ChromaDB
- Embedding Search
- Persistent Storage

Development

- Git
- GitHub
- Docker (optional)
- Fedora Linux
- Windows

---

🏗 Project Architecture

User
   │
   ▼
Flet Desktop GUI
   │
   ▼
Buddy Backend
   │
   ├── Conversation Manager
   ├── Memory Manager
   ├── Memory Search
   ├── Question Classifier
   └── Ollama Client
             │
             ▼
      Local LLM (Ollama)

---

📂 Project Structure

Buddy/
│
├── core/
├── gui/
├── memory/
├── prompts/
├── models/
├── report/
├── assets/
├── screenshots/
│
├── buddy_gui.py
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore

---

🚀 Development Roadmap

✅ v0.1 — Project Foundation

- Project setup
- Ollama integration
- Initial backend

---

✅ v0.2 — Core Backend

- Conversation system
- Backend architecture
- Modular project structure

---

✅ v0.3 — Memory System

- Persistent memory
- ChromaDB integration
- Memory retrieval

---

✅ v0.4 — Question Classification

- Intent detection
- Context-aware memory search

---

✅ v0.5 — Desktop GUI

- Flet interface
- Sidebar
- Chat window
- Input bar

---

✅ v0.6 — Personality & Conversation

- Conversation history
- AI personality improvements

---

✅ v0.7 — Stability

- Code cleanup
- Performance improvements
- Backend optimization

---

✅ v0.8 — Memory Optimization

- Improved retrieval
- Better conversation flow
- Faster responses

---

✅ v0.9 — Pulse ❤️

- Real-time response streaming
- Async UI rendering
- Smooth chat experience
- Major GUI responsiveness improvements

---

🚧 v1.0 — Production Release

Planned features:

- Voice input
- Voice output
- Image understanding
- Plugin architecture
- Better memory ranking
- Cross-platform packaging
- Mobile companion support
- Production-ready documentation

---

🎯 Project Vision

Buddy aims to become a complete offline AI companion capable of assisting with:

- Software Development
- Cybersecurity
- Learning
- Research
- Productivity
- Daily Planning
- Personal Knowledge Management

while ensuring user privacy and complete local ownership of data.

---

📖 Documentation

Detailed technical documentation is available in the "report/" directory.

---

🤝 Contributing

Buddy is under active development. Contributions, bug reports, feature requests, and discussions are welcome as the project matures.

---

📜 License

This project is licensed under the MIT License.

---

👨‍💻 Developer

Prakhar Pandey

Bachelor of Computer Applications (Data Science & AI)

Building Buddy as a long-term open-source, privacy-first AI companion.