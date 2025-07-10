import pandas as pd

def simulate_query_response(document_data, query, method):
    """Simulates the Q&A response and accuracy based on the method."""

    if document_data.empty:
        return "Sorry, I could not find relevant information...", 0.0

    if method == "Traditional Textract (Simulated Low Accuracy)":
        return "Sorry, I could not find relevant information...", 0.0
    elif method == "AWS Textract Visual Q&A (Simulated Moderate Accuracy)":
        return "Simulated answer for moderate accuracy", 0.4
    elif method == "TalentMine (LLM-enhanced) (Simulated High Accuracy)":
        return "Simulated answer for high accuracy", 1.0
    else:
        return "Sorry, I could not find relevant information...", 0.0

import pandas as pd

def evaluate_all_methods(document_data, predefined_queries):
    """Runs predefined benchmark queries against document data and aggregates results."""

    results = []
    for query, expected_answer in predefined_queries.items():
        # Simulate a method (in this case, direct lookup)
        try:
            # Simple lookup based on names in the document (Example)
            for _, row in document_data.iterrows():
                if "Name" in document_data.columns and row["Name"] in query:
                    extracted_answer = str(row["HRA_Contribution"]) if "HRA_Contribution" in document_data.columns else "N/A"

                    accuracy = 1 if extracted_answer == expected_answer else 0
                    results.append({"Query": query, "Extracted_Answer": extracted_answer, "Expected_Answer": expected_answer, "Accuracy": accuracy})
                    break # Break after the first match

                elif "EmployeeID" in document_data.columns and str(row["EmployeeID"]) in query:

                    extracted_answer = str(row["HRA_Contribution"]) if "HRA_Contribution" in document_data.columns else "N/A"
                    accuracy = 1 if extracted_answer == expected_answer else 0
                    results.append({"Query": query, "Extracted_Answer": extracted_answer, "Expected_Answer": expected_answer, "Accuracy": accuracy})
                    break # Break after the first match
            else:
                # If no match is found after iterating through all rows

                results.append({"Query": query, "Extracted_Answer": "N/A", "Expected_Answer": expected_answer, "Accuracy": 0})


        except Exception as e:
            print(f"Error processing query: {query} - {e}")
            results.append({"Query": query, "Extracted_Answer": "Error", "Expected_Answer": expected_answer, "Accuracy": 0})

    return pd.DataFrame(results)

import pandas as pd
import matplotlib.pyplot as plt

def generate_visualizations(evaluation_results):
    """Generates charts and plots based on the `evaluation_results`."""

    if evaluation_results.empty:
        return

    try:
        evaluation_results['Accuracy'] = pd.to_numeric(evaluation_results['Accuracy'])
    except KeyError:
        raise KeyError("Required column 'Accuracy' is missing.")
    except ValueError:
        raise TypeError("Column 'Accuracy' must be numeric.")
        
    if 'Method' not in evaluation_results.columns:
        raise KeyError("Required column 'Method' is missing.")
    if 'Category' not in evaluation_results.columns:
        raise KeyError("Required column 'Category' is missing.")
    
    methods = evaluation_results['Method'].unique()

    for method in methods:
        method_data = evaluation_results[evaluation_results['Method'] == method]
        plt.figure(figsize=(8, 6))
        plt.bar(method_data['Category'], method_data['Accuracy'])
        plt.xlabel('Category')
        plt.ylabel('Accuracy')
        plt.title(f'Accuracy per Category for Method {method}')
        plt.tight_layout()
        plt.show()