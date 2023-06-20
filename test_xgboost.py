import xgboost as xgb

try:
    # Set up the parameters for XGBoost
    params = {
        "tree_method": "gpu_hist",
        "objective": "binary:logistic",
        "max_depth": 4,
        "n_jobs": 1,
    }
    # Train an XGBoost model on a sample dataset
    dtrain = xgb.DMatrix(data, label=label)
    model = xgb.train(params, dtrain)
    print("XGBoost with GPU is working.")
except:
    print("XGBoost with GPU is not working.")

