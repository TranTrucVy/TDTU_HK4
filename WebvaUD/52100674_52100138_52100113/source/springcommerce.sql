CREATE DATABASE IF NOT EXISTS spring_commerce;
USE spring_commerce;

CREATE TABLE IF NOT EXISTS Categories (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  parent_id INT DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  alias VARCHAR(255) NOT NULL UNIQUE,
  price int NOT NULL,
  description TEXT DEFAULT NULL,
  size VARCHAR(255) DEFAULT NULL,
  short_description VARCHAR(255) DEFAULT NULL,
  quantity INT NOT NULL DEFAULT 0,
  deleted BOOLEAN NOT NULL DEFAULT FALSE,
  categories TEXT DEFAULT NULL,
  related_products TEXT DEFAULT NULL,
  feature BOOLEAN NOT NULL DEFAULT FALSE,
  image VARCHAR(255) DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Customer_New (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  full_name VARCHAR(255) DEFAULT NULL,
  phone_number VARCHAR(255) DEFAULT NULL,
  address TEXT DEFAULT NULL,
  gender ENUM('MALE', 'FEMALE', 'OTHER') DEFAULT NULL,
  birthday DATE DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  role VARCHAR(255) NOT NULL
);




CREATE TABLE IF NOT EXISTS Order_New (
  id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL,
  shipping_address TEXT NOT NULL,
  order_date DATETIME NOT NULL,
  total_price DECIMAL(10,2) NOT NULL,
  items JSON NOT NULL,
  status VARCHAR(50) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);


INSERT INTO Categories (name) VALUES ('Shoes');

INSERT INTO Products (name, alias, price, description, size, short_description, quantity, deleted, categories, feature, image)
VALUES ('Nike Air Max 90', 'nike-air-max-90', 100, "The Nike Air Max 90 is a retro running shoe with Max Air® in the heel for comfort and cushioning. Leather or canvas upper works with a polyurethane midsole and a durable rubber outsole for comfort, support, and durability. The Nike Air Max 90 is available in men's, women's, and kids' sizes.", 'US 8.5', 'Retro running shoe', 50, 0, '1', 1, 'nike-air-max-90.jpg');
INSERT INTO Products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image) 
VALUES ('Adidas Prophere', 'adidas-prophere', 350, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.', 995, false, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[2,3,5]', true, 'https://shop.cyberlearn.vn/images/adidas-prophere.png'),
       ('Adidas Prophere Black White', 'adidas-prophere-black-white', 450, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.', 990, false, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[1,4,6]', false, 'https://shop.cyberlearn.vn/images/adidas-prophere-black-white.png'),
       ('Adidas Prophere Customize', 'adidas-prophere-customize', 375, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.', 415, false, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[4,5,7]', true, 'https://shop.cyberlearn.vn/images/adidas-prophere-customize.png'),
       ('Adidas Super Star Red', 'adidas-super-star-red', 465, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.', 542, false, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[7,8,6]', false, 'https://shop.cyberlearn.vn/images/adidas-super-star-red.png');

INSERT INTO Customers (email, password, full_name, phone_number, address, gender, birthday)
VALUES ('john.doe@example.com', 'password', 'John Doe', '123-456-7890', '123 Main St, Anytown, USA', 'MALE', '1990-01-01');

INSERT INTO Orders (customer_id, shipping_address, order_date, total_price, items, status)
VALUES (1, '456 Market St, Anytown, USA', '2023-04-02 10:00:00', 100.00, '{"item_id": 1, "quantity": 2}', 'PENDING');

INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image)
VALUES ('Adidas Tenisky Super Star', 'adidas-tenisky-super-star', 250, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.\r\n\r\n', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.\r\n\r\n', 456, 0, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[4,2,3]', 0, 'https://shop.cyberlearn.vn/images/adidas-tenisky-super-star.png');

INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image)
VALUES ('Adidas Ultraboost 4', 'adidas-ultraboost-4', 450, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.\r\n\r\n', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.\r\n\r\n', 854, 0, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[8,2,1]', 1, 'https://shop.cyberlearn.vn/images/adidas-ultraboost-4.png');

INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image)
VALUES ('Adidas Yeezy 350', 'adidas-yeezy-350', 750, 'The adidas Primeknit upper wraps the foot with a supportive fit that enhances movement.\r\n\r\n', '[36,37,38,39,40,41,42]', 'The midsole contains 20% more Boost for an amplified Boost feeling.\r\n\r\n', 524, 0, '[{\"id\":\"ADIDAS\",\"category\":\"ADIDAS\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[1,4,6]', 0, 'https://shop.cyberlearn.vn/images/adidas-yeezy-350.png');

INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image) VALUES
('Nike Air Max 270 React', 'nike-air-max-270-react', 750, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 445, false, '[{"id":"NIKE","category":"NIKE"},{"id":"MEN","category":"MEN"},{"id":"WOMEN","category":"WOMEN"}]', '[11,9,15,16]', false, 'https://shop.cyberlearn.vn/images/nike-air-max-270-react.png'),
('Nike Flyknit', 'nike-flyknit', 350, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 367, false, '[{"id":"NIKE","category":"NIKE"},{"id":"MEN","category":"MEN"},{"id":"WOMEN","category":"WOMEN"}]', '[12,14,17,11]', true, 'https://shop.cyberlearn.vn/images/nike-flyknit.png'),
('Nike React Element', 'nike-react-element', 480, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 589, false, '[{"id":"NIKE","category":"NIKE"},{"id":"MEN","category":"MEN"},{"id":"WOMEN","category":"WOMEN"}]', '[16,15,13]', false, 'https://shop.cyberlearn.vn/images/nike-react-element.png');

INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image)
VALUES
('Nike SP Dunk', 'nike-sp-dunk', 450, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 582, false, '[{\"id\":\"NIKE\",\"category\":\"NIKE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[15,14,13]', false, 'https://shop.cyberlearn.vn/images/nike-sp-dunk.png'),
('Van Old School', 'van-old-school', 150, 'The Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers, padded collars, elastic side accents, and signature rubber waffle outsoles.\r\n', '[36,37,38,39,40,41,42]', '\r\nThe Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers', 654, false, '[{\"id\":\"VANS_CONVERSE\",\"category\":\"VANS CONVERSE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[18,19,1,2,3]', true, 'https://shop.cyberlearn.vn/images/van-old-school.png'),
('Vans black black', 'vans-black-black', 100, 'The Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers, padded collars, elastic side accents, and signature rubber waffle outsoles.\r\n', '[36,37,38,39,40,41,42]', '\r\nThe Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers', 985, false, '[{\"id\":\"VANS_CONVERSE\",\"category\":\"VANS CONVERSE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[19,17,4,5,6]', false, 'https://shop.cyberlearn.vn/images/vans-black-black.png'),
('Converse Chuck Taylor', 'converse-chuck-taylor', 125, 'The Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers, padded collars, elastic side accents, and signature rubber waffle outsoles.\r\n', '[36,37,38,39,40,41,42]', '\r\nThe Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers', 756, false, '[{\"id\":\"VANS_CONVERSE\",\"category\":\"VANS CONVERSE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[18,17,8,9,10]', true, 'https://shop.cyberlearn.vn/images/converse-chuck-taylor.png');


INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image) VALUES
('Nike Flyknit', 'nike', 750, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 445, false, '[{"id":"NIKE","category":"NIKE"},{"id":"MEN","category":"MEN"},{"id":"WOMEN","category":"WOMEN"}]', '[11,9,15,16]', false, 'https://shop.cyberlearn.vn/images/nike-flyknit.png'),
('Nike Air Max 270 React', 'nike-air-max-720', 350, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 367, false, '[{"id":"NIKE","category":"NIKE"},{"id":"MEN","category":"MEN"},{"id":"WOMEN","category":"WOMEN"}]', '[12,14,17,11]', true, 'https://shop.cyberlearn.vn/images/nike-air-max-270-react.png');


INSERT INTO products (name, alias, price, description, size, short_description, quantity, deleted, categories, related_products, feature, image)
VALUES
('Nike Dunk', 'nike-dunk', 450, 'Nike shoe is the rare high-percentage shooter who''s also a coach''s dream on D. Designed for his unrivaled 2-way game, the PG 4 unveils a new cushioning system that''s lightweight, articulated and responsive, ideal for players like PG who go hard every play.\r\n\r\n', '[36,37,38,39,40,41,42]', 'Paul George is the rare high-percentage shooter', 582, false, '[{\"id\":\"NIKE\",\"category\":\"NIKE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[15,14,13]', false, 'https://shop.cyberlearn.vn/images/nike-sp-dunk.png'),
('Van SK8', 'van-sk8', 150, 'The Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers, padded collars, elastic side accents, and signature rubber waffle outsoles.\r\n', '[36,37,38,39,40,41,42]', '\r\nThe Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers', 654, false, '[{\"id\":\"VANS_CONVERSE\",\"category\":\"VANS CONVERSE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[18,19,1,2,3]', true, 'https://shop.cyberlearn.vn/images/van-old-school.png'),
('Vans black', 'vans-new', 100, 'The Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers, padded collars, elastic side accents, and signature rubber waffle outsoles.\r\n', '[36,37,38,39,40,41,42]', '\r\nThe Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers', 985, false, '[{\"id\":\"VANS_CONVERSE\",\"category\":\"VANS CONVERSE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[19,17,4,5,6]', false, 'https://shop.cyberlearn.vn/images/vans-black-black.png'),
('Converse Chuck', 'converse-taylor', 125, 'The Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers, padded collars, elastic side accents, and signature rubber waffle outsoles.\r\n', '[36,37,38,39,40,41,42]', '\r\nThe Vans Coastal Classic Slip-On features sturdy low profile canvas and textile uppers', 756, false, '[{\"id\":\"VANS_CONVERSE\",\"category\":\"VANS CONVERSE\"},{\"id\":\"MEN\",\"category\":\"MEN\"},{\"id\":\"WOMEN\",\"category\":\"WOMEN\"}]', '[18,17,8,9,10]', true, 'https://shop.cyberlearn.vn/images/converse-chuck-taylor.png');

INSERT INTO Customer_New (email, password, full_name, phone_number, address, gender, birthday, role)
VALUES 
('admin@gmail.com', 'admin', 'John Doe', '123456789', '123 Main St, Anytown USA', 'MALE', '1990-01-01', 'ADMIN');
