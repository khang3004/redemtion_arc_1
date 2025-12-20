# EQUATION: y=w*x ==> w = y/x
class SimpleModel:
    def __init__(self, x: list[float], y: float) -> None:
        self.x = x
        self.y = y
        self._w = self._calculate_weight()
    
    def _calculate_weight(self) -> float:
        return (self.y) / (sum(self.x))
        
    def _predict(self, x: float) -> float:
        return self._w * x

    def predict(self, x: list[float]) -> list[float]:
        return [self._predict(value) for value in x]

my_ml = SimpleModel(x=[1, 2, 3, 4, 5], y=5)
print(my_ml.predict([1, 2, 3, 4, 5]))

class SimpleModelPro:
    def __init__(self):
        # Initialization: Empty model
        # w is assigned None to indicate it hasn't learned anything yet
        self._w: float | None = None 

    def fit(self, X_train: list[float], y_train: float) -> None:
        """
        Training process.
        Logic: Weight = Total Output / Total Input
        """
        if not X_train:
            raise ValueError("Data cannot be empty")
            
        total_input = sum(X_train)
        if total_input == 0:
             raise ValueError("Sum of X cannot be 0 (Division by zero)")
             
        self._w = y_train / total_input
        print(f"Model trained! Learned weight: {self._w:.4f}")

    def predict(self, X_new: list[float]) -> list[float]:
        """Predict on new data"""
        # Defensive Programming: Check if the model has been trained
        if self._w is None:
            raise RuntimeError("Model not trained! Please call .fit() first.")
        
        # Fix shadowing: name the sub-variable 'item' or 'val'
        return [item * self._w for item in X_new]

# --- USAGE (Standard Workflow) ---

# 1. Create model instance
model = SimpleModelPro()

# 2. Feed data to learn (Fit)
# Example: Total area of 3 rooms is 100m2, Total price is 5 billion -> Price per 1m2 = 0.05
model.fit(X_train=[30.0, 30.0, 40.0], y_train=5.0)

# 3. Use for prediction (Predict)
# How much for a 50m2 room? -> 50 * 0.05 = 2.5 billion
prediction_results = model.predict(X_new=[50.0, 20.0])

print(f"Predicted price: {prediction_results}")