from chains.extraction_chain import extract_employee_info

text = """
Rahul Sharma is a Data Scientist at Infosys.
He is  years old and has 4 years of experience.
"""

try:
    result = extract_employee_info(text)

    print("Extracted Employee Information:")
    print(result)

except Exception as e:
    print("Error:", e)