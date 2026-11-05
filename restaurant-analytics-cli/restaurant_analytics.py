import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "orders.csv"

def init_db():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Customer", "Course", "Item", "Quantity", "Unit_Price", "Total"])

def record_order(customer, course, item, quantity, unit_price):
    quantity = int(quantity)
    unit_price = float(unit_price)
    total = round(quantity * unit_price, 2)
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([customer, course, item, quantity, unit_price, total])

def admin_login():
    username = input("Admin Username: ").strip()
    password = input("Admin Password: ").strip()
    return username == "admin" and password == "admin"

def generate_course_pie_chart(course_name):
    df = pd.read_csv(CSV_FILE).dropna()
    df["Quantity"] = df["Quantity"].astype(int)
    df["Total"] = df["Total"].astype(float)
    course_df = df[df["Course"] == course_name]
    if course_df.empty:
        print(f"[INFO] No order records found for course: {course_name}")
        return

    summary = course_df.groupby("Item")["Quantity"].sum()
    plt.figure(figsize=(7, 7))
    plt.pie(
        summary.values,
        labels=summary.index,
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title(f"Most Popular Dishes - {course_name}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    init_db()
    if admin_login():
        for course in ["Starters", "Main Course", "Dessert", "Beverages"]:
            generate_course_pie_chart(course)
    else:
        print("[ACCESS DENIED] Invalid credentials.")
