-- Creating a trigger that will decrease the quantity
-- of an item after adding a new order

DELIMETER $$

CREATE TRIGGER decrease_item AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.quantity
		WHERE item_id = NEW.id;
	END$$
DELIMETER ;
