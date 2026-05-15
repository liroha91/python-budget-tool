# python-budget-tool/file_handler.py
# Includes File Handler functions

import csv

#--------------------------------------------------
# File Handler Functions (CSV right now, eventually JSON)
#--------------------------------------------------
def load_transactions():
  file_path = "transactions.csv"

  try:
    with open(file_path, mode='r', encoding='utf-8') as file:
      csv_reader = csv.DictReader(file)

      print(f"Successfully opened '{file_path}'. Processing rows:\n")
      for row in csv_reader:
        print(row)
        
  except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
  except PermissionError:
    print(f"Error: Permission denied. Close the file if it is open in another program.")
  except csv.Error as e:
    print(f"Error: Failed to parse the CSV structure on line {csv_reader.line_num}: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

#--------------------------------------------------

def save_transactions(transactions):
  file_path = "transactions.csv"
  
  if not transactions:
    print("No transactions to save.")
    return
  
  headers = transactions[0].keys()
    
  try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
      writer = csv.DictWriter(file, fieldnames=headers)
      writer.writeheader()
      writer.writerows(transactions)
    print(f"Success: Data safely saved to '{file_path}'.")
  except PermissionError:
    print(f"Error: Permission denied. Close '{file_path}' if it is open in another program.")
  except Exception as e:
    print(f"An unexpected error occurred while saving: {e}")

#--------------------------------------------------

def load_budget():
  file_path = "budget.csv"

  try:
    with open(file_path, mode='r', encoding='utf-8') as file:
      csv_reader = csv.DictReader(file)

      print(f"Successfully opened '{file_path}'. Processing rows:\n")
      for row in csv_reader:
        print(row)
  except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
  except PermissionError:
    print(f"Error: Permission denied. Close the file if it is open in another program.")
  except csv.Error as e:
    print(f"Error: Failed to parse the CSV structure on line {csv_reader.line_num}: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

#--------------------------------------------------

def save_budget(budget):
  file_path = "budget.csv"

  if not budget:
    print("No budget to save.")
    return

  headers = budget[0].keys()

  try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
      writer = csv.DictWriter(file, fieldnames=headers)
      writer.writeheader()
      writer.writerows(budget)
    print(f"Success: Data safely saved to '{file_path}'.")
  except PermissionError:
    print(f"Error: Permission denied. Close '{file_path}' if it is open in another program.")
  except Exception as e:
    print(f"An unexpected error occurred while saving: {e}")

#--------------------------------------------------

def export_summary(total_income, total_expenses, leftover):
  file_path = "budget_summary.txt"

  try:
    with open(file_path, mode='w', encoding='utf-8') as file:
      file.write("================= Budget Summary =================\n\n")
      file.write(f"Total Income: ${total_income}\n")
      file.write(f"Total Expenses: ${total_expenses}\n")
      file.write(f"Leftover: ${leftover}\n")

    print(f"Summary successfully exported to '{file_path}'.")

  except PermissionError:
    print(f"Error: Permission denied. Close '{file_path}' if it is open.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
