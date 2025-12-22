#Department Payroll Calculator         
def calculate_payroll(filename):
    departments_total = {}
    overtime_employees = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")     
            if len(parts) != 4:
                continue
            name, category, hours, rate = parts

            try:
                hours = float(hours)
                rate = float(rate)
                pay = hours * rate
                departments_total[category] = departments_total.get(category, 0) + pay
                if hours > 40:
                    overtime_employees.append((name, hours))
            except (ValueError, IndexError):
                continue
        return departments_total, overtime_employees



def generate_payroll_report(dept_costs, overtime_staff):
    with open("payroll_summary.txt", "w") as infile:
        infile.write("DEPARTMENT WAGE COSTS\n")
        infile.write("-" * 20 + "\n")
        for department, tot_cost in dept_costs.items():
            infile.write(f"{department}: ${tot_cost:.2f}\n")
        infile.write("\nOVERTIME ALERTS (> 40 Hours)\n")
        infile.write("-" * 20 + "\n")
        for name, hours in overtime_staff:
            infile.write(f"{name}({hours} hours)\n")
            

dept_costs, overtime_staff = calculate_payroll("timesheet.txt")
print(generate_payroll_report(dept_costs, overtime_staff))