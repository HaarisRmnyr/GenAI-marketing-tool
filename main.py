from utils.db_setup import create_db_and_table 
from utils.model_setup import generate_caption
from utils.ml_setup import load_campaign_data, prepare_data, train_model


def run_pipeline():
    # Step 1: Create database and table if not aleady present
    try:
        create_db_and_table()
    except:
        print("Database and table already exist.")

    # Step 2: Load and prepare data
    df = load_campaign_data()
    if (df.empty):
        print("No data found in the campaigns table.")
        return
    

    # Step 3: Train ML model
    X, y = prepare_data(df)
    model = train_model(X, y)
    print("Model trained successfully.")
    print(f"Coefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_}")

    # Step 4: Generate caption for a sample prompt
    print("\nGenerating caption for sample prompt...")
    for name in df[name]:
        caption = generate_caption(name)
        print(f"{name}: {caption}")

    
if __name__ == "__main__":
    run_pipeline()


