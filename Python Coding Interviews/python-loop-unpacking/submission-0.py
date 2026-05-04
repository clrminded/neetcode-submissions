from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max_name, max_score = scores[0][0], scores[0][1]
    for score in scores:
        if score[1] > max_score:
            max_score = score[1]
            max_name = score[0]
    return max_name
    
    


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
