import numpy as np

# def calculate_order_of_importance(data):
#     num_assets = len(data[0]) - 1  # Number of columns in the data excluding the PL column
#     correlations = []

#     asset_changes = np.array([row[:-1] for row in data])  # Extract all asset changes
#     pl_changes = np.array([row[-1] for row in data])  # Extract PL changes
    
#     for asset_idx in range(num_assets):
#         asset_change = asset_changes[:, asset_idx]
        
#         correlation = np.corrcoef(asset_change, pl_changes)[0, 1]
#         correlations.append((asset_idx, correlation))

#     correlations.sort(key=lambda x: abs(x[1]), reverse=True)
#     order_of_importance = [chr(ord('A') + asset_idx) for asset_idx, _ in correlations]
#     return ''.join(order_of_importance)

def calculate_order_of_importance(data):
    num_assets = len(data[0]) - 1  # Number of columns in the data excluding the PL column
    correlations = []

    for asset_idx in range(num_assets):
        asset_changes = np.array([row[asset_idx] for row in data])
        pl_changes = np.array([row[-1] for row in data])
        
        correlation = np.corrcoef(asset_changes, pl_changes)[0, 1]
        correlations.append((asset_idx, correlation))

    correlations.sort(key=lambda x: abs(x[1]), reverse=True)
    order_of_importance = [chr(ord('A') + asset_idx) for asset_idx, _ in correlations]
    return ''.join(order_of_importance)

with open('./Quant/OA/input_output/problem2/sample-input-1.txt', 'r') as f:
    data_string = f.read()

print(data_string)
data_rows = data_string.strip().split('\n')
data = [list(map(float, row.split(','))) for row in data_rows]
data_array = np.array(data)

print(calculate_order_of_importance(data_array))