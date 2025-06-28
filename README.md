# 🚀 LeetCode Solutions Collection

A comprehensive collection of my solutions to LeetCode problems from their Interview Crash Course: Algorithms and Data Structures, plus additional problems discovered through AlgoMonster or invented by me (not that someone else didn't think of them as well).

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Naming Convention](#file-naming-convention)
- [Categories](#categories)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains my solutions to various algorithmic problems, including:

- **LeetCode Problems**: Numbered solutions (e.g., `1_TwoSum.py`, `200_NumberOfIslands.py`)
- **Tutorial Examples**: Helper files prefixed with `0_` that demonstrate algorithms and concepts
- **Practice Problems**: Additional problems from various sources
- **Data Structures**: Implementations of common data structures and algorithms
- **Utility Modules**: Reusable code snippets and helper functions

Each file includes:

- Problem definition and description
- My commented solutions
- Test cases with inputs and expected outputs
- Some Explanations of the approach used

## 📁 Project Structure

```
leet_python311/
├── 📄 LeetCode Problems (numbered files)
│   ├── 1_TwoSum.py
│   ├── 200_NumberOfIslands.py
│   └── ... (100+ solutions)
├── 🔧 Tutorial & Helper Files (0_ prefix)
│   ├── 0_AA_CommonOps.py          # Common operations and utilities
│   ├── 0_BST.py                   # Binary Search Tree operations
│   ├── 0_DijkstraAdjList.py       # Dijkstra's algorithm
│   └── ... (50+ helper files)
├── 📊 Sorts/                      # Sorting algorithms
│   ├── BubbleSort.py
│   ├── QuickSort.py
│   ├── MergeSort.py
│   └── ... (6 sorting algorithms)
├── 🧩 Snippets/                   # Code snippets and examples
│   ├── CacheDecorator.py
│   ├── ListComprehension.py
│   ├── StringManipulations.py
│   └── ... (25+ snippets)
├── 🛠️ Modules/                    # Reusable modules
│   ├── Timer.py
│   ├── Formatting.py
│   └── TextEffects.py
├── 📋 requirements.txt            # Python dependencies
└── 📖 README.md                   # This file
```

## ⚙️ Prerequisites

- **Python Version**: 3.11+ (recommended)
- **Operating System**: Linux, macOS, or Windows
- **Package Manager**: pip

## 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/jaydeelew/leet_python311
   cd leet_python311
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running Individual Problems

Each Python file can be run independently:

```bash
# Run a specific LeetCode problem
python 1_TwoSum.py

# Run a sorting algorithm
python Sorts/QuickSort.py
```

## 📝 File Naming Convention

- **`[Number]_[ProblemName].py`**: LeetCode problems (e.g., `1_TwoSum.py`)
- **`0_[Description].py`**: Tutorial examples and helper files
- **`[Category]/[Algorithm].py`**: Organized by category (e.g., `Sorts/QuickSort.py`)

## 🏷️ Categories

### 🔢 LeetCode Problems

- **Easy**: Problems 1-1000 (e.g., `1_TwoSum.py`, `125_ValidPalindrome.py`)
- **Medium**: Problems 1000-2000 (e.g., `1004_MaxConsecOnesIII.py`)
- **Hard**: Advanced problems (e.g., `1293_ShortestPathGridWithKremovableObstacles.py`)

### 🧮 Algorithm Categories

- **Arrays & Strings**: `3_LongestSubstringNoRepeats.py`, `5_LongestPalindromicSubstring.py`
- **Linked Lists**: `19_RemoveNthFromEnd.py`, `21_MergeTwoSortedLists.py`
- **Trees**: `100_SameTree.py`, `104_MaxDepthBinaryTree.py`
- **Graphs**: `200_NumberOfIslands.py`, `323_NumOfConnectedComponents.py`
- **Dynamic Programming**: `198_HouseRobber.py`, `322_CoinChange.py`
- **Two Pointers**: `15_3Sum.py`, `209_MinSizeSubarrySum.py`
- **Sliding Window**: `3_LongestSubstringNoRepeats.py`, `340_LongestSubstringMostKsameChars.py`

### 🛠️ Utility Files

- **Common Operations**: `0_AA_CommonOps.py` - Essential Python operations
- **Data Structures**: `0_BST.py`, `0_Trie.py` - Implementation examples
- **Algorithms**: `0_DijkstraAdjList.py`, `0_KahnAlgo.py` - Classic algorithms
- **Sorting**: `Sorts/` directory with 6 different sorting algorithms

### 📚 Code Snippets

- **Python Features**: `Snippets/ListComprehension.py`, `Snippets/Generator_SquareNums.py`
- **Data Manipulation**: `Snippets/ShallowAndDeepCopy.py`, `Snippets/RemoveDupsFromList.py`
- **String Operations**: `Snippets/StringManipulations.py`, `Snippets/IsAnagram.py`

## 🎯 Key Features

- **Comprehensive Coverage**: 100+ LeetCode problems with solutions
- **Educational Focus**: Well-commented code with explanations
- **Modular Design**: Reusable components and utility functions
- **Performance Optimized**: Multiple approaches for many problems
- **Test Cases**: Included test cases with expected outputs on many problems
- **Cross-Platform**: Works on Linux, macOS, and Windows

## 📄 License

This project is for educational purposes. All LeetCode problems are property of LeetCode.

---
