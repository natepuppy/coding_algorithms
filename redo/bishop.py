def min_bishop_moves(start: int, end: int) -> int:
    if start == end:
        return 0
    
    start_r, start_c = start // 8, start % 8
    end_r, end_c = end // 8, end % 8

    # On different colors:
    if (start_r + start_c) % 2 != (end_r + end_c) % 2:
        return -1
    
    # On same diagonal:
    if abs(start_r - end_r) == abs(start_c - end_c): # The only hard part!!!!!
        return 1
    
    return 2


# --- Validation Test Cases ---
if __name__ == "__main__":
    test_cases = [
        {"start": 0,  "end": 0,  "expected": 0},
        {"start": 0,  "end": 9,  "expected": 1},
        {"start": 0,  "end": 1,  "expected": -1},
        {"start": 0,  "end": 2,  "expected": 2},
        {"start": 28, "end": 46, "expected": 1},
        {"start": 36, "end": 25, "expected": 2},
        {"start": 63, "end": 0,  "expected": 1}
    ]
    
    all_passed = True
    for i, tc in enumerate(test_cases):
        result = min_bishop_moves(tc["start"], tc["end"])
        if result == tc["expected"]:
            # print(#0a0) # Color indicator for success
            print(f"Test {i} Passed: start={tc['start']}, end={tc['end']} -> {result}")
        else:
            all_passed = False
            # print(#f00) # Color indicator for failure
            print(f"Test {i} FAILED: start={tc['start']}, end={tc['end']}. Expected {tc['expected']}, got {result}")
            
    if all_passed:
        print("\nAll standard test scenarios evaluated successfully!")
