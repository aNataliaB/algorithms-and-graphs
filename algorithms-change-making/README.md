# Cost-Minimized Change-Making Problem Simulator (Greedy vs. Dynamic Programming)
A desktop GUI application implemented in Python that simulates and compares two standard computer science strategies for solving the change-making problem: the **Greedy Algorithm** and **Dynamic Programming**. Unlike the classic version of this problem, this system minimizes the total *cost* of the coins used rather than just their quantity.

## Project Overview
The application solves a bounded change-making problem where each coin in the user's "wallet" has both a face value (denomination) and an associated cost weight[cite: 5, 6]. It explicitly demonstrates cases where a greedy approach fails to find the optimal solution (or any solution at all) compared to the mathematically guaranteed optimal result produced by dynamic programming[cite: 5, 6].

### Key Features:
* **Algorithmic Duality:**
  * **Greedy Approach:** Sorts coins by denomination descending and greedily picks the largest available coin fitting the remaining target amount[cite: 6].
  * **Dynamic Programming (DP):** Uses a 2D matrix state breakdown ($O(N \cdot W)$ complexity) to calculate the absolute global minimum cost solution and backtracks to retrieve the exact coins used[cite: 6].
* **Graphical User Interface (Tkinter):** A clean desktop window providing inputs for custom coin sets, custom cost vectors, and target amounts with full runtime results layout.
* **Strict Input Validation:** Includes robust error parsing for negative values, non-integer arguments, mismatched array lengths between coins and costs, target amount boundaries, and alerts for insufficient total wallet balance.

## Team & Collaboration
This project was co-created as a collaborative academic assignment.
* **My Contribution:** Fully designed and coded the Graphical User Interface (`main.py`) using Tkinter. Implemented input streaming arrays parsing, data validation logic blocks, custom exception handling, window configurations, and runtime communication layers via visual warning messages[cite: 5]. Co-authored the core algorithms setup.

## Technologies
* **Language:** Python 
* **GUI Framework:** Tkinter[cite: 5]
* **Core Paradigms:** Dynamic Programming, Greedy Optimization, Bounded Knapsack-style constraints[cite: 6].

## Code Structure
* `main.py` - Script driving the Tkinter graphical interface layout and user loop validation rules[cite: 5].
* `core.py` - Algorithmic logic container housing the `Moneta` class, `wydaj_zachlannie` loop, and `wydaj_dynamicznie` matrix state processor[cite: 6].
