# Original list with possible duplicates
universities = [
    "Cranfield University",
    "Cardiff Metropolitan University",
    "Leeds Trinity University",
    "Wales University Trinity Saint David",
    "University Liverpool Hope",
    "University of Aberdeen",
    "University of Surrey",
    "Brunel University London",
    "Aston University",
    "University of Striling",
    "University of Hull",
    "Northumbria University",
    "Ulster University",
    "Wrexham University",
    "Kingston University",
    "Southampton Solent University",
    "University of Portsmouth",
    "Aberystwyth University",
    "University of Greenwich",
    "De Montfort University",
    "Middlesex University",
    "University of Brington",
    "London South Bank University",
    "University of Hertfordshire",
    "Staffordshire University",
    "University of Bedfordshire",
    "Leeds Beckett University",
    "Sheffield Hallam University",
    "University of Wolverhampton",
    "University of Chester",
    "University of Sunderland"
]

# Remove duplicates while preserving order
seen = set()
unique_universities = []
for uni in universities:
    if uni not in seen:
        unique_universities.append(uni)
        seen.add(uni)

# Print the cleaned list
print("Unique universities:")
for uni in unique_universities:
    print(uni)