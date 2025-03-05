import joblib

# Load the model
model = joblib.load("iris_model.pkl")

# Print the model
print("Model:", model)

# Print model parameters
print("Model Parameters:", model.get_params())

# If it's a decision tree, print the tree structure
if hasattr(model, "tree_"):
    from sklearn.tree import export_text

    tree_rules = export_text(model)
    print("Tree structure:\n", tree_rules)

# If the model has feature importances, print them
if hasattr(model, "feature_importances_"):
    print("Feature Importances:", model.feature_importances_)
