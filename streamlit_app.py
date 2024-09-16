import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to plot heatmap
def plot_heatmap(corr_matrix):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', cbar=True)
    st.pyplot(plt)

# Streamlit app
def main():
    st.title("Stock Correlation Heatmap Viewer")

    # URL to your CSV file on GitHub
    csv_url = "https://raw.githubusercontent.com/Clinton-William/gdp-dashboard/data/high_correlation_pairs.csv"
    
    # Read the CSV file directly from GitHub
    df = pd.read_csv(csv_url, index_col=0)
    
    # Display the DataFrame
    st.write("Data Preview:")
    st.dataframe(df)
    
    # Display correlation heatmap
    st.write("Correlation Heatmap:")
    
    # Make the heatmap scrollable by limiting the display size
    corr_matrix = df  # Assuming the CSV already contains the correlation matrix
    
    scrollable_area = st.container()
    with scrollable_area:
        scroll_height = st.slider("Adjust Scroll Height", 400, 1200, 600)  # Adjust scroll height
        st.markdown(
            f"""
            <style>
            .stApp {{
                overflow: auto;
                max-height: {scroll_height}px;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        plot_heatmap(corr_matrix)

if __name__ == "__main__":
    main()
