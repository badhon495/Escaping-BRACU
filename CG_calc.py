# We are assuming that the user has taken 4 courses in each semester and he got same CGPA in all courses.
def calculate_cg(current_cg, semester, total_cg):
    total_cg = total_cg * (semester - 1) * 4
    weighted_cg = current_cg * 4
    total_cg += weighted_cg
    final_cg = total_cg / (semester * 4)
    return final_cg
