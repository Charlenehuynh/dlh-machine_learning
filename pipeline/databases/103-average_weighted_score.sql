--  creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE weighted_avg FLOAT DEFAULT 0;
    SELECT SUM(projects.weight * corrections.score) / SUM(projects.weight)  INTO weighted_avg 
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = weighted_avg WHERE users.id = user_id ;
END $$
DELIMITER;