DECLARE 
    items_count INT NOT NULL DEFAULT 1; 
BEGIN
    FOR i IN 1..items_count LOOP
        INSERT INTO Diamond (diamond_index, color, cut, clarity, carat_weight)
            VALUES ('9', 'F', 'Ideal', 'IF', '0.2'); 

        INSERT INTO Diamond (diamond_index, color, cut, clarity, carat_weight)
            VALUES ('10', 'J', 'Premium', 'VS2', '0.31');

        INSERT INTO Diamond (diamond_index, color, cut, clarity, carat_weight)
            VALUES ('11', 'I', 'Good', 'VS1', '0.52'); 
    END LOOP;
END;
    
