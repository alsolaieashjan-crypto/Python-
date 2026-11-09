# AI300: Foundations of Artificial Intelligence & Python Algorithms

This repository contains algorithmic implementations, interactive game systems, and problem-solving assignments developed for **AI300** at King Saud University. The codebase demonstrates algorithmic problem-solving, 2D matrix traversal, heuristic AI decision logic, and persistent file logging using Python.

---

## 📁 Repository Structure

### 1. Games and Heuristic AI
- **Tic-Tac-Toe with Rule-Based AI (`AI300_HW2_AshjanAlsolaie.py`)**:
  - Interactive 3x3 grid modeling with coordinate validation and turn alternation.
  - Implements an automated AI opponent utilizing rule-based heuristics (winning line detection, opponent block, center priority, and corner defense).
  - Tracks session performance metrics via nested dictionaries.
- **Hangman Engine (`AI300_HW1_AshjanAlsolaie.py`)**:
  - Visual ASCII rendering across 6 error margins, dynamic score computation, and input sanitization.
- **2D Grid Traversal & Collision (`AI300_Lab8_AshjanAlsolaie.py`)**:
  - Coordinate system using Python tuples and dictionaries.
  - Simulates WASD navigation, boundary enforcement, obstacle collision handling, and path history tracking.
- **Menu-Driven Framework (`AI300_HW0_AshjanAlsolaie.py`)**:
  - Interactive CLI game shell managing dynamic score averages and session routing.

### 2. Algorithmic Problem Solving
- **Trapping Rainwater (`AI300_Lab7_AshjanAlsolaie.py`)**:
  - Classical two-boundary elevation algorithm calculating cumulative trapped rainwater volume across irregular terrain.
  - Utilizes array slicing and dynamic prefix/suffix bounds checking ($\min(\max_{left}, \max_{right}) - \text{height}$).
- **Lexical Sentiment Analyzer (`AI300_Lab6_AshjanAlsolaie.py`)**:
  - Slicing-based text tokenization and lexicon polarity scoring (Positive, Negative, Neutral).
  - Extracts the exact positional token index triggering the classification.

### 3. System Workflows and IO
- **Audit & File Persistence (`AI300_Lab9_AshjanAlsolaie.py`)**:
  - File I/O workflows managing structured text manipulation, header validation, and iterative revision counters.
- **Zakat & Multi-Account Systems (`AI300_Lab1_AshjanAlsolaie.py`, `AI300_Lab4_AshjanAlsolaie.py`)**:
  - Financial threshold evaluation, multi-metal Nisab market pricing (Gold, Silver, or the cheaper of both), and multi-account asset aggregation.

---

## 🛠️ Technical Competencies
- **Algorithmic Logic:** Array slicing, two-boundary min-max analysis, greedy path traversal, and heuristic AI decision trees.
- **Data Structures:** Immutable coordinate tuples, nested state dictionaries, and dynamic lists.
- **Software Practices:** Input sanitization, procedural decomposition, and persistent file logging.
