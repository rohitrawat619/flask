import csv
import string

# Function to add a letter to the Email if it's a duplicate
def generate_unique_Email(Email, existing_Emails):
    alphabet = list(string.ascii_lowercase)
    modified_Email = Email
    i = 0
    # Keep adding a letter from 'a' to 'z' until a unique Email is found
    while modified_Email in existing_Emails:
        if i < len(alphabet):
            modified_Email = Email.split('@')[0] + alphabet[i] + '@' + Email.split('@')[1]
            i += 1
        else:
            # In case we run out of letters, append a number
            modified_Email = Email.split('@')[0] + str(i - len(alphabet) + 1) + '@' + Email.split('@')[1]
    return modified_Email

# Reading and updating the CSV file
def modify_duplicate_Emails(input_file, output_file=None):
    existing_Emails = set()
    
    # Read the input CSV file
    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)  # Read all rows into memory

    # Update duplicate Emails
    for row in rows:
        Email = row['Email']
        if Email in existing_Emails:
            unique_Email = generate_unique_Email(Email, existing_Emails)
            row['Email'] = unique_Email  # Modify the Email to make it unique
        existing_Emails.add(row['Email'])

    # Write the updated data to the same or a new CSV file
    output_file = output_file if output_file else input_file  # Overwrite if output is not provided
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = rows[0].keys()  # Use the same fieldnames as the input
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Processed CSV file has been saved as {output_file}")

# Usage
input_file = 'admission.csv'  # Replace with the path to your input CSV file
output_file = 'output_Emails.csv'  # Optional, replace with desired output file or None to overwrite input
modify_duplicate_Emails(input_file, output_file)