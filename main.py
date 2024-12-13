# main.py

##############################################
from CG_calc import calculate_cg

# Input values
current_cg = float(input("Enter the current CG: "))
level = int(input("Enter the current level: "))

# Predefined total CG
total_cg = 4  # This should be updated across calls if necessary

# Calculate the final CG
final_cg = calculate_cg(current_cg, level, total_cg)

# Display the final CG
print(f"The final CG is: {final_cg:.2f}")
##############################################
