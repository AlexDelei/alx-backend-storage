-- Creating a trigger that will reset
-- the valid_email attribute field

DELIMITER $$

CREATE TRIGGER reset_email_validity AFTER UPDATE ON users
FOR EACH ROW
	BEGIN
		IF NEW.email <> OLD.email THEN
			SET NEW.valid_email = FALSE;
		END IF;
	END$$
DELIMITER ;

