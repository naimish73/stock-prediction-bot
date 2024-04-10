import joblib
import yfinance as yf
import plotly.graph_objects as go


# Load the model from .pkl file
# model = joblib.load('../../technical_analysis_model/model_pkl_files/decision_tree_model.pkl')
model = joblib.load('/home/rahul/Desktop/Rahul/DE SEM 6/stock-prediction-bot/technical_analysis/technical_analysis_model/model_pkl_files/decision_tree_model.pkl')

# Function to fetch latest data and make predictions
def fetch_data_and_predict(symbol,model_title,time_frame='1m'):
    # Fetch latest data
    ticker = yf.Ticker(symbol)
    data = ticker.history(interval=time_frame, period="1d")
    data.drop(columns=['Volume', 'Dividends', 'Stock Splits'], inplace=True)

    # Prepare data for prediction
    X = data[['Open', 'High', 'Low', 'Close']]

    # Predict using the model
    live_prediction = model.predict(X)

    # C lear previous graph
    # clear_output(wait=True)

    t1 = go.Scatter(x=data.index, y=data['Close'], mode='lines', name="Actual Close", line=dict(color='blue'))
    t2 = go.Scatter(x=data.index, y=live_prediction, mode='lines', name="Predicted Close", line=dict(color='red'))

    # Create layout for the plot
    layout = go.Layout(title=f'Stock Price Prediction With {model_title}', xaxis=dict(title='Date'), yaxis=dict(title='Price'))

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