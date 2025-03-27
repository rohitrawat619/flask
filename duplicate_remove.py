# # Original list with possible duplicates
# universities = [
#     "Cranfield University",
#     "Cardiff Metropolitan University",
#     "Leeds Trinity University",
#     "Wales University Trinity Saint David",
#     "University Liverpool Hope",
#     "University of Aberdeen",
#     "University of Surrey",
#     "Brunel University London",
#     "Aston University",
#     "University of Striling",
#     "University of Hull",
#     "Northumbria University",
#     "Ulster University",
#     "Wrexham University",
#     "Kingston University",
#     "Southampton Solent University",
#     "University of Portsmouth",
#     "Aberystwyth University",
#     "University of Greenwich",
#     "De Montfort University",
#     "Middlesex University",
#     "University of Brington",
#     "London South Bank University",
#     "University of Hertfordshire",
#     "Staffordshire University",
#     "University of Bedfordshire",
#     "Leeds Beckett University",
#     "Sheffield Hallam University",
#     "University of Wolverhampton",
#     "University of Chester",
#     "University of Sunderland"
# ]

# # Remove duplicates while preserving order
# seen = set()
# unique_universities = []
# for uni in universities:
#     if uni not in seen:
#         unique_universities.append(uni)
#         seen.add(uni)

# # Print the cleaned list
# print("Unique universities:")
# for uni in unique_universities:
#     print(uni)


import pandas as pd

# Sample Data (Replace with your actual file)
data = {
    "QS": [80, 104, 129, 741, 601, 531, 567, 408, 380, 285, 256, 851],
    "University": [
        "University of Southampton",
        "University of St Andrews",
        "Newcastle University",
        "UWE Bristol",
        "Manchester Metropolitan",
        "University of Bradford",
        "University of Huddersfield",
        "University of Birkbeck",
        "University of Kent",
        "University of Leicester",
        "Heriot-Watt University",
        "University of Lincoln"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort by QS Ranking
df_sorted = df.sort_values(by="QS", ascending=True)

# Save to CSV
df_sorted.to_csv("sorted_universities.csv", index=False)

# Display sorted universities
print(df_sorted)