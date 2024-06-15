-- Creating a stored procedure that computes
-- and stores the score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	DECLARE avg_score DECIMAL(5, 2);

	-- average score for a specific user
        SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = user_id;

	UPDATE users
	SET average_score = avg_score
        WHERE id = user_id;
END$$

DELIMITER ;
