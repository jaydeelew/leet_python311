## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Naming Convention](#file-naming-convention)
- [Categories](#categories)
- [Algorithm Categories](#algorithm-categories)
- [Utility Files](#utility-files)
- [Code Snippets](#code-snippets)
- [Key Features](#key-features)
- [License](#license)

## Overview

A comprehensive collection of my solutions to LeetCode problems from their Interview Crash Course: Algorithms and Data Structures, plus additional problems discovered through AlgoMonster or invented by me (not that someone else didn't think of them as well).

## Project Structure

```
leet_python311/
├── LeetCode Problems (numbered files)
│   ├── 1_TwoSum.py
│   ├── 200_NumberOfIslands.py
│   └── ... (100+ solutions)
├── Tutorial & Helper Files (0_ prefix)
│   ├── 0_AA_CommonOps.py          # Common operations and utilities
│   ├── 0_BST.py                   # Binary Search Tree operations
│   ├── 0_DijkstraAdjList.py       # Dijkstra's algorithm
│   └── ... (50+ helper files)
├── Sorts/                        # Sorting algorithms
│   ├── BubbleSort.py
│   ├── QuickSort.py
│   ├── MergeSort.py
│   └── ... (6 sorting algorithms)
├── Snippets/                     # Code snippets and examples
│   ├── CacheDecorator.py
│   ├── ListComprehension.py
│   ├── StringManipulations.py
│   └── ... (25+ snippets)
├── Modules/                      # Reusable modules
│   ├── Timer.py
│   ├── Formatting.py
│   └── TextEffects.py
└── README.md                     # This file
```

## Prerequisites

- **Python Version**: 3.11+ (recommended)
- **Operating System**: Linux, macOS, or Windows

## Installation

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

3. **Ready to use!** No additional dependencies required.

## Usage

### Running Individual Problems

Each Python file can be run independently:

```bash
# Run a specific LeetCode problem
python 1_TwoSum.py

# Run a sorting algorithm
python Sorts/QuickSort.py
```

## File Naming Convention

- **`[Number]_[ProblemName].py`**: LeetCode problems (e.g., `1_TwoSum.py`)
- **`0_[Description].py`**: Tutorial examples and helper files
- **`[Category]/[Algorithm].py`**: Organized by category (e.g., `Sorts/QuickSort.py`)

## Categories

### LeetCode Problems

- **Easy**: Problems 1-1000 (e.g., `1_TwoSum.py`, `125_ValidPalindrome.py`)
- **Medium**: Problems 1000-2000 (e.g., `1004_MaxConsecOnesIII.py`)
- **Hard**: Advanced problems (e.g., `1293_ShortestPathGridWithKremovableObstacles.py`)

## Algorithm Categories

- **Arrays & Strings**: `3_LongestSubstringNoRepeats.py`, `5_LongestPalindromicSubstring.py`, `53_MaxSubarray.py`, `560_SubarraySumEqualsK.py`, `209_MinSizeSubarrySum.py`, `643_MaxAvgSubarray1.py`, `2090_KradiuSubarrayAvgs.py`, `487_LengthOfLongestSubstringOfOnes.py`, `2389_LongestSubsequenceWithSumLimit.py`, `2461_MaxSumOfDistinctSubarraysLenk.py`, `2260_MinConsecCardsToPickUp.py`, `2248_IntersectionOfMultipleArrays.py`, `2352_EqualColumnAndRowPairs.py`

- **Linked Lists**: `19_RemoveNthFromEnd.py`, `21_MergeTwoSortedLists.py`, `138_CopyListRandomPointer.py`, `141_LinkedListCycle.py`, `876_MiddleLinkedList.py`, `61_RotateList.py`, `206_ReverseLinkedList.py`

- **Trees**: `100_SameTree.py`, `104_MaxDepthBinaryTree.py`, `98_IsValidBST.py`, `701_InsertIntoBST.py`, `530_MinDiffBetweenNodesBST.py`, `103_BinaryTreeZigzagLevelTraveral.py`, `144_PreorderTraversal.py`, `111_MinDepthBinaryTree.py`, `1448_CountGoodNodesBinaryTree.py`, `236_LowestCommonAncestor.py`, `270_ClosestBinarySearchTreeValue.py`, `515_LargestValueEachTreeRow.py`, `1302_DeepestLeavesSum.py`, `199_BinaryTreeRightSideView.py`, `863_AllNodesDistanceKfromTarget.py`

- **Graphs**: `200_NumberOfIslands.py`, `323_NumOfConnectedComponents.py`, `1091_ShortestPathBinaryMatrix.py`, `1129_ShortestPathAlternatingColors.py`, `797_AllPathsFromSourceToTarget.py`, `841_KeysAndRooms.py`, `1971_IsValidPath.py`, `1466_ReorderRoutesToCityZero.py`, `1557_MinNumOfVerticesToReachAllNodes.py`, `1926_NearestExitFromEntranceMaze.py`, `2368_ReachableNodesWithRestrictions.py`, `2101_DetonateMaxBombs.py`, `743_NetworkDelayTime.py`

- **Dynamic Programming**: `198_HouseRobber.py`, `322_CoinChange.py`, `70_ClimbingStairs.py`, `746_MinCostClimbingStairs.py`, `300_LsisIterative.py`, `300_LsisRecursive.py`, `1143_LongestCommonSubsequence.py`, `509_Fibonacci.py`

- **Two Pointers**: `15_3Sum.py`, `209_MinSizeSubarrySum.py`

- **Sliding Window**: `3_LongestSubstringNoRepeats.py`, `340_LongestSubstringMostKsameChars.py`

- **Binary Search**: `704_BinarySearch.py`, `69_Sqrt.py`, `33_SearchRotatedArray.py`, `270_ClosestBinarySearchTreeValue.py`, `875_KokoEatingBananas.py`, `1870_MinSpeedToArriveOnTime.py`, `1283_FIndSmallestDivisorGivenThreshold.py`, `1231_DivideChocolate.py`

- **Heaps & Priority Queues**: `295_MedianFromDataStream.py`, `502_IP0.py`, `347_TopKfrequentElements.py`, `703_KthLargestElementInStream.py`, `215_KthLargestElement.py`, `973_KclosestPointsToOrigin.py`, `2208_MinStepsToHalfSumAnArray.py`, `RemainderAfterSmashStones.py`, `RemoveStonesMinimizeArraySum.py`, `1167_MinimumCostConnectSticks.py`

- **Backtracking & Recursion**: `17_LetterCombinationsOfPhoneNum.py`, `22_GenerateParentheses.py`, `39_CombinationSum.py`, `46_Permutations.py`, `77_Combinations.py`, `78_Subsets.py`, `216_CombinationSum3.py`

- **Greedy**: `881_FewestNumOfBoatsToSavePeople.py`, `1710_MaximizeUnitsOnTruck.py`, `1481_LeastUniqueIntsAfterKremovals.py`, `1196_HowManyApplesCanPutInBasket.py`, `1189_MaxNumberOfBalloons.py`

- **Stack & Queue**: `739_DailyTemperatures.py`, `844_BackspaceStringCompare.py`, `1047_RemoveAdjacentDuplicates.py`, `1544_MakeStringGreat.py`

- **Hash Table & Counting**: `217_ContainsDuplicates.py`, `169_MajorityElement.py`, `49_GroupAnagrams.py`, `771_JewelsAndStones.py`, `1832_IsPangram.py`, `1941_AllCharsEqualOccurences.py`, `1133_LargestUniqueNumber.py`, `1426_CountingElements.py`

- **Math & Number Theory**: `204_CountPrimes.py`, `367_ValidPerfectSquare.py`, `1323_Max69Number.py`, `1732_FindHighestAltitude.py`, `1433_MinValueGetPosStepByStepSum.py`

- **Matrix & 2D Arrays**: `542_01Matrix.py`, `1380_LuckyNumsInMatrix.py`, `2352_EqualColumnAndRowPairs.py`

- **String Manipulation**: `125_ValidPalindrome.py`, `468_ValidateIPaddress.py`, `392_IsSubsequence.py`, `433_MinimumGeneticMutation.py`, `1544_MakeStringGreat.py`, `1047_RemoveAdjacentDuplicates.py`

## Utility Files

- **Common Operations**: `0_AA_CommonOps.py` - Essential Python operations
- **Data Structures**: `0_BST.py`, `0_Trie.py` - Implementation examples
- **Algorithms**: `0_DijkstraAdjList.py`, `0_KahnAlgo.py` - Classic algorithms
- **Sorting**: `Sorts/` directory with 6 different sorting algorithms

## Code Snippets

- **Python Features**: `Snippets/ListComprehension.py`, `Snippets/Generator_SquareNums.py`
- **Data Manipulation**: `Snippets/ShallowAndDeepCopy.py`, `Snippets/RemoveDupsFromList.py`
- **String Operations**: `Snippets/StringManipulations.py`, `Snippets/IsAnagram.py`

## Key Features

- **Comprehensive Coverage**: 100+ LeetCode problems with solutions
- **Educational Focus**: Well-commented code with explanations
- **Modular Design**: Reusable components and utility functions
- **Performance Optimized**: Multiple approaches for many problems
- **Test Cases**: Included test cases with expected outputs on many problems
- **Cross-Platform**: Works on Linux, macOS, and Windows

## License

This project is for educational purposes. All LeetCode problems are property of LeetCode.

---
