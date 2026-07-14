# {
#   "nodeType": "Add",
#   "left": { "nodeType": "Value", "valueType": "Int" },
#   "right": { "nodeType": "Value", "valueType": "Int" }
# }

# {
#   "nodeType": "Add",
#   "left": { "nodeType": "Value", "valueType": "Int" },
#   "right": { "nodeType": "Value", "valueType": "Bool" }
# }

# {
#   "nodeType": "If",
#   "condition": {
#     "nodeType": "IsEqual",
#     "left": { "nodeType": "Value", "valueType": "Int" },
#     "right": { "nodeType": "Value", "valueType": "Int" }
#   },
#   "thenBranch": { "nodeType": "Value", "valueType": "Bool" },
#   "elseBranch": { "nodeType": "Value", "valueType": "Bool" }
# }


# nodeType: [Value, Add, IsEqual, If]

# Value
# - Return the valueType

# Add
# - Check that the types of the sub nodes are both "Int"
# - If not, throw error, if they are, return "Int"

# IsEqual
# - Check that the types of the sub nodes are both "Bool"
# - If not, throw error, if they are, return "Bool"

# If
# - recursively send the node inside the condition to the dfs function
# - if it doesn't return a bool, throw error
# - if it returns true, call the dfs on the thenBranch
# - if it returns false, call the dfs on the elseBranch



def infer_type(ast):
    def dfs(node):
        node_type = node["nodeType"]
        
        if node_type == "Value":
            return node["valueType"]
        if node_type == "Add":
            left = dfs(node["left"])
            right = dfs(node["right"])
        
            if left == "Int" and right == "Int":
                return "Int"
            else:
                return "TypeError"
        if node_type == "IsEqual":
            left = dfs(node["left"])
            right = dfs(node["right"])

            if left == right and left != "TypeError":
                return "Bool"
            else:
                return "TypeError"
        if node_type == "If":
            condition_result = dfs(node["condition"])
            
            if condition_result != "Bool":   # What is the result? True or False?
                return "TypeError"
            
            then_branch = dfs(node["thenBranch"])
            else_branch = dfs(node["elseBranch"])

            if then_branch == else_branch:
                return then_branch
            else:
                return "TypeError"

    return dfs(ast)











