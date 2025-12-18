from typing import Dict, Callable
class SimpleDataProcessor:
    def __init__(self, data: List[Dict[str, Any]]):
        """
        Initialize the processor with the input data.
        - List: A list containing multiple elements.
        - Dict[str, Any]: Each element in the list is a dictionary.
        - str: Dictionary keys must be strings.
        - Any: Dictionary values can be of any data type (int, float, str, etc.).
        """
        self._data = data  # Private attribute

    def get_average_score(self, subject: str) -> Optional[float]:
        """
        Calculate the average score of a subject.
        Time Complexity: O(n)
        """
        
        if not self._data:
            return None
        
        total_score = 0.0
        count = 0
        
        for record in self._data:
            # Use the .get() method to avoid KeyError
            score = record.get(subject)
            if isinstance(score, (int, float)):
                total_score += score
                count += 1
                
        if count == 0:
            return 0.0
        return round(total_score / count, 2)

# Usage
students = [{"name": "An", "math": 8.5}, {"name": "Binh", "math": 9.0}, {"name": "Chi", "math": "N/A"}]
processor = SimpleDataProcessor(students)
print(f"Average Math: {processor.get_average_score('math')}")