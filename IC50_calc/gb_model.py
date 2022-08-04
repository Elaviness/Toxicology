from sklearn.ensemble import GradientBoostingRegressor
from joblib import load

gbm: GradientBoostingRegressor = load('gb_full_model.joblib')