select * from jan2024;
select * from feb2024;
select * from mar2024;
select * from apr2024;
select * from ma2024;
select * from jun2024;
select * from jul2024;
select * from aug2024;
select * from sep2024;
select * from oct2024;
select * from nov2024;
select * from dec2024;
select * from expenses24;

CREATE TABLE Expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_name VARCHAR(255),
    expense_type VARCHAR(100),
    amount_paid DECIMAL(10, 2),
    expense_date DATE,
    description TEXT
);


CREATE TABLE Expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_name VARCHAR(255),
    expense_type VARCHAR(100),
    amount_paid DECIMAL(10, 2),
    expense_date DATE,
    description TEXT
);

INSERT INTO Expenses (expense_name, expense_type, amount_paid, expense_date, description)
VALUES ('Office Supplies', 'Office', 150.00, '2024-12-01', 'Purchase of office stationery');

SELECT * FROM Expenses;

SELECT * FROM Expenses WHERE expense_type = 'Office' AND amount_paid > 100;

UPDATE Expenses
SET amount_paid = 200.00
WHERE id = 1;

DELETE FROM Expenses WHERE id = 1;

SELECT COUNT(*) FROM Expenses;

SELECT SUM(amount_paid) AS total_expenses FROM Expenses;

SELECT AVG(amount_paid) AS average_expense FROM Expenses;

SELECT MAX(amount_paid) AS max_expense FROM Expenses;

SELECT MIN(amount_paid) AS min_expense FROM Expenses;

SELECT expense_type, SUM(amount_paid) AS total_per_type
FROM Expenses
GROUP BY expense_type;

SELECT * FROM Expenses
ORDER BY expense_date DESC;

SELECT * FROM Expenses
WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';

SELECT expense_name, amount_paid
FROM Expenses
WHERE amount_paid > (
    SELECT AVG(amount_paid) FROM Expenses
);

SELECT * FROM Expenses
ORDER BY expense_date DESC
LIMIT 1;

SELECT YEAR(expense_date) AS year, MONTH(expense_date) AS month, SUM(amount_paid) AS total_expenses
FROM Expenses
GROUP BY YEAR(expense_date), MONTH(expense_date);

SELECT expense_name, COUNT(*)
FROM Expenses
GROUP BY expense_name
HAVING COUNT(*) > 1;

SELECT DISTINCT expense_type FROM Expenses;

SELECT description,
    SUM(amount_paid) AS total_expense
FROM Expenses
GROUP BY description
ORDER BY total_expense DESC;


