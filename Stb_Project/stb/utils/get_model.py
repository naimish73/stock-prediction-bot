import joblib
import yfinance as yf
import plotly.graph_objects as go
import pickle

# Load the model from .pkl file
model = joblib.load('/home/rahul/Desktop/Rahul/DE SEM 6/stock-prediction-bot/technical_analysis/technical_analysis_model/model_pkl_files/decision_tree_model.pkl')

# Load the model from .pkl file

# Load the model from the pickle file
with open('/home/rahul/Desktop/Rahul/DE SEM 6/stock-prediction-bot/technical_analysis/technical_analysis_model/model_pkl_files/RandomForestRegressor.pkl', 'rb') as f:
    Randomforest = pickle.load(f)


with open('/home/rahul/Desktop/Rahul/DE SEM 6/stock-prediction-bot/technical_analysis/technical_analysis_model/model_pkl_files/DesicionTreeModel.pkl', 'rb') as f:
    DecisionTree = pickle.load(f)


with open('/home/rahul/Desktop/Rahul/DE SEM 6/stock-prediction-bot/technical_analysis/technical_analysis_model/model_pkl_files/XGBoost.pkl', 'rb') as f:
    XgBoostModel = pickle.load(f)





# Function to fetch latest data and make predictions
def XgBoost_predict(symbol,time_frame='1m'):
    # Fetch latest data
    ticker = yf.Ticker(symbol)
    data = ticker.history(interval=time_frame, period="1d")
    data.reset_index(inplace=True)
    data.drop(columns=['Datetime','Volume', 'Dividends', 'Stock Splits'], inplace=True)

    # # Prepare data for prediction
    # X = data[['Open', 'High', 'Low', 'Close']]

    # Predict using the model
    XgBoostModel_pred = XgBoostModel.predict(data)

    last_actual_value = data['Close'].iloc[-1]
    last_predicted_value = XgBoostModel_pred[-1]
    difference = round(((last_actual_value - last_predicted_value)/last_actual_value)*100, 3)
    
    
    # C lear previous graph
    # clear_output(wait=True)

    t1 = go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Actual Close", line=dict(color='blue'))
    t2 = go.Scatter(x=data.index, y=XgBoostModel_pred, mode='lines', name="Predicted Close", line=dict(color='red'))

    # Create layout for the plot
    layout = go.Layout(title=f'Stock Price Prediction With XgBoost Model \t\t\t Actual Value : {last_actual_value} \t\t\t Predicted Value : {last_predicted_value} \t\t\t Difference(%) : {difference}% ', xaxis=dict(title='Date'), yaxis=dict(title='Price'))

    # Combine traces and layout into a figure
    fig = go.Figure(data=[t1, t2], layout=layout)

    return fig

def DecisionTree_predict(symbol,time_frame='1m'):
    # Fetch latest data
    ticker = yf.Ticker(symbol)
    data = ticker.history(interval=time_frame, period="1d")
    data.reset_index(inplace=True)
    data.drop(columns=['Datetime','Volume', 'Dividends', 'Stock Splits'], inplace=True)

    # # Prepare data for prediction
    # X = data[['Open', 'High', 'Low', 'Close']]

    # Predict using the model
    DecisionTree_pred = DecisionTree.predict(data)
    
    last_actual_value = data['Close'].iloc[-1]
    last_predicted_value = DecisionTree_pred[-1]
    difference = round(((last_actual_value - last_predicted_value)/last_actual_value)*100, 3)
    

    # C lear previous graph
    # clear_output(wait=True)

    t1 = go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Actual Close", line=dict(color='blue'))
    t2 = go.Scatter(x=data.index, y=DecisionTree_pred, mode='lines', name="Predicted Close", line=dict(color='red'))

    # Create layout for the plot
    layout = go.Layout(title=f'Stock Price Prediction With Decision1 Tree Model \t\t\t Actual Value : {last_actual_value} \t\t\t Predicted Value : {last_predicted_value} \t\t\t Difference(%) : {difference}% ', xaxis=dict(title='Date'), yaxis=dict(title='Price'))

    # Combine traces and layout into a figure
    fig = go.Figure(data=[t1, t2], layout=layout)
    return fig


def DecisionTree_model_predict(symbol,time_frame='1m'):
    # Fetch latest data
    ticker = yf.Ticker(symbol)
    data = ticker.history(interval=time_frame, period="1d")
    data.reset_index(inplace=True)
    data.drop(columns=['Datetime','Volume', 'Dividends', 'Stock Splits'], inplace=True)

    # # Prepare data for prediction
    # X = data[['Open', 'High', 'Low', 'Close']]

    # Predict using the model
    DecisionTree_pred = model.predict(data)
    last_actual_value = data['Close'].iloc[-1]
    last_predicted_value = DecisionTree_pred[-1]
    difference = round(((last_actual_value - last_predicted_value)/last_actual_value)*100, 3)
    

    # C lear previous graph
    # clear_output(wait=True)

    t1 = go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Actual Close", line=dict(color='blue'))
    t2 = go.Scatter(x=data.index, y=DecisionTree_pred, mode='lines', name="Predicted Close", line=dict(color='red'))

    # Create layout for the plot
    layout = go.Layout(title=f'Stock Price Prediction With Decision Tree Model \t\t\t Actual Value : {last_actual_value} \t\t\t Predicted Value : {last_predicted_value} \t\t\t Difference(%) : {difference}% ', xaxis=dict(title='Date'), yaxis=dict(title='Price'))

    # Combine traces and layout into a figure
    fig = go.Figure(data=[t1, t2], layout=layout)
    return fig

def RandomForest_predict(symbol,time_frame='1m'):
    # Fetch latest data
    ticker = yf.Ticker(symbol)
    data = ticker.history(interval=time_frame, period="1d")
    data.reset_index(inplace=True)
    data.drop(columns=['Datetime','Volume', 'Dividends', 'Stock Splits'], inplace=True)

    # # Prepare data for prediction
    # X = data[['Open', 'High', 'Low', 'Close']]

    # Predict using the model
    Randomforest_pred = Randomforest.predict(data)

    last_actual_value = data['Close'].iloc[-1]
    last_predicted_value = Randomforest_pred[-1]
    difference = round(((last_actual_value - last_predicted_value)/last_actual_value)*100, 3)
    
    # C lear previous graph
    # clear_output(wait=True)

    t1 = go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Actual Close", line=dict(color='blue'))
    t2 = go.Scatter(x=data.index, y=Randomforest_pred, mode='lines', name="Predicted Close", line=dict(color='red'))

    # Create layout for the plot
    layout = go.Layout(title=f'Stock Price Prediction With Random Forest Model \t\t\t Actual Value : {last_actual_value} \t\t\t Predicted Value : {last_predicted_value} \t\t\t Difference(%) : {difference}% ', xaxis=dict(title='Date'), yaxis=dict(title='Price'))

    # Combine traces and layout into a figure
    fig = go.Figure(data=[t1, t2], layout=layout)
    return fig

"""# Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Actual Close', color='blue')
    plt.plot(data.index, live_prediction, label='Predicted Close', color='red', linestyle='dashed')
    plt.title('Actual vs Predicted Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()"""