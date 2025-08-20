-- 1. Отримати всі завдання певного користувача (наприклад user_id = 3)
SELECT * FROM tasks WHERE user_id = 3;

-- 2. Вибрати завдання зі статусом 'new'
SELECT * FROM tasks 
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Оновити статус завдання (task_id = 5 → 'in progress')
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 5;

-- 4. Користувачі без жодного завдання
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 5. Додати нове завдання для конкретного користувача (user_id = 3)
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New Task', 'Task description', (SELECT id FROM status WHERE name='new'), 3);

-- 6. Отримати всі незавершені завдання
SELECT * FROM tasks 
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалити завдання (id = 7)
DELETE FROM tasks WHERE id = 7;

-- 8. Знайти користувачів з email, що містить '@gmail.com'
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- 9. Оновити ім'я користувача (id = 2)
UPDATE users SET fullname = 'New Name' WHERE id = 2;

-- 10. Кількість завдань за статусами
SELECT s.name, COUNT(t.id) 
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 11. Завдання користувачів з певним доменом (наприклад '@example.com')
SELECT t.* 
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 12. Завдання без опису
SELECT * FROM tasks WHERE description IS NULL OR description = '';

-- 13. Користувачі + їхні завдання у статусі 'in progress'
SELECT u.fullname, t.title 
FROM users u
JOIN tasks t ON u.id = t.user_id
JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

-- 14. Користувачі + кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) 
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id;