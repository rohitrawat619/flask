import re

# Sample raw data
data = [
    {"qs_rank": "1001 - 1200", "university": "London Metropolitan University"},
    {"qs_rank": "1001-1200", "university": "University of West London"},
    {"qs_rank": "184", "university": "University of York"},
    {"qs_rank": "151-160", "university": "University of Suffolk"},
    {"qs_rank": "1201", "university": "Teeside University"},
    {"qs_rank": "106", "university": "Buckinghamshire New University"},
    {"qs_rank": "34", "university": "University of Manchester"},
    {"qs_rank": "54", "university": "University of Bristol"},
    {"qs_rank": "901-950", "university": "Robert Gordon University"},
    {"qs_rank": "", "university": "Regent Collage London"},
    {"qs_rank": "901-950", "university": "University of Salford"},
    {"qs_rank": "951-1000", "university": "University of Central Lancashire"},
    {"qs_rank": "526", "university": "Coventry University"},
    {"qs_rank": "", "university": "York St John University"},
    {"qs_rank": "251-300", "university": "Roehampton University"},
    {"qs_rank": "1000 - 1200", "university": "Birmingham City University"},
    {"qs_rank": "901 - 950", "university": "University of East London"},
    {"qs_rank": "741-750", "university": "University of Westminster"},
]

def extract_numeric_rank(rank_str):
    """Extract a numeric value from a QS rank string for sorting."""
    if not rank_str.strip():
        return float('inf')  # Treat empty rank as lowest priority
    nums = re.findall(r'\d+', rank_str)
    if len(nums) == 1:
        return int(nums[0])
    elif len(nums) > 1:
        # If it's a range like "1001-1200", take the average
        return (int(nums[0]) + int(nums[1])) / 2
    return float('inf')

# Sort the list using extracted QS rank
sorted_universities = sorted(data, key=lambda x: extract_numeric_rank(x["qs_rank"]))

# Print the sorted result
for uni in sorted_universities:
    print(f"{uni['qs_rank']:<10} {uni['university']}")