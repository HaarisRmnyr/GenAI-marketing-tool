# GenAI-marketing-tool
A locally hosted AI-powered marketing assistant that predicts campaign performance and generates creative Instagram-style captions using Hugging Face's T5 model.

**Featuers:**

- **Generative AI**: Uses a pretrained T5 model to generate captions from product names
- **ML Insights Engine**: Predicts conversions based on impressions, clicks, and CTR using scikit-learn
- **SQLite Database**: Stores campaign data in a lightweight local database
- **Modular Architecture**: Clean separation of database, ML, and model logic
- **Integration Script**: `main.py` runs the full pipeline end-to-end


**Setup Instructions**

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/GenAI-marketing-tool.git
   cd GenAI-marketing-tool
2. **Install Dependancies:** pip install -r requirements.txt

3. **Run the Integration Script:** python main.py

**Sample Output:**

📊 ML Model Trained
Coefficients: [0.03, 0.12, 0.45]
Intercept: 5.2

📝 Generated Captions:
- EcoGlow LED Lamp: Brighten your space with eco-friendly brilliance!
- AquaPure Water Bottle: Hydration meets purity in every sip.



# What I learned
This project was a significant leap from my previous work with simple API calls. I went from having limited knowledge of using AI as an external service to understanding the complete machine learning lifecycle from start to finish.

I gained hands-on experience in:

**End-to-End ML Development:** I learned how to move beyond just consuming an API and truly build an AI solution. This involved setting up a database with SQLite3 and Python, performing complex SQL queries to source data, and handling the entire data preparation pipeline.

**Generative AI Workflows:** I gained a deep understanding of generative AI, including selecting the right pre-trained models, fine-tuning them on a custom dataset, and managing the model import and training process.
