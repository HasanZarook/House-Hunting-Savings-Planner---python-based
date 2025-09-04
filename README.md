
# 🏡 House Hunting Savings Planner

This repository contains **three Python programs** that help calculate how long it will take to save for a house down payment.  
Each file introduces additional complexity, from simple fixed savings to salary raises and bisection search optimization.  

---

## 📂 Files Overview

### 1️⃣ house_hunting.py  
- Calculates the number of months required to save for a down payment.  
- Assumes:
  - Fixed salary
  - Fixed savings rate
  - Fixed interest rate  

👉 **Inputs**:  
- Annual salary  
- Portion of salary to save (decimal)  
- Total cost of dream house  

---

### 2️⃣ saving_with_raise.py  
- Extends the first program by adding a **semi-annual salary raise**.  
- More realistic as salaries usually increase over time.  

👉 **Inputs**:  
- Annual salary  
- Portion of salary to save (decimal)  
- Total cost of dream house  
- Semi-annual raise percentage (decimal)  

---

### 3️⃣ savings_bisection.py  
- Uses **bisection search** to find the best savings rate required to afford a house down payment within **36 months**.  
- Handles cases where it’s not possible to reach the goal even with 100% savings.  

👉 **Inputs**:  
- Starting annual salary (fixed values for house cost = 1,000,000 and semi-annual raise = 7%)  

👉 **Outputs**:  
- Best savings rate (decimal)  
- Steps taken in bisection search  

---

## 🛠️ Usage

Run any file in Python:

```bash
python house_hunting.py
````

```bash
python saving_with_raise.py
```

```bash
python savings_bisection.py
```

Provide inputs when prompted.

---

## 🧮 Example Run (for house\_hunting.py)

```
Enter your annual salary :120000
enter the percentage of saved amount in your monthly salary,put this value as decimal :0.10
How cost your dream house? 500000
How many months will take to save the down payment : 80 months
```

---

## 📊 Concepts Covered

* 💵 Financial modeling (savings + interest)
* 📈 Salary raises effect on savings
* 🔍 Bisection search for optimization
* 🧮 Simulation of time-based savings

---

## 👨‍💻 Authors

* Hasan Zarook (2021-CE-58)

---

## 📜 License

This project is licensed under the **MIT License**.

```

---
